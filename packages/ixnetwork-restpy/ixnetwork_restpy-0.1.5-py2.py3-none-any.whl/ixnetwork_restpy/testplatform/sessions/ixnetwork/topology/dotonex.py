from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DotOneX(Base):
	"""
	"""

	_SDM_NAME = 'dotOneX'

	def __init__(self, parent):
		super(DotOneX, self).__init__(parent)

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

	def LightweightDhcpv6relayAgent(self, Count=None, DescriptiveName=None, LightweightDhcp6RelayAgentGlobalAndPortData=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of LightweightDhcpv6relayAgent from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LightweightDhcpv6relayAgent will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LightweightDhcp6RelayAgentGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent.LightweightDhcpv6relayAgent))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent import LightweightDhcpv6relayAgent
		return self._select(LightweightDhcpv6relayAgent(self), locals())

	def add_LightweightDhcpv6relayAgent(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of LightweightDhcpv6relayAgent on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent.LightweightDhcpv6relayAgent)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lightweightdhcpv6relayagent import LightweightDhcpv6relayAgent
		return self._create(LightweightDhcpv6relayAgent(self), locals())

	def Mpls(self, Bos=None, Cos=None, Count=None, DescriptiveName=None, DestMac=None, Enablecw=None, Multiplier=None, Name=None, Overridecos=None, RxLabelValue=None, Status=None, TransportType=None, Ttl=None, TxLabelValue=None, UpperLayer=None):
		"""Gets child instances of Mpls from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Mpls will be returned.

		Args:
			Bos (obj(ixnetwork_restpy.multivalue.Multivalue)): bos
			Cos (obj(ixnetwork_restpy.multivalue.Multivalue)): EXP
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination Mac.
			Enablecw (bool): Enable Control Word
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overridecos (bool): Override Cos
			RxLabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Rx Label
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TransportType (str(overMac|overTunnel)): TransportType
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): TTL
			TxLabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Tx Label
			UpperLayer (str(nhEthernet|nhIp)): Value to Determine who is upper Layer.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls.Mpls))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls import Mpls
		return self._select(Mpls(self), locals())

	def add_Mpls(self, ConnectedVia=None, Enablecw="False", Multiplier="1", Name=None, Overridecos="False", StackedLayers=None, TransportType="overMac", UpperLayer="nhEthernet"):
		"""Adds a child instance of Mpls on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Enablecw (bool): Enable Control Word
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overridecos (bool): Override Cos
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TransportType (str(overMac|overTunnel)): TransportType
			UpperLayer (str(nhEthernet|nhIp)): Value to Determine who is upper Layer.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls.Mpls)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls import Mpls
		return self._create(Mpls(self), locals())

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

	def Pppoxclient(self, AcMatchMac=None, AcMatchName=None, AcOptions=None, ActualRateDownstream=None, ActualRateUpstream=None, AgentAccessAggregationCircuitId=None, AgentCircuitId=None, AgentRemoteId=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ChapName=None, ChapSecret=None, ClientDnsOptions=None, ClientLocalIp=None, ClientLocalIpv6Iid=None, ClientNcpOptions=None, ClientNetmask=None, ClientNetmaskOptions=None, ClientPrimaryDnsAddress=None, ClientSecondaryDnsAddress=None, ClientSignalIWF=None, ClientSignalLoopChar=None, ClientSignalLoopEncapsulation=None, ClientSignalLoopId=None, ClientV6NcpOptions=None, ClientWinsOptions=None, ClientWinsPrimaryAddress=None, ClientWinsSecondaryAddress=None, Count=None, DataLink=None, DescriptiveName=None, DomainList=None, DslTypeTlv=None, EchoReqInterval=None, EnableDomainGroups=None, EnableEchoReq=None, EnableEchoRsp=None, EnableHostUniq=None, EnableMaxPayload=None, EnableRedial=None, Encaps1=None, Encaps2=None, HostUniq=None, HostUniqLength=None, LcpAccm=None, LcpEnableAccm=None, LcpMaxFailure=None, LcpRetries=None, LcpStartDelay=None, LcpTermRetries=None, LcpTimeout=None, MaxPayload=None, MruNegotiation=None, Mtu=None, Multiplier=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, PadiRetries=None, PadiTimeout=None, PadrRetries=None, PadrTimeout=None, PapPassword=None, PapUser=None, PonTypeTlv=None, RedialMax=None, RedialTimeout=None, ServiceName=None, ServiceOptions=None, Status=None, UnlimitedRedialAttempts=None, UserDefinedDslType=None, UserDefinedPonType=None):
		"""Gets child instances of Pppoxclient from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Pppoxclient will be returned.

		Args:
			AcMatchMac (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			AcMatchName (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			AcOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates PPPoE AC retrieval mode
			ActualRateDownstream (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual downstream data rate (sub-option 0x81), in kbps.
			ActualRateUpstream (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter specifies the value to be included in the vendor specific PPPoE tag. It is the actual upstream data rate (sub-option 0x82), in kbps.
			AgentAccessAggregationCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): The value to be inserted into the Agent Access-Aggregation-Circuit-ID-ASCII-Value field of the PPPoX tag.
			AgentCircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): The value to be inserted into the Agent Circuit ID field of the PPPoX tag.
			AgentRemoteId (obj(ixnetwork_restpy.multivalue.Multivalue)): The value to be inserted into the Agent Remote ID field of the PPPoX tag.
			AuthRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of PPP authentication retries
			AuthTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for PPP authentication, in seconds.
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): The authentication type to use during link setup.
			ChapName (obj(ixnetwork_restpy.multivalue.Multivalue)): User name when CHAP Authentication is being used
			ChapSecret (obj(ixnetwork_restpy.multivalue.Multivalue)): Secret when CHAP Authentication is being used
			ClientDnsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The client DNS options.
			ClientLocalIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The requested IPv4 address.
			ClientLocalIpv6Iid (obj(ixnetwork_restpy.multivalue.Multivalue)): The requested IPv6 Interface Identifier (IID).
			ClientNcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The NCP configuration mode for IPv4 addressing.
			ClientNetmask (obj(ixnetwork_restpy.multivalue.Multivalue)): The netmask that the client will use with the assigned IP address.
			ClientNetmaskOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The client netmask option.
			ClientPrimaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the primary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary only' or 'Request Primary and Secondary'.
			ClientSecondaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the secondary DNS server address that the client requests from the server when the value of the Client DNS Options field is set to 'Request Primary and Secondary'.
			ClientSignalIWF (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADI and PADR packets.
			ClientSignalLoopChar (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADI and PADR packets.
			ClientSignalLoopEncapsulation (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADI and PADR packets.
			ClientSignalLoopId (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x01 , 0x02, 0x03 (Remote ID,Circuit ID and Access Aggregation Circuit ID) into the DSL tag in PADI and PADR packets.
			ClientV6NcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The NCP configuration mode for IPv6 addressing.
			ClientWinsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the mode in which WINS host addresses are configured.
			ClientWinsPrimaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the primary WINS address.
			ClientWinsSecondaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the secondary WINS address.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DataLink (obj(ixnetwork_restpy.multivalue.Multivalue)): A one-byte field included with sub-option 0x90.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DomainList (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure domain group settings
			DslTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): DSL Type to be advertised in PPPoE VSA Tag. For undefined DSL type user has to select User-defined DSL Type.
			EchoReqInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Keep alive interval, in seconds
			EnableDomainGroups (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable domain groups
			EnableEchoReq (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableEchoRsp (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableHostUniq (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables PPPoE Host-Uniq tag
			EnableMaxPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables PPPoE Max Payload tag
			EnableRedial (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, PPPoE redial is enabled
			Encaps1 (obj(ixnetwork_restpy.multivalue.Multivalue)): A one-byte field included with sub-option 0x90.
			Encaps2 (obj(ixnetwork_restpy.multivalue.Multivalue)): A one-byte field included with sub-option 0x90.
			HostUniq (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates Host-Uniq Tag
			HostUniqLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Host-Uniq Length, in bytes
			LcpAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Async-Control-Character-Map
			LcpEnableAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Async-Control-Character-Map
			LcpMaxFailure (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
			LcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP retries
			LcpStartDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay time in milliseconds to wait before sending LCP Config Request packet
			LcpTermRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP Termination Retries
			LcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for LCP phase, in seconds
			MaxPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): Max Payload
			MruNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MRU Negotiation
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Max Transmit Unit for PPP
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of NCP retries
			NcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for NCP phase, in seconds
			NcpType (obj(ixnetwork_restpy.multivalue.Multivalue)): IP address type (IPv4 or IPv6) for Network Control Protocol
			PadiRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of PADI Retries
			PadiTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for PADI no response, in seconds
			PadrRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of PADR Retries
			PadrTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for PADR no response, in seconds
			PapPassword (obj(ixnetwork_restpy.multivalue.Multivalue)): Password when PAP Authentication is being used
			PapUser (obj(ixnetwork_restpy.multivalue.Multivalue)): User name when PAP Authentication is being used
			PonTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): PON Type to be advertised in PPPoE VSA Tag. For undefined PON type user has to select User-defined PON Type.
			RedialMax (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of PPPoE redials
			RedialTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): PPPoE redial timeout, in seconds
			ServiceName (obj(ixnetwork_restpy.multivalue.Multivalue)): Access Concentrator Service Name - this option is only available for PPP servers.
			ServiceOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates PPPoE service retrieval mode
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UnlimitedRedialAttempts (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, PPPoE unlimited redial attempts is enabled
			UserDefinedDslType (obj(ixnetwork_restpy.multivalue.Multivalue)): User Defined DSL-Type Value.
			UserDefinedPonType (obj(ixnetwork_restpy.multivalue.Multivalue)): User Defined PON-Type Value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient.Pppoxclient))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient import Pppoxclient
		return self._select(Pppoxclient(self), locals())

	def add_Pppoxclient(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Pppoxclient on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient.Pppoxclient)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxclient import Pppoxclient
		return self._create(Pppoxclient(self), locals())

	def Pppoxserver(self, AcName=None, AcceptAnyAuthValue=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ClientBaseIID=None, ClientBaseIp=None, ClientIID=None, ClientIIDIncr=None, ClientIpIncr=None, Count=None, DescriptiveName=None, DnsServerList=None, EchoReqInterval=None, EnableDnsRa=None, EnableEchoReq=None, EnableEchoRsp=None, EnableMaxPayload=None, Ipv6AddrPrefixLen=None, Ipv6PoolPrefix=None, Ipv6PoolPrefixLen=None, LcpAccm=None, LcpEnableAccm=None, LcpMaxFailure=None, LcpRetries=None, LcpStartDelay=None, LcpTermRetries=None, LcpTimeout=None, MruNegotiation=None, Mtu=None, Multiplier=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, PppoxServerGlobalAndPortData=None, ServerBaseIID=None, ServerBaseIp=None, ServerDnsOptions=None, ServerIID=None, ServerIIDIncr=None, ServerIpIncr=None, ServerNcpOptions=None, ServerNetmask=None, ServerNetmaskOptions=None, ServerPrimaryDnsAddress=None, ServerSecondaryDnsAddress=None, ServerSignalDslTypeTlv=None, ServerSignalIWF=None, ServerSignalLoopChar=None, ServerSignalLoopEncapsulation=None, ServerSignalLoopId=None, ServerSignalPonTypeTlv=None, ServerV6NcpOptions=None, ServerWinsOptions=None, ServerWinsPrimaryAddress=None, ServerWinsSecondaryAddress=None, ServiceName=None, SessionsCount=None, Status=None):
		"""Gets child instances of Pppoxserver from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Pppoxserver will be returned.

		Args:
			AcName (obj(ixnetwork_restpy.multivalue.Multivalue)): Access Concentrator Name - this option is only available for PPP servers.
			AcceptAnyAuthValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures a PAP/CHAP authenticator to accept all offered usernames, passwords, and base domain names
			AuthRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of PPP authentication retries
			AuthTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for PPP authentication, in seconds.
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): The authentication type to use during link setup.
			ClientBaseIID (obj(ixnetwork_restpy.multivalue.Multivalue)): Obsolete - use clientIID instead.
			ClientBaseIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IP address to be used when creating PPP client addresses. This property is used as an incrementor for the 'clientIpIncr' property
			ClientIID (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IPv6CP (RFC5072) interface identifier for the PPP client. Used in conjunction with 'clientIIDIncr' as its incrementor. Valid for IPv6 only. The identifier is used in assigned global and local scope addresses created after negotiation.
			ClientIIDIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Client IPv6CP interface identifier increment, used in conjuction with the base identifier
			ClientIpIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): The incrementor for the clientBaseIp property address when multiple PPP addresses are created.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DnsServerList (obj(ixnetwork_restpy.multivalue.Multivalue)): DNS server list separacted by semicolon
			EchoReqInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Keep alive interval, in seconds
			EnableDnsRa (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable RDNSS routing advertisments
			EnableEchoReq (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableEchoRsp (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableMaxPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables PPP Max Payload tag
			Ipv6AddrPrefixLen (obj(ixnetwork_restpy.multivalue.Multivalue)): Address prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
			Ipv6PoolPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Pool prefix for the IPv6 IP pool.
			Ipv6PoolPrefixLen (obj(ixnetwork_restpy.multivalue.Multivalue)): Pool prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
			LcpAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Async-Control-Character-Map
			LcpEnableAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Async-Control-Character-Map
			LcpMaxFailure (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
			LcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP retries
			LcpStartDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay time in milliseconds to wait before sending LCP Config Request packet
			LcpTermRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP Termination Retries
			LcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for LCP phase, in seconds
			MruNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MRU Negotiation
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Max Transmit Unit for PPP
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of NCP retries
			NcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for NCP phase, in seconds
			NcpType (obj(ixnetwork_restpy.multivalue.Multivalue)): IP address type (IPv4 or IPv6) for Network Control Protocol
			PppoxServerGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			ServerBaseIID (obj(ixnetwork_restpy.multivalue.Multivalue)): Obsolete - use serverIID instead.
			ServerBaseIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IP address to be used when create PPP server addresses. This property is used in conjunction with the 'IPv4 Server IP Increment By' property.
			ServerDnsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The server DNS options.
			ServerIID (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IPv6CP (RFC5072) interface identifier for the PPP server, used in conjunction with 'serverIIDIncr' as incrementor. Valid for IPv6 only.
			ServerIIDIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Server IPv6CP interface identifier increment, used in conjuction with the base identifier
			ServerIpIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Server IP increment, used in conjuction with 'IPv4 Server IP' property
			ServerNcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the NCP configuration mode.
			ServerNetmask (obj(ixnetwork_restpy.multivalue.Multivalue)): The netmask that the server will assign to the client when the Server Netmask Options parameter is set to Supply Netmask.
			ServerNetmaskOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The server netmask option.
			ServerPrimaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The primary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
			ServerSecondaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The secondary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to Supply Primary and Secondary.
			ServerSignalDslTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): DSL-Type TLV to be inserted in PPPoE VSA Tag.
			ServerSignalIWF (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADO and PADS packets.
			ServerSignalLoopChar (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADO and PADS packets.
			ServerSignalLoopEncapsulation (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADO and PADS packets.
			ServerSignalLoopId (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x01 and 0x02 (Remote ID and Circuit ID) into the DSL tag in PADO and PADS packets.
			ServerSignalPonTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): PON-Type TLV to be inserted in PPPoE VSA Tag.
			ServerV6NcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the NCP configuration mode.
			ServerWinsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The WINS server discovery mode.
			ServerWinsPrimaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The primary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
			ServerWinsSecondaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The secondary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to Supply Primary and Secondary.
			ServiceName (obj(ixnetwork_restpy.multivalue.Multivalue)): Access Concentrator Service Name - this option is only available for PPP servers.
			SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver.Pppoxserver))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver import Pppoxserver
		return self._select(Pppoxserver(self), locals())

	def add_Pppoxserver(self, ConnectedVia=None, Multiplier="1", Name=None, SessionsCount="10", StackedLayers=None):
		"""Adds a child instance of Pppoxserver on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver.Pppoxserver)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver import Pppoxserver
		return self._create(Pppoxserver(self), locals())

	def Ptp(self, AlternateMasterFlag=None, AnnounceCurrentUtcOffsetValid=None, AnnounceDropRate=None, AnnounceFrequencyTraceable=None, AnnounceLeap59=None, AnnounceLeap61=None, AnnouncePtpTimescale=None, AnnounceReceiptTimeout=None, AnnounceTimeTraceable=None, AvnuMode=None, Bmca=None, ClockAccuracy=None, ClockClass=None, ClockIdentity=None, CommunicationMode=None, Count=None, CumulativeScaledRateOffset=None, CurrentUtcOffset=None, CustomClockId=None, DelayMechanism=None, DelayReqDropRate=None, DelayReqOffset=None, DelayReqResidenceTime=None, DelayReqSpread=None, DelayRespDropRate=None, DelayRespReceiptTimeout=None, DelayRespResidenceTime=None, DelayResponseDelay=None, DelayResponseDelayInsertionRate=None, DescriptiveName=None, Domain=None, DropMalformed=None, DropSignalReqAnnounce=None, DropSignalReqDelayResp=None, DropSignalReqSync=None, EnableNegativeTesting=None, FollowUpBadCrcRate=None, FollowUpDelay=None, FollowUpDelayInsertionRate=None, FollowUpDropRate=None, FollowUpResidenceTime=None, Frequency=None, GmTimeBaseIndicator=None, GrandmasterIdentity=None, GrantDelayRespDurationInterval=None, GrantSyncDurationInterval=None, GrantUnicastDurationInterval=None, HandleAnnounceTlv=None, HandleCancelTlv=None, LastGmPhaseChange=None, LearnPortId=None, LogAnnounceInterval=None, LogDelayReqInterval=None, LogSyncInterval=None, MasterCount=None, MasterIpAddress=None, MasterIpIncrementBy=None, MasterIpv6Address=None, MasterIpv6IncrementBy=None, MasterMacAddress=None, MasterMacIncrementBy=None, MulticastAddress=None, Multiplier=None, Name=None, NanosecondsPerSecond=None, NotSlave=None, NumberOFMsgs=None, OffsetScaledLogVariance=None, OneWay=None, PDelayFollowUpDelay=None, PDelayFollowUpDelayInsertionRate=None, PDelayFollowUpDropRate=None, PDelayFollowUpResidenceTime=None, PathTraceTLV=None, PortNumber=None, Priority1=None, Priority2=None, Profile=None, RenewalInvited=None, RequestAttempts=None, RequestHolddown=None, RequestInterval=None, ReverseSync=None, ReverseSyncIntervalPercent=None, Role=None, RxCalibration=None, ScaledLastGmFreqChange=None, SendMulticastAnnounce=None, SignalInterval=None, SignalUnicastHandling=None, SimulateBoundary=None, SimulateTransparent=None, SlaveCount=None, SlaveIpAddress=None, SlaveIpIncrementBy=None, SlaveIpv6Address=None, SlaveIpv6IncrementBy=None, SlaveMacAddress=None, SlaveMacIncrementBy=None, Status=None, StepMode=None, StepsRemoved=None, StrictGrant=None, SyncDropRate=None, SyncReceiptTimeout=None, SyncReceiptTimeoutgPTP=None, SyncResidenceTime=None, TimeSource=None, TimestampOffset=None, TxCalibration=None, TxTwoStepCalibration=None, UpdateTime=None):
		"""Gets child instances of Ptp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ptp will be returned.

		Args:
			AlternateMasterFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Select this check box to set the Alternate Master flag in all Announce and Sync messages
			AnnounceCurrentUtcOffsetValid (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce currentUtcOffsetValid bit
			AnnounceDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped Announce messages
			AnnounceFrequencyTraceable (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce frequency traceable bit
			AnnounceLeap59 (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce leap59 bit
			AnnounceLeap61 (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce leap61 bit
			AnnouncePtpTimescale (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce ptpTimescale bit
			AnnounceReceiptTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of Announce Intervals that have to pass without receipt of an Announce message to trigger timeout
			AnnounceTimeTraceable (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Announce time traceable bit
			AvnuMode (str(aVNU_GPTP|aVNU_NA)): AVNU Mode
			Bmca (obj(ixnetwork_restpy.multivalue.Multivalue)): Run the Best Master Clock Algorithm for gPTP (if disabled can use a pre-defined Master or accept messages from any source)
			ClockAccuracy (obj(ixnetwork_restpy.multivalue.Multivalue)): Clock accuracy
			ClockClass (obj(ixnetwork_restpy.multivalue.Multivalue)): Traceability of the time or frequency distributed by the grandmaster clock
			ClockIdentity (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the ClockIdentity to be used by this device
			CommunicationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Communication mode (unicast/multicast/mixed)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CumulativeScaledRateOffset (obj(ixnetwork_restpy.multivalue.Multivalue)): Cumulative Scaled Rate Offset field set in the gPTP FollowUp TLV
			CurrentUtcOffset (obj(ixnetwork_restpy.multivalue.Multivalue)): Set announced Current UTC Offset (seconds)
			CustomClockId (obj(ixnetwork_restpy.multivalue.Multivalue)): Use the ClockIdentity configured in the next column instead of MAC based generated one
			DelayMechanism (obj(ixnetwork_restpy.multivalue.Multivalue)): Clock delay mechanism
			DelayReqDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped (P)DelayReq messages
			DelayReqOffset (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage of the agreed (P)DelayReq Inter-arrival time to schedule between two subsequent DelayReq messages
			DelayReqResidenceTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Residence time of (P)DelayReq messages through an associated one-step end-to-end transparent clock inserted in the correction field of (P)DelayReq messages sent by this clock
			DelayReqSpread (obj(ixnetwork_restpy.multivalue.Multivalue)): Distribute (P)DelayReq messages in an interval around the targeted Inter-arrival mean time (expressed as a % of targeted mean)
			DelayRespDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped DelayResp messages
			DelayRespReceiptTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): DelayResponse Receipt Timeout in seconds
			DelayRespResidenceTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Residence time of DelayReq messages through an associated two-step end-to-end transparent clock inserted in the correction field of DelayResp messages sent by this clock, or the residence time of PdelayResp messages through an associated one-step end-to-end transparent clock inserted in the correction field of PdelayResp messages sent by this clock
			DelayResponseDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Additional delay introduced in the DelayResp message (nanoseconds)
			DelayResponseDelayInsertionRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the DelayResp messages in which the delay is introduced
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Domain (obj(ixnetwork_restpy.multivalue.Multivalue)): PTP Domain
			DropMalformed (obj(ixnetwork_restpy.multivalue.Multivalue)): Drop packets that for which fields like Domain, message rates, Clock Class, Clock Accuracy and Offset Scaled Log Variance are not respecting strict G8275.1 imposed intervals
			DropSignalReqAnnounce (obj(ixnetwork_restpy.multivalue.Multivalue)): Select this check box to drop any Signal Request that contains Announce TLV
			DropSignalReqDelayResp (obj(ixnetwork_restpy.multivalue.Multivalue)): Select this check box to drop any Signal Request that contains DelayResp TLV
			DropSignalReqSync (obj(ixnetwork_restpy.multivalue.Multivalue)): Select this check box to drop any Signal Request that contains Sync TLV
			EnableNegativeTesting (bool): Enable Negative Conformance Test
			FollowUpBadCrcRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the bad crc FollowUp messages
			FollowUpDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Additional delay introduced in the FollowUp message timestamp (ns)
			FollowUpDelayInsertionRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the FollowUp messages in which the delay is introduced
			FollowUpDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped FollowUp messages
			FollowUpResidenceTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Master to slave residence of Sync messages through an associated two-step transparent clock inserted in the correction field of FollowUp messages sent by this clock
			Frequency (number): Frequency(N)
			GmTimeBaseIndicator (obj(ixnetwork_restpy.multivalue.Multivalue)): GM Time Base Indicator field set in the gPTP FollowUp TLV
			GrandmasterIdentity (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the ClockIdentity of the Grandmaster behind this device
			GrantDelayRespDurationInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for DelayResp messages
			GrantSyncDurationInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV for Sync messages
			GrantUnicastDurationInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Value of DurationField in REQUEST_UNICAST_TRANSMISSION_TLV
			HandleAnnounceTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Send and respond to Announce TLV unicast requests in signal messages.
			HandleCancelTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Send and respond to Cancel TLV unicast requests in signal messages
			LastGmPhaseChange (obj(ixnetwork_restpy.multivalue.Multivalue)): Last GM Phase Change nanoseconds set in the gPTP FollowUp TLV
			LearnPortId (obj(ixnetwork_restpy.multivalue.Multivalue)): Slave learns Master Port ID
			LogAnnounceInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The log mean time interval between successive Announce messages
			LogDelayReqInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The log mean time interval between successive (P)DelayReq messages
			LogSyncInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The log mean time interval between successive Sync messages
			MasterCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The total number of Unicast masters to be used for this slave
			MasterIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this slave
			MasterIpIncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this slave
			MasterIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this slave
			MasterIpv6IncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this slave
			MasterMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this slave
			MasterMacIncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this slave
			MulticastAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The destination multicast address for G8275.1: non-forwardable (01:80:C2:00:00:0E, recommended) or forwardable (01:1B:19:00:00:00)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NanosecondsPerSecond (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of nanoseconds the emulated clock should effectively count for one second of hardware ticks
			NotSlave (obj(ixnetwork_restpy.multivalue.Multivalue)): When enabled for Master clocks it prevents a G8275.1 port from going into Slave state, by ignoring Announce messages
			NumberOFMsgs (number): Messages Count
			OffsetScaledLogVariance (obj(ixnetwork_restpy.multivalue.Multivalue)): Static Offset Scaled Log Variance of this clock
			OneWay (obj(ixnetwork_restpy.multivalue.Multivalue)): Do not send Delay Requests
			PDelayFollowUpDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Additional delay introduced in the PdelayResp FollowUp message (ns)
			PDelayFollowUpDelayInsertionRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the PdelayResp FollowUp messages in which the delay is introduced
			PDelayFollowUpDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped PdelayResp FollowUp messages
			PDelayFollowUpResidenceTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Total residence time of PdelayReq and PdelayResp messagews through an associated two-step end-to-end transparent clock inserted in the correction field of PdelayRespFollowUp messages sent by this clock
			PathTraceTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the master will append a Path Trace TLV to Announce messages
			PortNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Port number
			Priority1 (obj(ixnetwork_restpy.multivalue.Multivalue)): PTP priority1.
			Priority2 (obj(ixnetwork_restpy.multivalue.Multivalue)): PTP priority2
			Profile (obj(ixnetwork_restpy.multivalue.Multivalue)): The profile used by this clock
			RenewalInvited (obj(ixnetwork_restpy.multivalue.Multivalue)): Set the Renewal Invited flag in Grant Unicast Transmission TLV
			RequestAttempts (obj(ixnetwork_restpy.multivalue.Multivalue)): How many succesive requests a slave can request before entering into holddown
			RequestHolddown (obj(ixnetwork_restpy.multivalue.Multivalue)): Time between succesive requests if denied/timeout for Signal Request
			RequestInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time between succesive requests if denied/timeout for Signal Request
			ReverseSync (obj(ixnetwork_restpy.multivalue.Multivalue)): As a slave, periodically send Reverse Sync messages with recovered clock. As a master, calculate the Offset of the Slave reported time to master time
			ReverseSyncIntervalPercent (obj(ixnetwork_restpy.multivalue.Multivalue)): The percentage of incoming Sync interval to use for Reverse Sync interval
			Role (obj(ixnetwork_restpy.multivalue.Multivalue)): The desired role of this clock (Masters may become Slave as per BMCA)
			RxCalibration (obj(ixnetwork_restpy.multivalue.Multivalue)): The amount of time (in ns) that the Receive side timestamp needs to be offset to allow for error
			ScaledLastGmFreqChange (obj(ixnetwork_restpy.multivalue.Multivalue)): Scaled Last GM Freq Change field set in the gPTP FollowUp TLV
			SendMulticastAnnounce (obj(ixnetwork_restpy.multivalue.Multivalue)): Send multicast Announce messages
			SignalInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time between Signal Request messages, in seconds
			SignalUnicastHandling (obj(ixnetwork_restpy.multivalue.Multivalue)): Signal unicast handling
			SimulateBoundary (obj(ixnetwork_restpy.multivalue.Multivalue)): Simulate a Grandmaster port behind this clock acting as a Boundary clock
			SimulateTransparent (obj(ixnetwork_restpy.multivalue.Multivalue)): Simulate a transparent clock in front of this master clock.
			SlaveCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The total number of Unicast slaves to be used for this master.
			SlaveIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this master
			SlaveIpIncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this master
			SlaveIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this master
			SlaveIpv6IncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this master
			SlaveMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used for enumerating all the addresses for this master
			SlaveMacIncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the increment to be used for enumerating all the addresses for this master
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			StepMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Clock step mode
			StepsRemoved (obj(ixnetwork_restpy.multivalue.Multivalue)): The Steps Removed field advertised in Announce Messages, representing the number of hops between this emulated Boundary clock and the Grandmaster clock (including it). Valid values: 0 to 65,535
			StrictGrant (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the master will not grant values that are above maximum offered values
			SyncDropRate (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage rate of the dropped Sync messages
			SyncReceiptTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of seconds that have to pass without receipt of an Sync message to trigger timeout
			SyncReceiptTimeoutgPTP (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of Sync Intervals that have to pass without receipt of an Sync message to trigger timeout
			SyncResidenceTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Master to slave residence time of Sync messages through an associated one-step transparent clock inserted in the correction field of Sync messages sent by this clock
			TimeSource (obj(ixnetwork_restpy.multivalue.Multivalue)): Time source for the PTP device
			TimestampOffset (obj(ixnetwork_restpy.multivalue.Multivalue)): The initial offset added to the local clock when starting the session
			TxCalibration (obj(ixnetwork_restpy.multivalue.Multivalue)): The amount of time (in ns) that the transmit timestamp of one step messages (Sync, PdelayResp) needs to be adjusted for error
			TxTwoStepCalibration (obj(ixnetwork_restpy.multivalue.Multivalue)): The amount of time (in ns) that the read transmit timestamp of sent messages (two-step Sync, DelayReq, PdelayReq, two-step PdelayResp) needs to be adjusted for error
			UpdateTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Clocks in Slave role will correct their time based on received Sync messages

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp.Ptp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp import Ptp
		return self._select(Ptp(self), locals())

	def add_Ptp(self, AvnuMode="aVNU_NA", ConnectedVia=None, EnableNegativeTesting="False", Frequency="0", Multiplier="1", Name=None, NumberOFMsgs="1", StackedLayers=None):
		"""Adds a child instance of Ptp on the server.

		Args:
			AvnuMode (str(aVNU_GPTP|aVNU_NA)): AVNU Mode
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableNegativeTesting (bool): Enable Negative Conformance Test
			Frequency (number): Frequency(N)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOFMsgs (number): Messages Count
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp.Ptp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp import Ptp
		return self._create(Ptp(self), locals())

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

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def CaCert(self):
		"""The CA certificate to be used

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('caCert')

	@property
	def CertDir(self):
		"""The location to the saved certificates

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('certDir')

	@property
	def CertificateKeySameFile(self):
		"""flag to determine whether to use same Certificate file for both Private Key and User Certificate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('certificateKeySameFile')

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
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def FastInnerMethod(self):
		"""FAST Inner Method

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastInnerMethod')

	@property
	def FastProMode(self):
		"""FAST Provision Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastProMode')

	@property
	def Faststateless(self):
		"""FAST Stateless Resume

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('faststateless')

	@property
	def HostAuthMode(self):
		"""Host Authentication Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostAuthMode')

	@property
	def HostCert(self):
		"""The Peer certificate to be used by the host

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostCert')

	@property
	def HostKey(self):
		"""The private key certificate to be used by the host

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostKey')

	@property
	def HostName(self):
		"""Credential of the host for authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostName')

	@property
	def HostPwd(self):
		"""Password of the host for authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostPwd')

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
	def ParentEth(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)
		"""
		return self._get_attribute('parentEth')
	@ParentEth.setter
	def ParentEth(self, value):
		self._set_attribute('parentEth', value)

	@property
	def PeerCert(self):
		"""The Peer certificate to be used

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('peerCert')

	@property
	def PrivateKey(self):
		"""The private key certificate to be used

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('privateKey')

	@property
	def Protocol(self):
		"""protocol for authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('protocol')

	@property
	def RunTimeCertGen(self):
		"""Generate Certificate during Run time. Configure details in Global parameters. Common Name will be User Name. Certificate and Key file names will be generated based on corresponding Client User name. Eg: If Client User name is IxiaUser1 then Certificate File will be IxiaUser1.pem, Key File will be IxiaUser1_key.pem, CA certificate File will be root.pem

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('runTimeCertGen')

	@property
	def SendCACertOnly(self):
		"""Use this option to send CA Certificate only to Port. Eg: For PEAPv0/v1 case there is no need to send User Certificate to port.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendCACertOnly')

	@property
	def SessionInfo(self):
		"""Current 802.1x session state: Log Off - Supplicant has been sent EAPOL-Logoff message. Stopped - Supplicant disconnected succesfully. Authenticating - Supplicant is being authenticated. but negotiation didn't complete yet. Held - Supplicant ignores and discards all EAPOL packets. Authenticated - Authenticator has successfully authenticated the Supplicant. Restart - Supplicant is entered Restart state. Force Authentication - This state is entered because DUT's portControl is set to force-authorized. Force UnAuthentication - This state is entered because DUT's portControl is set to force-unauthorized. Unconfigured - Supplicant Unconfigured state. Configured - Supplicant initilize state. Authentication Failure - Supplicant's authentication failed. CA Cert Load Failed - Supplicant's unable to load CA certificate. Failed To Load Certificate/Key - Failed to load certificate or certificate key. Invalid EAP - Invalid EAP. Generic EAP Failure - Generic EAP Failure.

		Returns:
			list(str[acquired|authenticated|authenticating|configured|connecting|disconnected|eapFailure|forceAuth|forceUnAuth|genFailure|held|initFailure|invalidFailure|loadFailure|logoff|restart|unconfigured])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

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

	@property
	def TlsVersion(self):
		"""TLS version selecction

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tlsVersion')

	@property
	def UserName(self):
		"""Credential of the user for authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('userName')

	@property
	def UserPwd(self):
		"""Password of the user for authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('userPwd')

	@property
	def VerifyPeer(self):
		"""Verifies the provided peer certificate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('verifyPeer')

	@property
	def WaitId(self):
		"""When enabled, the supplicant does not send the initial EAPOL Start message. Instead, it waits for the authenticator (the DUT) to send an EAPOL Request / Identity message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('waitId')

	def remove(self):
		"""Deletes a child instance of DotOneX on the server.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./dotOneX object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
