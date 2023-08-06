## VLCP docker plugin: integrate VLCP SDN network into docker engine

There is always a time when you want your docker containers directly connected to external networks
instead of using NAT from the docker node. Integrate your docker cluster with VLCP gives you full
access to a modern, professional SDN solution with little effort.

### Prepare for Installation

Using an external network plugin is supported by docker and docker swarm standalone, but not yet
in swarmkit (swarm mode in docker engine 1.12). VCLP is a global scope network so you must configure
your Docker cluster with an [external key-value store]
(https://docs.docker.com/engine/userguide/networking/#/an-overlay-network-with-an-external-key-value-store)

After configuring the cluster, there are still some preparations:
   1. Install OpenvSwitch (2.3+, 2.5, any recent versions) on every node. Start OpenvSwitch service. 
   2. Ensure Python 2.7 or Python 3.x or PyPy is installed (virtualenv is OK) on every node

VLCP currently uses Redis as the storage server (supporting other KV-storages e.g. etcd is in future plan). Install a Redis server and configure it to listen on an IP address accessable by all the other nodes. Configure Redis server with persistent
storage (RDB or/and AOF).

### Install VLCP and Docker Plugin

Install the VLCP package and vlcp-docker-plugin on all nodes with pip. Also install python-daemon to support daemonize:
```bash
pip install vlcp-docker-plugin python-daemon
```
A few optional packages are also recommended if you are using CPython. They are not needed in PyPy:
```bash
pip install vlcp_event_cython hiredis
```

In every node, copy /examples/vlcp.conf from the git repo to /etc/vlcp.conf, modify the Redis server address to IP or
domain name of your Redis server:
```
module.redisdb.url='tcp://<yourserverhere>[:<yourport>]/'
# Examples:
module.redisdb.url='tcp://10.1.9.7/'
module.redisdb.url='tcp://redis-server.mydomain.priv/'
module.redisdb.url='tcp://10.1.9.7:6379/'   # Specify port. Default to 6379 if not specified
module.redisdb.url='ssl://10.1.9.7/'    # Through a SSL proxy
```
Example configuration also bind the management API to localhost:8081, it is recommended but not
necessary on every node. Remove or comment out that line to disable the port. You should leave
at least one node to have the management API opened for creating physical network.

Create the docker plugins directory if not already created:
```bash
mkdir -p /run/docker/plugins
```
Start VLCP:
```bash
python -m vlcp.start -d
```

To start VLCP as a service, it is recommended to start with the following bash:
```bash
#!/bin/bash
start(){
mkdir -p /run/docker/plugins
rm -f /run/docker/plugins/vlcp.sock
# remove -d if using systemd
/usr/bin/python -m vlcp.start -d
}
start
```

### Configuring OpenvSwitch and Physical Network
In every node, start OpenvSwitch, create the default bridge and connect it to VLCP controller:
```bash
ovs-vsctl add-br dockerbr0
ovs-vsctl set-fail-mode dockerbr0 secure
ovs-vsctl set-controller dockerbr0 tcp:127.0.0.1
```
One or more physical networks should be created before creating networks in docker engine. Most types
of physical networks have physical ports for external connection. The physical port should be added to
OpenvSwitch in every node, but the physical network and physical port only need to be created once
with VLCP management API.

#### VLAN-tagged networks

Assume trunk0 is a trunk port connected to external switches)

For OpenvSwitch:
```bash
ovs-vsctl add-port dockerbr0 trunk0
```
For VLCP API (on any node):
```bash
curl -g 'http://localhost:8081/viperflow/createphysicalnetwork?type=vlan&vlanrange=`[[1000,1100]]`&id=vlan'
curl -g 'http://localhost:8081/viperflow/createphysicalport?physicalnetwork=vlan&name=trunk0'
```
Replace [1000,1100] to your vlan tag range ([[begin1, end1], [begin2, end2]]). 'vlan' is the physicalnetwork id,
you may replace it with any string you like, or remove the parameter and let VLCP generate an UUID for you.
For Docker integration, since usually you do not have many physical networks, it is always simplier to use
a meanful name instead of an UUID.

#### VXLAN (overlay) networks

For OpenvSwitch:
```bash
ovs-vsctl add-port dockerbr0 vxlan0 -- set interface vxlan0 type=vxlan options:local_ip=10.9.1.2 options:remote_ip=flow options:key=flow
```
Replace '10.9.1.2' to your node's IP address. Correctly configuring the endpoint IP address is the key for
VLCP overlay network, it should be different for every node, you can obtain the IP address from
an piece of bash script.

For VLCP API (on any node):
```bash
curl -g 'http://localhost:8081/viperflow/createphysicalnetwork?type=vxlan&vnirange=`[[10000,11000]]`&id=vxlan'
curl -g 'http://localhost:8081/viperflow/createphysicalport?physicalnetwork=vxlan&name=vxlan0'
```
Replace [[10000,11000]] to your vni range ([[begin1, end1], [begin2, end2]])

#### Bridge network

Assume eth0 is the port with external network that you want to bridge to. 

**WARNING: bridging the NIC your management IP address is on DISCONNECT YOUR SERVER from network. NEVER DO THAT.
Always use a separated NIC which does not break your management network.**

For OpenvSwitch:
```bash
ovs-vsctl add-port dockerbr0 eth0
```

For VLCP API (on any node):
```bash
curl -g 'http://localhost:8081/viperflow/createphysicalnetwork?type=native&id=native'
curl -g 'http://localhost:8081/viperflow/createphysicalport?physicalnetwork=native&name=eth0'
```

#### Host local network

Host local networks do not have physical port for external connection, so they are only connected in the same host. 

For VLCP API (on any node):
```bash
curl -g 'http://localhost:8081/viperflow/createphysicalnetwork?type=local&id=local'
```

### Create networks in Docker
```bash
docker network create -d vlcp --subnet 192.168.1.0/24 --ip-range 192.168.1.64/28 --gateway 192.168.1.1 --internal -o physicalnetwork=vlan vlcp_network
```
-d vlcp specify the network plugin to be VLCP. Other options are:
  + --subnet: The subnet CIDR
  + --ip-range: A CIDR which ip address can be allocated from. If not specified *subnet* is used.
  + --gateway: Default gateway for this network
  + --internal: Do not use docker default bridge network. It is necessary if you want the SDN network to provide L3 routing and external
  network access. If you want to use docker built-in NAT and PAT access, remove this option.
  + -o specify the ID of physical network you created earlier. Also, use additional -o to provide other options:
    + -o vlan=*vlantag*: For VLAN-tagged network, specify the network VLAN tag
    + -o vni=*vni*: For VXLAN overlay network, specify the VNI.
    + -o mtu=*mtu*: Specify network MTU. For VXLAN network, better set MTU to MTU of outer network - 50, i.e. if the
                    outer network MTU = 1500, you should specify -o mtu=1450 for VXLAN network.
  + 'vlcp_network': the docker network name, replace this to any name you preferred.

### Create container connecting to VLCP networks in docker
```bash
docker create --network vlcp_network --ip 192.168.1.65 ...
```
Use --network to specify vlcp_network (or any name you decided earlier). Use --ip to choose an IP address manually, if not specified,
docker chhoses an IP address automatically from the ip-range. Other parameters are the same as normal docker create.
*docker run* has the same parameters.
