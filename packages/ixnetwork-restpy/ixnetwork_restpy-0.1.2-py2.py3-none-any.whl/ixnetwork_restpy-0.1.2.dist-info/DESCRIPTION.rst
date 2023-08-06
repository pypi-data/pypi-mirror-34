# IxNetwork REST API Client
- A python client that consists of auto generated classes from low level IxNetwork meta data and custom classes.
- Custom classes are those classes that fall outside of SDM meta data
	- Multivalue class is a specialized class to ease the use of multivalues

# Custom Classes
## Connection class
Manages a connection to the following test tool infrastructure:
- Linux API Server
- IxNetwork GUI
- Connection Manager

### Class Details
- constructor:
	- Connection(ip_address, port=443)
	- submit a get sessions to find the backend information
	- backend information determines whether or not to bypass authentication
- methods:
	- auth(uid=, pwd=) -> authenticate and internally set the returned api key
	- create_session() -> create a Session instance
	- get_session(id=) -> returns a list of Session instances or if id is specified return that Session instance
- properties:
	- api_key -> instead of using the auth metod, use this property to set the x-api-key header

## Session class
- methods:
	- dump() -> print all properties, members etc
	- delete() -> delete the current session 
- properties:
	- ixnetwork -> returns the ixnetwork instance which is the root instance
		- all auto generated classes will be accessible under that instance
- operations:
	- load_config
	- save_config

## MultiValue class
- helper class used to provide additional runtime information about a property with type kMultiValue
- properties:
	- patterns -> returns a list of supported patterns
	- format -> returns information about the format accepted by the value property
	- value -> shortcut that takes a gui based string (requires documentation): 
		- '0.0.0.0'
		- 'Inc: 0.0.0.0, 0.0.0.1'
		- 'Dec: 0.0.0.0, 0.0.0.1'
		- 'Randr: 0.0.0.0, 255.255.255.255, 0.0.0.1, 1'
		- 'List: 0.0.0.0, 0.0.0.12, 0.0.0.22, 0.0.0.19'
		- 'Randb: 100.1.1.1, 0.255.255.255, 1, 4000000'
		- 'Alt: true'
	- subsets -> returns a list of possible subset candidates
	- shared -> returns a list of possible shared candidates
- methods:
	- get_values(skip=0, take=end) -> returns a list of values encapsulated by the multivalue

# Auto Generated Classes
- SDM Nodes
	- kRequired
		- accessed via a property on parent
	- kList, kOptional
		- accessed via a get_ or create_ method on a parent instance
		- get_(...) method has optional named parameters for searching for a specific instance
		- supports create_(...) method on parent with optional named parameters for all writeable properties
		- supports delete method on instance
	- kManaged
		- accessed via a get_ method on a parent instance
		- get_(...) method has optional named parameters for searching for a specific instance
- SDM Execs will be generated under an operations property
	- available on every instance
	- if SDM node supports kMultiValue allow for operations based on a session range using search
		- search string is formatted as nodeName.propertyName and regex, for example:
			- bgppeer1.start('ipv4.address: ^1.1.1') -> starts only those devices with ipv4 address that begins with 1.1.1
			- ipv41.operations.start('ethernet.mac: ^(00:00..01|02)$')???
			- start all bgppeer sessions across all dgs that match a specific criteria???
			- bgppeer1.start('asnumber: ^1')
- SDM Attributes will be generated with the following types
	- kMultivalue -> instance of MultiValue helper class
	- kArray -> list
	- kString -> str
	- kBool -> bool
	- kObjref -> href (str)
	- kStruct -> dict
	- kInteger, kInteger64 -> int
- Property Updates
	- will be cached client side
	- will be submitted to the server in one call anytime a create_ or operation is called
- Documentation
	- inline documentation will use google docstring format
	- every class, property, operation will be documented inline
	- generated markdown and html static documentation from all inline documentation

# Build, Test and Deploy
- p4 package
	- not part of an actual IxNetwork source tree
- nightly build against latest IxNetwork
- test (unit and system)
- manually deploy as a package to pypi using jenkins

# Scaffold Sample

```python
from ixnetwork_restapi import *

# setup connection parameters to be used by the http transport
connection = Connection('127.0.0.1', port=443)

# authenticate using auth method
connection.auth('admin', 'admin')

# authenticate using supplied api_key
connection.api_key = 'a7dba444ac1e4db79231442c6a605609'

# get a list of sessions
sessions = connection.session() 

# get a single session
session = connection.session(1) 

# create a session
session = connection.create_session() 

# load a configuration
session.load_config('ipv4_traffic.ixncfg', local=true)

# kRequired returns instance via a property
ixnetwork = session.ixnetwork

# kList, kManaged, kOptional return instance via a method
# method can take named parameters to allow searching via select for a specific instance
# if named parameters are supplied and there are no matches raise an error
# if named parameters are supplied and there are more than one match raise an error
# if no named parameters are supplied return all instances
topology1 = ixnetwork.get_topology(name='Topology 1')
device_group1 = topology1.create_deviceGroup(name='DG 1', enabled='Alt: True')
ethernet1 = device_group1.create_ethernet(name='Eth 1', mac='Inc: 00:00:00:00:00:01, 00:00:00:00:00:01')

# kList, kOptional will generate a create_<class name here> method on the parent object
# named parameters for all properties
vport1 = ixnetwork.create_vport(name='Ethernet 1')
vport2 = ixnetwork.create_vport(name='Ethernet 2')
vport3 = ixnetwork.create_vport(name='Ethernet 3')
topology2 = ixnetwork.create_topology(name='Topology 2', vports=[vport1, vport2])

# kList, kOptional support a delete method
vport1.delete()

# all auto generated instances support a dump method that displays all property values
vport1.dump() 

# methods with kObjref or kArray[kObjref] will be wired to accept an object instance or an href
vport1.operations.connect(ixnetwork.availableHardware.chassis(hostname='10.38.78.17').card(id=3).port(id=6)) 

# batch all updates and submit them in one operation using the connection
vport1.type = 'ethernet'
vport2.type = 'pos'
print(vport2.type) -> pos
vport2.refresh() -> commit -> get pos from server
topology2.name = 'WestBound'
topology1.name = 'EastBound'
topology1.vports = list(vport3)
ethernet1.mac.value = 'List: 00:00:00:00:00:01, 00:00:00:00:00:01'  

vport1.update(type='pos', name='abc', txgapcontrol='interleave')

ixnetwork.operations.assign_ports() 

```

# Search Sample
```python
from ixnetwork_restapi import *

connection = Connection('127.0.0.1', port=443)
connection.api_key = 'a7dba444ac1e4db79231442c6a605609'
vport1 = connection.session(id=1).ixnetwork.get_vport(name='Ethernet - 001') 

bgp_peer = connection.session(id=1).ixnetwork
	.get_topology(name='Topology 1')
	.get_deviceGroup(name='DG 1') 
	.get_ethernet(name='Eth 1')
	.get_ipv4(name='IPV4 - 1')
	.get_bgpIpv4Peer(name='BGP')

```


