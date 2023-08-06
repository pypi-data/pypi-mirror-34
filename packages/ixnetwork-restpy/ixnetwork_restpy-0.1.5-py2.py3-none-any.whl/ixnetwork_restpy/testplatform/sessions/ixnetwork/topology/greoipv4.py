from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Greoipv4(Base):
	"""GRE IPv4 protocol.
	"""

	_SDM_NAME = 'greoipv4'

	def __init__(self, parent):
		super(Greoipv4, self).__init__(parent)

	def CfmBridge(self, Active=None, BridgeId=None, Count=None, DescriptiveName=None, EnableOutOfSequenceCcmDetection=None, EncapsulationType=None, EtherType=None, GarbageCollectionTime=None, Multiplier=None, Name=None, OperationMode=None, Status=None):
		"""Gets child instances of CfmBridge from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of CfmBridge will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BridgeId (obj(ixnetwork_restpy.multivalue.Multivalue)): Bridge ID
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableOutOfSequenceCcmDetection (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Out of Sequence CCM Detection
			EncapsulationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Encapsulation
			EtherType (obj(ixnetwork_restpy.multivalue.Multivalue)): Ether Type
			GarbageCollectionTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Garbage Collection Time (sec)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Operation Mode
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge.CfmBridge))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge import CfmBridge
		return self._select(CfmBridge(self), locals())

	def add_CfmBridge(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of CfmBridge on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge.CfmBridge)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmbridge import CfmBridge
		return self._create(CfmBridge(self), locals())

	def Connector(self, ConnectedTo=None, Count=None, PropagateMultiplier=None):
		"""Gets child instances of Connector from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Connector will be returned.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			PropagateMultiplier (bool): The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._select(Connector(self), locals())

	def add_Connector(self, ConnectedTo=None):
		"""Adds a child instance of Connector on the server.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._create(Connector(self), locals())

	def Dhcpv4client(self, Count=None, DescriptiveName=None, Dhcp4Broadcast=None, Dhcp4GatewayAddress=None, Dhcp4GatewayMac=None, Dhcp4ServerAddress=None, Dhcp4UseFirstServer=None, Multiplier=None, Name=None, RenewTimer=None, Status=None, UseRapidCommit=None):
		"""Gets child instances of Dhcpv4client from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv4client will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Dhcp4Broadcast (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, ask the server or relay agent to use the broadcast IP address in the replies.
			Dhcp4GatewayAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the Manual Gateway IP Address for the DHCPv4 Client.
			Dhcp4GatewayMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the Manual Gateway MAC corresponding to the configured Manual Gateway IP of the DHCPv4 Client session.
			Dhcp4ServerAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The address of the DHCP server from which the subnet will accept IP addresses.
			Dhcp4UseFirstServer (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, the subnet accepts the IP addresses offered by the first server to respond with an offer of IP addresses.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RenewTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): The used-defined lease renewal timer. The value is estimated in seconds and will override the lease renewal timer if it is not zero and is smaller than server-defined value.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UseRapidCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables DHCP clients to negotiate leases with rapid commit.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client.Dhcpv4client))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client import Dhcpv4client
		return self._select(Dhcpv4client(self), locals())

	def add_Dhcpv4client(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Dhcpv4client on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client.Dhcpv4client)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4client import Dhcpv4client
		return self._create(Dhcpv4client(self), locals())

	def Dhcpv6client(self, Count=None, CustomLinkLocalAddress=None, DescriptiveName=None, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6GatewayAddress=None, Dhcp6GatewayMac=None, Dhcp6IANACount=None, Dhcp6IAPDCount=None, Dhcp6IaId=None, Dhcp6IaIdInc=None, Dhcp6IaT1=None, Dhcp6IaT2=None, Dhcp6IaType=None, Dhcp6UsePDGlobalAddress=None, EnableStateless=None, MaxNoPerClient=None, Multiplier=None, Name=None, RenewTimer=None, Status=None, UseCustomLinkLocalAddress=None, UseRapidCommit=None):
		"""Gets child instances of Dhcpv6client from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv6client will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CustomLinkLocalAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the Manual Link-Local IPv6 Address for the DHCPv6 Client.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Dhcp6DuidEnterpriseId (obj(ixnetwork_restpy.multivalue.Multivalue)): The enterprise-number is the vendor's registered Private Enterprise Number as maintained by IANA.
			Dhcp6DuidType (obj(ixnetwork_restpy.multivalue.Multivalue)): DHCP Unique Identifier Type.
			Dhcp6DuidVendorId (obj(ixnetwork_restpy.multivalue.Multivalue)): The vendor-assigned unique ID for this range. This ID is incremented automaticaly for each DHCP client.
			Dhcp6GatewayAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the Manual Gateway IPv6 Address for the DHCPv6 Client.
			Dhcp6GatewayMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the Manual Gateway MAC corresponding to the configured Manual Gateway IP of the DHCPv6 Client session.
			Dhcp6IANACount (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of IANA options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.
			Dhcp6IAPDCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of IAPD options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.
			Dhcp6IaId (obj(ixnetwork_restpy.multivalue.Multivalue)): The identity association unique ID for this range.
			Dhcp6IaIdInc (obj(ixnetwork_restpy.multivalue.Multivalue)): Increment step for each IAID in a multiple IANA/IAPD case.
			Dhcp6IaT1 (obj(ixnetwork_restpy.multivalue.Multivalue)): The suggested time at which the client contacts the server from which the addresses were obtained to extend the lifetimes of the addresses assigned.
			Dhcp6IaT2 (obj(ixnetwork_restpy.multivalue.Multivalue)): The suggested time at which the client contacts any available server to extend the lifetimes of the addresses assigned.
			Dhcp6IaType (obj(ixnetwork_restpy.multivalue.Multivalue)): Identity Association Type.
			Dhcp6UsePDGlobalAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Use DHCPc6-PD global addressing.
			EnableStateless (bool): Enables DHCP stateless.
			MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RenewTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): The used-defined lease renewal timer. The value is estimated in seconds and will override the lease renewal timer if it is not zero and is smaller than server-defined value.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UseCustomLinkLocalAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables users to manually set non-EUI link local addresses
			UseRapidCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables DHCP clients to negotiate leases with rapid commit.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client.Dhcpv6client))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client import Dhcpv6client
		return self._select(Dhcpv6client(self), locals())

	def add_Dhcpv6client(self, ConnectedVia=None, EnableStateless="False", MaxNoPerClient="1", Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Dhcpv6client on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableStateless (bool): Enables DHCP stateless.
			MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client.Dhcpv6client)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6client import Dhcpv6client
		return self._create(Dhcpv6client(self), locals())

	def Ethernet(self, Count=None, DescriptiveName=None, EnableVlans=None, Mac=None, Mtu=None, Multiplier=None, Name=None, NotifyMACMove=None, Status=None, UseVlans=None, VlanCount=None):
		"""Gets child instances of Ethernet from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ethernet will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableVlans (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables VLANs for the sessions.
			Mac (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC addresses of the devices
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum transmission unit
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NotifyMACMove (bool): Flag to determine if MAC move notification to be sent
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
		return self._select(Ethernet(self), locals())

	def add_Ethernet(self, ConnectedVia=None, Multiplier="1", Name=None, NotifyMACMove="False", StackedLayers=None, UseVlans="False", VlanCount="1"):
		"""Adds a child instance of Ethernet on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NotifyMACMove (bool): Flag to determine if MAC move notification to be sent
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
		return self._create(Ethernet(self), locals())

	def Ipv4(self, Address=None, Count=None, DescriptiveName=None, GatewayIp=None, ManualGatewayMac=None, Multiplier=None, Name=None, Prefix=None, ResolveGateway=None, Status=None):
		"""Gets child instances of Ipv4 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv4 will be returned.

		Args:
			Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 addresses of the devices
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			GatewayIp (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 addresses of the Gateways for the devices
			ManualGatewayMac (obj(ixnetwork_restpy.multivalue.Multivalue)): User specified Gateway MAC addresses
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
			ResolveGateway (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables the gateway MAC address discovery.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4.Ipv4))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4 import Ipv4
		return self._select(Ipv4(self), locals())

	def add_Ipv4(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ipv4 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4.Ipv4)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4 import Ipv4
		return self._create(Ipv4(self), locals())

	def Ipv6(self, Address=None, Count=None, DescriptiveName=None, GatewayIp=None, ManualGatewayMac=None, Multiplier=None, Name=None, Prefix=None, ResolveGateway=None, Status=None):
		"""Gets child instances of Ipv6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv6 will be returned.

		Args:
			Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 addresses of the devices
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			GatewayIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Gateways of the layer
			ManualGatewayMac (obj(ixnetwork_restpy.multivalue.Multivalue)): User specified Gateway MAC addresses
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
			ResolveGateway (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables the gateway MAC address discovery.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6.Ipv6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6 import Ipv6
		return self._select(Ipv6(self), locals())

	def add_Ipv6(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ipv6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6.Ipv6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6 import Ipv6
		return self._create(Ipv6(self), locals())

	def Ipv6Autoconfiguration(self, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of Ipv6Autoconfiguration from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv6Autoconfiguration will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration.Ipv6Autoconfiguration))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration import Ipv6Autoconfiguration
		return self._select(Ipv6Autoconfiguration(self), locals())

	def add_Ipv6Autoconfiguration(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ipv6Autoconfiguration on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration.Ipv6Autoconfiguration)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6autoconfiguration import Ipv6Autoconfiguration
		return self._create(Ipv6Autoconfiguration(self), locals())

	def IsisDceSimRouter(self, Active=None, BroadcastRootPriority=None, Count=None, DceMCastIpv4GroupCount=None, DceMCastIpv6GroupCount=None, DceMCastMacGroupCount=None, DescriptiveName=None, Multiplier=None, Name=None, Nickname=None, Status=None, SystemId=None):
		"""Gets child instances of IsisDceSimRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisDceSimRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BroadcastRootPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Broadcast Root Priority
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DceMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			DceMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			DceMCastMacGroupCount (number): MAC Group Count(multiplier)
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Nickname (obj(ixnetwork_restpy.multivalue.Multivalue)): Switch Id
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): System Id

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter.IsisDceSimRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter import IsisDceSimRouter
		return self._select(IsisDceSimRouter(self), locals())

	def add_IsisDceSimRouter(self, ConnectedVia=None, DceMCastIpv4GroupCount="0", DceMCastIpv6GroupCount="0", DceMCastMacGroupCount="0", Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisDceSimRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			DceMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			DceMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			DceMCastMacGroupCount (number): MAC Group Count(multiplier)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter.IsisDceSimRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcesimrouter import IsisDceSimRouter
		return self._create(IsisDceSimRouter(self), locals())

	def IsisFabricPath(self, Active=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, Count=None, DescriptiveName=None, Enable3WayHandshake=None, EnableConfiguredHoldTime=None, ExtendedLocalCircuitId=None, InterfaceMetric=None, Level1DeadInterval=None, Level1HelloInterval=None, LevelType=None, Multiplier=None, Name=None, NetworkType=None, Status=None):
		"""Gets child instances of IsisFabricPath from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisFabricPath will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			AutoAdjustArea (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Area
			AutoAdjustMTU (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust MTU
			AutoAdjustSupportedProtocols (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Supported Protocols
			CircuitTranmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Circuit Transmit Password / MD5-Key
			ConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Configured Hold Time
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enable3WayHandshake (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 3-way Handshake
			EnableConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Configured Hold Time
			ExtendedLocalCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Local Circuit Id
			InterfaceMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface Metric
			Level1DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Dead Interval (sec)
			Level1HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Hello Interval (sec)
			LevelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Level Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath.IsisFabricPath))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath import IsisFabricPath
		return self._select(IsisFabricPath(self), locals())

	def add_IsisFabricPath(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisFabricPath on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath.IsisFabricPath)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpath import IsisFabricPath
		return self._create(IsisFabricPath(self), locals())

	def IsisL3(self, Active=None, AdjSID=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, BFlag=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, Count=None, DedicatedOnePlusOne=None, DedicatedOneToOne=None, DescriptiveName=None, Enable3WayHandshake=None, EnableAdjSID=None, EnableBfdRegistration=None, EnableConfiguredHoldTime=None, EnableIPv6SID=None, EnableLinkProtection=None, EnableSRLG=None, Enhanced=None, ExtendedLocalCircuitId=None, ExtraTraffic=None, FFlag=None, Funcflags=None, Function=None, InterfaceMetric=None, Ipv6MTMetric=None, Ipv6SidValue=None, LFlag=None, Level1DeadInterval=None, Level1HelloInterval=None, Level1Priority=None, Level2DeadInterval=None, Level2HelloInterval=None, Level2Priority=None, LevelType=None, Multiplier=None, Name=None, NetworkType=None, OverrideFFlag=None, PFlag=None, Reserved0x40=None, Reserved0x80=None, SFlag=None, Shared=None, SrlgCount=None, Srv6SidFlags=None, Status=None, SuppressHello=None, Unprotected=None, VFlag=None, Weight=None):
		"""Gets child instances of IsisL3 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): AdjSID
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			AutoAdjustArea (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Area
			AutoAdjustMTU (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust MTU
			AutoAdjustSupportedProtocols (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Supported Protocols
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Backup Flag, if set, the Adj-SID is eligible for protection
			CircuitTranmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Circuit Transmit Password / MD5-Key
			ConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Configured Hold Time
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DedicatedOnePlusOne (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
			DedicatedOneToOne (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enable3WayHandshake (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 3-way Handshake
			EnableAdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Adj SID
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Configured Hold Time
			EnableIPv6SID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6 SID
			EnableLinkProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the link protection on the ISIS link between two mentioned interfaces.
			EnableSRLG (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the SRLG on the ISIS link between two mentioned interfaces.
			Enhanced (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
			ExtendedLocalCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Local Circuit Id
			ExtraTraffic (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
			FFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation
			Funcflags (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the function flags
			Function (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies endpoint function codes
			InterfaceMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface Metric
			Ipv6MTMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 MT Metric
			Ipv6SidValue (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Adj SID
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Flag, if set, then the value/index carried by the Adj-SID has local significance
			Level1DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Dead Interval (sec)
			Level1HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Hello Interval (sec)
			Level1Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Priority
			Level2DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 2 Dead Interval (sec)
			Level2HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 2 Hello Interval (sec)
			Level2Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 2 Priority
			LevelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Level Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			OverrideFFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.
			PFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.
			Reserved0x40 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x40.
			Reserved0x80 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x80.
			SFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies
			Shared (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			Srv6SidFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies the value of the SRv6 SID Flags
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SuppressHello (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello suppression
			Unprotected (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value Flag, if set, the Adjacency SID carries a value
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3.IsisL3))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3 import IsisL3
		return self._select(IsisL3(self), locals())

	def add_IsisL3(self, ConnectedVia=None, Multiplier="1", Name=None, SrlgCount="1", StackedLayers=None):
		"""Adds a child instance of IsisL3 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3.IsisL3)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3 import IsisL3
		return self._create(IsisL3(self), locals())

	def IsisSpbBcb(self, Active=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, Count=None, DeadInterval=None, DescriptiveName=None, Enable3WayHandshake=None, EnableConfiguredHoldTime=None, ExtendedLocalCircuitId=None, HelloInterval=None, InterfaceMetric=None, LevelType=None, Multiplier=None, Name=None, NetworkType=None, Status=None):
		"""Gets child instances of IsisSpbBcb from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbBcb will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			AutoAdjustArea (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Area
			AutoAdjustMTU (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust MTU
			AutoAdjustSupportedProtocols (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Supported Protocols
			CircuitTranmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Circuit Transmit Password / MD5-Key
			ConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Configured Hold Time
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Dead Interval (sec)
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enable3WayHandshake (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 3-way Handshake
			EnableConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Configured Hold Time
			ExtendedLocalCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Local Circuit Id
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Interval (sec)
			InterfaceMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface Metric
			LevelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Level Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb.IsisSpbBcb))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb import IsisSpbBcb
		return self._select(IsisSpbBcb(self), locals())

	def add_IsisSpbBcb(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisSpbBcb on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb.IsisSpbBcb)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbcb import IsisSpbBcb
		return self._create(IsisSpbBcb(self), locals())

	def IsisSpbBeb(self, Active=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, Count=None, DeadInterval=None, DescriptiveName=None, Enable3WayHandshake=None, EnableConfiguredHoldTime=None, ExtendedLocalCircuitId=None, HelloInterval=None, InterfaceMetric=None, LevelType=None, Multiplier=None, Name=None, NetworkType=None, Status=None):
		"""Gets child instances of IsisSpbBeb from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbBeb will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			AutoAdjustArea (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Area
			AutoAdjustMTU (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust MTU
			AutoAdjustSupportedProtocols (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Supported Protocols
			CircuitTranmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Circuit Transmit Password / MD5-Key
			ConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Configured Hold Time
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Dead Interval (sec)
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enable3WayHandshake (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 3-way Handshake
			EnableConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Configured Hold Time
			ExtendedLocalCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Local Circuit Id
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Interval (sec)
			InterfaceMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface Metric
			LevelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Level Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb.IsisSpbBeb))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb import IsisSpbBeb
		return self._select(IsisSpbBeb(self), locals())

	def add_IsisSpbBeb(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisSpbBeb on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb.IsisSpbBeb)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbbeb import IsisSpbBeb
		return self._create(IsisSpbBeb(self), locals())

	def IsisSpbSimRouter(self, Active=None, BridgePriority=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, SpSourceId=None, SpbTopologyCount=None, Status=None, SystemId=None):
		"""Gets child instances of IsisSpbSimRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbSimRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BridgePriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Bridge Priority
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SpSourceId (obj(ixnetwork_restpy.multivalue.Multivalue)): SP Source Id
			SpbTopologyCount (number): Topology Count
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): System Id

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter.IsisSpbSimRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter import IsisSpbSimRouter
		return self._select(IsisSpbSimRouter(self), locals())

	def add_IsisSpbSimRouter(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisSpbSimRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter.IsisSpbSimRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbsimrouter import IsisSpbSimRouter
		return self._create(IsisSpbSimRouter(self), locals())

	def IsisTrill(self, Active=None, AuthType=None, AutoAdjustArea=None, AutoAdjustMTU=None, AutoAdjustSupportedProtocols=None, CircuitTranmitPasswordOrMD5Key=None, ConfiguredHoldTime=None, Count=None, DescriptiveName=None, Enable3WayHandshake=None, EnableConfiguredHoldTime=None, ExtendedLocalCircuitId=None, InterfaceMetric=None, Level1DeadInterval=None, Level1HelloInterval=None, Level1Priority=None, LevelType=None, Multiplier=None, Name=None, NetworkType=None, Status=None):
		"""Gets child instances of IsisTrill from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrill will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			AutoAdjustArea (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Area
			AutoAdjustMTU (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust MTU
			AutoAdjustSupportedProtocols (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Adjust Supported Protocols
			CircuitTranmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Circuit Transmit Password / MD5-Key
			ConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Configured Hold Time
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enable3WayHandshake (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 3-way Handshake
			EnableConfiguredHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Configured Hold Time
			ExtendedLocalCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Local Circuit Id
			InterfaceMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface Metric
			Level1DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Dead Interval (sec)
			Level1HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Hello Interval (sec)
			Level1Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): Level 1 Priority
			LevelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Level Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill.IsisTrill))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill import IsisTrill
		return self._select(IsisTrill(self), locals())

	def add_IsisTrill(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IsisTrill on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill.IsisTrill)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrill import IsisTrill
		return self._create(IsisTrill(self), locals())

	def IsisTrillSimRouter(self, Active=None, BroadcastRootPriority=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Nickname=None, Status=None, SystemId=None, TrillMCastIpv4GroupCount=None, TrillMCastIpv6GroupCount=None, TrillMCastMacGroupCount=None):
		"""Gets child instances of IsisTrillSimRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrillSimRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BroadcastRootPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Broadcast Root Priority
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Nickname (obj(ixnetwork_restpy.multivalue.Multivalue)): Nickname
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): System Id
			TrillMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			TrillMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			TrillMCastMacGroupCount (number): MAC Group Count(multiplier)

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter.IsisTrillSimRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter import IsisTrillSimRouter
		return self._select(IsisTrillSimRouter(self), locals())

	def add_IsisTrillSimRouter(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None, TrillMCastIpv4GroupCount="0", TrillMCastIpv6GroupCount="0", TrillMCastMacGroupCount="0"):
		"""Adds a child instance of IsisTrillSimRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TrillMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			TrillMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			TrillMCastMacGroupCount (number): MAC Group Count(multiplier)

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter.IsisTrillSimRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillsimrouter import IsisTrillSimRouter
		return self._create(IsisTrillSimRouter(self), locals())

	def Lacp(self, Active=None, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, CollectingFlag=None, CollectorsMaxdelay=None, Count=None, DescriptiveName=None, DistributingFlag=None, InterMarkerPDUDelay=None, InterMarkerPDUDelayRandomMax=None, InterMarkerPDUDelayRandomMin=None, LacpActivity=None, LacpduPeriodicTimeInterval=None, LacpduTimeout=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, Multiplier=None, Name=None, PeriodicSendingOfMarkerRequest=None, SendMarkerRequestOnLagChange=None, Status=None, SupportRespondingToMarker=None, SynchronizationFlag=None):
		"""Gets child instances of Lacp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Lacp will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ActorKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Key
			ActorPortNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Number
			ActorPortPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Priority
			ActorSystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Id
			ActorSystemPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Priority
			AdministrativeKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Administrative Key
			AggregationFlagState (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregation Flag State
			CollectingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Collecting Flag
			CollectorsMaxdelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Collectors Maximum Delay
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistributingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Distributing Flag
			InterMarkerPDUDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay (sec)
			InterMarkerPDUDelayRandomMax (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Max (sec)
			InterMarkerPDUDelayRandomMin (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Min (sec)
			LacpActivity (obj(ixnetwork_restpy.multivalue.Multivalue)): LACP Actvity
			LacpduPeriodicTimeInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Periodic Time Interval
			LacpduTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Timeout
			MarkerRequestMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Request Mode
			MarkerResponseWaitTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Response Wait Time (sec)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeriodicSendingOfMarkerRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): Periodic Sending Of Marker Request
			SendMarkerRequestOnLagChange (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Marker Request On Lag Change
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportRespondingToMarker (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Responding To Marker
			SynchronizationFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Synchronization Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp.Lacp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp import Lacp
		return self._select(Lacp(self), locals())

	def add_Lacp(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Lacp on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp.Lacp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lacp import Lacp
		return self._create(Lacp(self), locals())

	def MsrpListener(self, Active=None, AdvertiseAs=None, Count=None, DeclareUnsolicitedVlan=None, DescriptiveName=None, JoinTimer=None, LeaveAllTimer=None, LeaveTimer=None, ListenerDomainCount=None, Multiplier=None, Name=None, ProtocolVersion=None, StartVlanId=None, Status=None, SubscribeAll=None, SubscribedStreamCount=None, VlanCount=None):
		"""Gets child instances of MsrpListener from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MsrpListener will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Attribute Advertise As Type
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeclareUnsolicitedVlan (bool): Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			JoinTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Join Timer in miliseconds
			LeaveAllTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Leave All timer in milisecond
			LeaveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Leave Timer in milisecond
			ListenerDomainCount (number): Domain Count
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ProtocolVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP protocol version
			StartVlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): Start VLAN ID of VLAN range
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SubscribeAll (bool): Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
			SubscribedStreamCount (number): Count of streams Listener want to listen
			VlanCount (obj(ixnetwork_restpy.multivalue.Multivalue)): VLAN count of VLAN range

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener.MsrpListener))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener import MsrpListener
		return self._select(MsrpListener(self), locals())

	def add_MsrpListener(self, ConnectedVia=None, DeclareUnsolicitedVlan="False", ListenerDomainCount="1", Multiplier="1", Name=None, StackedLayers=None, SubscribeAll="True", SubscribedStreamCount="1"):
		"""Adds a child instance of MsrpListener on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			DeclareUnsolicitedVlan (bool): Declare VLAN membership of configured VLAN range using MVRP even before learning any streams
			ListenerDomainCount (number): Domain Count
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			SubscribeAll (bool): Send MSRP Listener Ready for all streams advertised in recieved MSRP Talker Advertise
			SubscribedStreamCount (number): Count of streams Listener want to listen

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener.MsrpListener)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrplistener import MsrpListener
		return self._create(MsrpListener(self), locals())

	def MsrpTalker(self, Active=None, AdvertiseAs=None, AdvertiseVlanMembership=None, Count=None, DescriptiveName=None, JoinTimer=None, LeaveAllTimer=None, LeaveTimer=None, Multiplier=None, Name=None, ProtocolVersion=None, Status=None, StreamCount=None, TalkerDomainCount=None):
		"""Gets child instances of MsrpTalker from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MsrpTalker will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Attribute Advertise As Type
			AdvertiseVlanMembership (bool): Advertise VLAN Membership from these talkers
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			JoinTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Join Timer in miliseconds
			LeaveAllTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Leave All timer in milisecond
			LeaveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP Leave Timer in milisecond
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ProtocolVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): MRP protocol version
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			StreamCount (number): number of stream id instances per talker instance (multiplier)
			TalkerDomainCount (number): Domain Count

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker.MsrpTalker))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker import MsrpTalker
		return self._select(MsrpTalker(self), locals())

	def add_MsrpTalker(self, AdvertiseVlanMembership="True", ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None, StreamCount="1", TalkerDomainCount="1"):
		"""Adds a child instance of MsrpTalker on the server.

		Args:
			AdvertiseVlanMembership (bool): Advertise VLAN Membership from these talkers
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StreamCount (number): number of stream id instances per talker instance (multiplier)
			TalkerDomainCount (number): Domain Count

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker.MsrpTalker)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.msrptalker import MsrpTalker
		return self._create(MsrpTalker(self), locals())

	def Nglacp(self, Active=None, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, CollectingFlag=None, CollectorsMaxdelay=None, Count=None, DescriptiveName=None, DistributingFlag=None, InterMarkerPDUDelay=None, InterMarkerPDUDelayRandomMax=None, InterMarkerPDUDelayRandomMin=None, LacpActivity=None, LacpduPeriodicTimeInterval=None, LacpduTimeout=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, Multiplier=None, Name=None, PeriodicSendingOfMarkerRequest=None, SendMarkerRequestOnLagChange=None, Status=None, SupportRespondingToMarker=None, SynchronizationFlag=None):
		"""Gets child instances of Nglacp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Nglacp will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ActorKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Key
			ActorPortNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Number
			ActorPortPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Priority
			ActorSystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Id
			ActorSystemPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Priority
			AdministrativeKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Administrative Key
			AggregationFlagState (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregation Flag State
			CollectingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Collecting Flag
			CollectorsMaxdelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Collectors Maximum Delay
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistributingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Distributing Flag
			InterMarkerPDUDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay (sec)
			InterMarkerPDUDelayRandomMax (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Max (sec)
			InterMarkerPDUDelayRandomMin (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Min (sec)
			LacpActivity (obj(ixnetwork_restpy.multivalue.Multivalue)): LACP Actvity
			LacpduPeriodicTimeInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Periodic Time Interval
			LacpduTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Timeout
			MarkerRequestMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Request Mode
			MarkerResponseWaitTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Response Wait Time (sec)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeriodicSendingOfMarkerRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): Periodic Sending Of Marker Request
			SendMarkerRequestOnLagChange (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Marker Request On Lag Change
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportRespondingToMarker (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Responding To Marker
			SynchronizationFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Synchronization Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nglacp.Nglacp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nglacp import Nglacp
		return self._select(Nglacp(self), locals())

	def add_Nglacp(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Nglacp on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nglacp.Nglacp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nglacp import Nglacp
		return self._create(Nglacp(self), locals())

	def Ngstaticlag(self, Active=None, Count=None, DescriptiveName=None, LagId=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of Ngstaticlag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ngstaticlag will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LagId (obj(ixnetwork_restpy.multivalue.Multivalue)): LAG ID
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ngstaticlag.Ngstaticlag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ngstaticlag import Ngstaticlag
		return self._select(Ngstaticlag(self), locals())

	def add_Ngstaticlag(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ngstaticlag on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ngstaticlag.Ngstaticlag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ngstaticlag import Ngstaticlag
		return self._create(Ngstaticlag(self), locals())

	def StaticLag(self, Active=None, Count=None, DescriptiveName=None, LagId=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of StaticLag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of StaticLag will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LagId (obj(ixnetwork_restpy.multivalue.Multivalue)): LAG ID
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag.StaticLag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag import StaticLag
		return self._select(StaticLag(self), locals())

	def add_StaticLag(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of StaticLag on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag.StaticLag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticlag import StaticLag
		return self._create(StaticLag(self), locals())

	def Streams(self, Active=None, ClassMeasurementInterval=None, Count=None, DataFramePriority=None, DescriptiveName=None, DestinationMac=None, MaxFrameSize=None, MaxIntervalFrames=None, Multiplier=None, Name=None, PerFrameOverhead=None, PortTcMaxLatency=None, Rank=None, SourceMac=None, SrClass=None, Status=None, StreamId=None, StreamName=None, UniqueId=None, VlanId=None):
		"""Gets child instances of Streams from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Streams will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ClassMeasurementInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Class Measurement Interval (us)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DataFramePriority (obj(ixnetwork_restpy.multivalue.Multivalue)): data frame priority of tagged data stream
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestinationMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination MAC
			MaxFrameSize (obj(ixnetwork_restpy.multivalue.Multivalue)): maximum frame size that talker will produce
			MaxIntervalFrames (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of frames that the talker may transmit in one class measurement interval
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PerFrameOverhead (obj(ixnetwork_restpy.multivalue.Multivalue)): Per Frame Overhead (Bytes)
			PortTcMaxLatency (obj(ixnetwork_restpy.multivalue.Multivalue)): maximum latency that is introduced by talker
			Rank (obj(ixnetwork_restpy.multivalue.Multivalue)): Rank of the stream
			SourceMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Source MAC
			SrClass (obj(ixnetwork_restpy.multivalue.Multivalue)): Derived SR Class
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			StreamId (obj(ixnetwork_restpy.multivalue.Multivalue)): 64 bit stream ID after concatenation of 48 bit source MAC and 16 bit Unique ID
			StreamName (obj(ixnetwork_restpy.multivalue.Multivalue)): User friendly name for 64 bit stream ID
			UniqueId (obj(ixnetwork_restpy.multivalue.Multivalue)): 16 bit unsigned integer value to distinguish among multiple streams sourced by same talker
			VlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): VLAN ID

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams.Streams))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams import Streams
		return self._select(Streams(self), locals())

	def add_Streams(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Streams on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams.Streams)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.streams import Streams
		return self._create(Streams(self), locals())

	def Tag(self, __id__=None, Count=None, Enabled=None, Name=None):
		"""Gets child instances of Tag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Tag will be returned.

		Args:
			__id__ (obj(ixnetwork_restpy.multivalue.Multivalue)): the tag ids that this entity will use/publish
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._select(Tag(self), locals())

	def add_Tag(self, Enabled="False", Name=None):
		"""Adds a child instance of Tag on the server.

		Args:
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._create(Tag(self), locals())

	@property
	def ConnectedVia(self):
		"""List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DestIp(self):
		"""Destination IPv4 address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destIp')

	@property
	def EnableChecksum(self):
		"""Enable Checksum.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableChecksum')

	@property
	def EnableKey(self):
		"""Enable Key.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableKey')

	@property
	def EnableSequenceNumber(self):
		"""Enable Sequence Number.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableSequenceNumber')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def InKey(self):
		"""In Key.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('inKey')

	@property
	def Multiplier(self):
		"""Number of layer instances per parent instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def OutKey(self):
		"""Out Key.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('outKey')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SrcIp(self):
		"""Source IPv4 address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srcIp')

	@property
	def StackedLayers(self):
		"""List of secondary (many to one) child layer protocols

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('stackedLayers')
	@StackedLayers.setter
	def StackedLayers(self, value):
		self._set_attribute('stackedLayers', value)

	@property
	def StateCounts(self):
		"""A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

		Returns:
			dict(total:number,notStarted:number,down:number,up:number)
		"""
		return self._get_attribute('stateCounts')

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	def remove(self):
		"""Deletes a child instance of Greoipv4 on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def FetchAndUpdateConfigFromCloud(self, Mode):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		Args:
			Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('fetchAndUpdateConfigFromCloud', payload=locals(), response_object=None)

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./greoipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
