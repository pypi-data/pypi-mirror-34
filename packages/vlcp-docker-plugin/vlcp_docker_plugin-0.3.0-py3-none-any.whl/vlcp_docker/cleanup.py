'''
Created on 2016/11/3

:author: hubo
'''

from __future__ import print_function
from vlcp.config import manager
from vlcp.scripts.script import ScriptModule 
import vlcp.service.sdn.viperflow as viperflow
import vlcp.service.kvdb.objectdb as objectdb
from vlcp.server.module import depend, call_api
from vlcp.utils.connector import TaskPool
from vlcp.protocol.http import Http, HttpConnectionStateEvent
import subprocess
from time import sleep
import sys
from vlcp_docker.dockerplugin import _unplug_ovs, _delete_veth
import os
import os.path
from vlcp.event.connection import Client
from vlcp.event.stream import MemoryStream
import json
import vlcp.utils.encoders as encoders
from vlcp.event.event import M_
try:
    from shlex import quote as shell_quote
except:
    from pipes import quote as shell_quote
import itertools


_find_invalid_ovs = '''#/bin/bash
%s find interface error!=[] | grep name | grep %s | grep -oP '".*"' | awk '{print substr($1, 2, length($1) - 2)}'
'''

_find_unused_veth = '''#/bin/bash
%s link show | grep '\-tap@'%s | awk '{print $2}' | grep -oP '.*\-tap'
'''

def _bytes(s, encoding = 'ascii'):
    if isinstance(s, str):
        return s.encode(encoding)
    else:
        return s

def _str(s, encoding = 'utf-8'):
    if not isinstance(s, str):
        return s.decode(encoding)
    else:
        return s

@depend(viperflow.ViperFlow, objectdb.ObjectDB)
class Cleanup(ScriptModule):
    '''
    Clean up unreleased veth devices, delete unreleased logical ports. Comparing current logical ports
    with docker API result
    
    cleanup.py -f <configfile> [-H <endpoint>] [--skipovs] [--skipiplink] [--skiplogicalport] [--nodockerinfo]
    
    -H or --host:       specify docker API endpoint
    --skipovs:          do not remove invalid ports from OpenvSwitch
    --skipiplink:       do not remove extra veth devices
    --skiplogicalport:  do not remove unreleased logical ports
    --nodockerinfo:     do not detect docker info, always delete logical ports
    
    '''
    options = (('skipovs', None, False),
               ('skipiplink', None, False),
               ('skiplogicalport', None, False),
               ('host', 'H', True)
               )
    async def run(self, host = None, skipovs = None, skipiplink = None, skiplogicalport = None):
        skipovs = (skipovs is not None)
        skipiplink = (skipiplink is not None)
        skiplogicalport = (skiplogicalport is not None)
        pool = TaskPool(self.scheduler)
        pool.start()
        if host is None:
            host = os.environ.get('DOCKER_HOST', 'unix:///var/run/docker.sock')
        enable_ssl = os.environ.get('DOCKER_TLS_VERIFY', '')
        cert_root_path = os.environ.get('DOCKER_CERT_PATH', '~/.docker')
        ca_path, cert_path, key_path = [os.path.join(cert_root_path, f) for f in ('ca.pem', 'cert.pem', 'key.pem')]
        if '/' not in host:
            if enable_ssl:
                host = 'ssl://' + host
            else:
                host = 'tcp://' + host
        self._docker_conn = None
        http_protocol = Http(False)
        http_protocol.defaultport = 2375
        http_protocol.ssldefaultport = 2375
        http_protocol.persist = False
        
        def _create_docker_conn():
            self._docker_conn = Client(host, http_protocol, self.scheduler, key_path, cert_path, ca_path)
            self._docker_conn.start()
            return self._docker_conn
        
        async def call_docker_api(path, data = None, method = None):
            if self._docker_conn is None or not self._docker_conn.connected:
                _create_docker_conn()
                conn_up = HttpConnectionStateEvent.createMatcher(HttpConnectionStateEvent.CLIENT_CONNECTED)
                conn_noconn = HttpConnectionStateEvent.createMatcher(HttpConnectionStateEvent.CLIENT_NOTCONNECTED)
                _, m = await M_(conn_up, conn_noconn)
                if m is conn_noconn:
                    raise IOError('Cannot connect to docker API endpoint: ' + repr(host))
            if method is None:
                if data is None:
                    method = b'GET'
                else:
                    method = b'POST'
            if data is None:
                final_resp, _ = await http_protocol.request_with_response(
                                            self.apiroutine,
                                            self._docker_conn,
                                            b'docker',
                                            _bytes(path),
                                            method,
                                            [(b'Accept-Encoding', b'gzip, deflate')]
                                        )
            else:
                final_resp, _ = await http_protocol.request_with_response(
                                            self.apiroutine,
                                            self._docker_conn,
                                            b'docker',
                                            _bytes(path),
                                            method,
                                            [(b'Content-Type', b'application/json;charset=utf-8'),
                                             (b'Accept-Encoding', b'gzip, deflate')],
                                            MemoryStream(_bytes(json.dumps(data))))
            output_stream = final_resp.stream
            try:
                if final_resp.statuscode >= 200 and final_resp.statuscode < 300:
                    if output_stream is not None and b'content-encoding' in final_resp.headerdict:
                        ce = final_resp.headerdict.get(b'content-encoding')
                        if ce.lower() == b'gzip' or ce.lower() == b'x-gzip':
                            output_stream.getEncoderList().append(encoders.gzip_decoder())
                        elif ce.lower() == b'deflate':
                            output_stream.getEncoderList().append(encoders.deflate_decoder())
                    if output_stream is None:
                        return {}
                    else:
                        data = await output_stream.read(self.apiroutine)
                        return json.loads(data.decode('utf-8'))
                else:
                    raise ValueError('Docker API returns error status: ' + repr(final_resp.status))
            finally:
                if output_stream is not None:
                    output_stream.close(self.scheduler)
        
        async def execute_bash(script, ignoreerror = True):
            def task():
                try:
                    sp = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    outdata, errdata = sp.communicate(_bytes(script))
                    sys.stderr.write(_str(errdata))
                    errno = sp.poll()
                    if errno != 0 and not ignoreerror:
                        print('Script failed, output:\n', repr(outdata), file=sys.stderr)
                        raise ValueError('Script returns %d' % (errno,))
                    else:
                        return _str(outdata)
                finally:
                    if sp.poll() is None:
                        try:
                            sp.terminate()
                            sleep(2)
                            if sp.poll() is None:
                                sp.kill()
                        except Exception:
                            pass
            return await pool.run_task(self.apiroutine, task)
        
        ovsbridge = manager.get('module.dockerplugin.ovsbridge', 'dockerbr0')
        vethprefix = manager.get('module.dockerplugin.vethprefix', 'vlcp')
        ipcommand = manager.get('module.dockerplugin.ipcommand', 'ip')
        ovscommand = manager.get('module.dockerplugin.ovscommand', 'ovs-vsctl')
        find_invalid_ovs = _find_invalid_ovs % (shell_quote(ovscommand), shell_quote(vethprefix))
        find_unused_veth = _find_unused_veth % (shell_quote(ipcommand), shell_quote(vethprefix))
        print("docker API endpoint: ", host)
        print("ovsbridge: ", ovsbridge)
        print("vethprefix: ", vethprefix)
        
        async def invalid_ovs_ports():
            result = await execute_bash(find_invalid_ovs)
            first_invalid_ovs_list = result.splitlines(False)
            first_invalid_ovs_list = [k.strip() for k in first_invalid_ovs_list if k.strip()]
            if first_invalid_ovs_list:
                print("Detect %d invalid ports from OpenvSwitch, wait 5 seconds to detect again..." % (len(first_invalid_ovs_list),))
            else:
                return []
            await self.apiroutine.wait_with_timeout(5)
            result = await execute_bash(find_invalid_ovs)
            second_invalid_ovs_list = result.splitlines(False)
            second_invalid_ovs_list = [k.strip() for k in second_invalid_ovs_list if k.strip()]
            invalid_ports = list(set(first_invalid_ovs_list).intersection(second_invalid_ovs_list))
            if invalid_ports:
                print('Detect %d invalid ports from intersection of two tries, removing...' % (len(invalid_ports),))
                # Remove these ports
                def _remove_ports():
                    for p in invalid_ports:
                        try:
                            _unplug_ovs(ovscommand, ovsbridge, p[:-len('-tag')])
                        except Exception as exc:
                            print('Remove port %r failed: %s' % (p, exc))
                await pool.run_task(self.apiroutine, _remove_ports)
            return invalid_ports
        
        async def remove_unused_ports():
            result = await execute_bash(find_unused_veth)
            first_unused_ports = result.splitlines(False)
            first_unused_ports = [k.strip() for k in first_unused_ports if k.strip()]
            if first_unused_ports:
                print("Detect %d unused ports from ip-link, wait 5 seconds to detect again..." % (len(first_unused_ports),))
            else:
                return []
            await self.apiroutine.wait_with_timeout(5)
            result = await execute_bash(find_unused_veth)
            second_unused_ports = result.splitlines(False)
            second_unused_ports = [k.strip() for k in second_unused_ports if k.strip()]
            unused_ports = list(set(first_unused_ports).intersection(second_unused_ports))
            if unused_ports:
                print('Detect %d unused ports from intersection of two tries, removing...' % (len(unused_ports),))
                # Remove these ports
                def _remove_ports():
                    for p in unused_ports:
                        try:
                            _unplug_ovs(ovscommand, ovsbridge, p[:-len('-tag')])
                        except Exception as exc:
                            print('Remove port %r from OpenvSwitch failed: %s' % (p, exc))                    
                        try:
                            _delete_veth(ipcommand, p[:-len('-tag')])
                        except Exception as exc:
                            print('Delete port %r with ip-link failed: %s' % (p, exc))
                await pool.run_task(self.apiroutine, _remove_ports)
            return unused_ports
        
        async def detect_unused_logports():
            # docker network ls
            print("Check logical ports from docker API...")
            result = await call_docker_api(br'/v1.24/networks?filters={"driver":["vlcp"]}')
            network_ports = dict((n['Id'], dict((p['EndpointID'], p['IPv4Address'])
                                               for p in n['Containers'].values()))
                            for n in result
                            if n['Driver'] == 'vlcp')  # Old version of docker API does not support filter by driver
            print("Find %d networks and %d endpoints from docker API, recheck in 5 seconds..." % \
                    (len(network_ports), sum(len(ports) for ports in network_ports.values())))
            async def recheck_ports():
                await self.apiroutine.wait_with_timeout(5)
                # docker network inspect, use this for cross check
                result = await call_docker_api(br'/v1.24/networks?filters={"driver":["vlcp"]}')
                second_network_ports = dict((n['Id'], dict((p['EndpointID'], p['IPv4Address'])
                                                   for p in n['Containers'].values()))
                                            for n in result
                                            if n['Id'] in network_ports and n['Driver'] == 'vlcp')
                for nid in network_ports:
                    if nid not in second_network_ports:
                        print('WARNING: network {} may be removed.'.format(nid))
                        second_network_ports[nid] = {}
                print("Recheck find %d endpoints from docker API" % \
                      (sum(len(ports) for ports in second_network_ports.values()),))
                return second_network_ports
            async def check_viperflow():
                first_vp_ports = {}
                for nid in network_ports:
                    result = await call_api(self.apiroutine, 'viperflow', 'listlogicalports',
                                            {'logicalnetwork': 'docker-' + nid + '-lognet'})
                    first_vp_ports[nid] = dict((p['id'], p.get('ip_address'))
                                                    for p in result
                                                    if p['id'].startswith('docker-'))
                print("Find %d endpoints from viperflow database, recheck in 5 seconds..." % \
                        (sum(len(ports) for ports in first_vp_ports.values()),))
                await self.apiroutine.wait_with_timeout(5)
                second_vp_ports = {}
                for nid in network_ports:
                    result = await call_api(self.apiroutine, 'viperflow', 'listlogicalports',
                                            {'logicalnetwork': 'docker-' + nid + '-lognet'})
                    second_vp_ports[nid] = dict((p['id'], p.get('ip_address'))
                                                    for p in result
                                                    if p['id'] in first_vp_ports[nid])
                print("Find %d endpoints from viperflow database from the intersection of two tries" % \
                        (sum(len(ports) for ports in second_vp_ports.values()),))
                second_vp_ports = dict((nid, dict((pid[len('docker-'):], addr)
                                                  for pid, addr in v.items()))
                                       for nid, v in second_vp_ports.items())
                return second_vp_ports
            second_vp_ports = await check_viperflow()
            second_ports = await recheck_ports()
            unused_logports = dict((nid, dict((pid, addr)
                                          for pid, addr in v.items()
                                          if pid not in network_ports[nid] and\
                                             pid not in second_ports[nid]))
                                for nid, v in second_vp_ports.items())
            return unused_logports
        
        routines = []
        if not skipovs:
            routines.append(invalid_ovs_ports())
        if not skipiplink:
            routines.append(remove_unused_ports())
        if not skiplogicalport:
            routines.append(detect_unused_logports())
        execute_result = await self.apiroutine.execute_all(routines)
        if skiplogicalport:
            return
        unused_logports = execute_result[-1]
        if any(ports for ports in unused_logports.values()):
            print("Find %d unused logical ports, first 20 ips:\n%r" % \
                  (sum(len(ports) for ports in unused_logports.values()),
                   [v for _,v in \
                        itertools.takewhile(lambda x: x[0] <= 20,
                            enumerate(addr for ports in unused_logports.values()
                                for addr in ports.values()))]))
            print("Will remove them in 5 seconds, press Ctrl+C to cancel...")
            await self.apiroutine.wait_with_timeout(5)
            for ports in unused_logports.values():
                for p, addr in ports.items():
                    try:
                        await call_api(self.apiroutine, 'viperflow', 'deletelogicalport',
                                         {'id': 'docker-' + p})
                    except Exception as exc:
                        print("WARNING: remove logical port %r (IP: %s) failed, maybe it is already removed. Message: %s" % \
                                (p, addr, exc))
        print("Done.")

if __name__ == '__main__':
    Cleanup.main()

