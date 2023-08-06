from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv4(Base):
	"""Static IPV4
	"""

	_SDM_NAME = 'ipv4'

	def __init__(self, parent):
		super(Ipv4, self).__init__(parent)

	def Ancp(self, Count=None, DescriptiveName=None, DynamicTopologyDiscovery=None, KeepAliveRetries=None, KeepAliveTimeout=None, LineConfiguration=None, MaxRedialAttempts=None, Multiplier=None, Name=None, NasIp=None, NasServicePort=None, PartitionId=None, RemoteLoopback=None, Standard=None, Status=None, TransactionalMulticast=None, TriggerAccessLoopEvents=None, UnlimitedRedial=None):
		"""Gets child instances of Ancp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ancp will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DynamicTopologyDiscovery (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable/Disable Dynamic Topology Discovery capability
			KeepAliveRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of times ANCP adjacency mechanism send ANCP keep-alive packets before closing the TCP connections
			KeepAliveTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timer value in units of 100ms used in the adjacency protocol with the peer
			LineConfiguration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable/Disable DSL Line Configuration capability
			MaxRedialAttempts (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of attempts to establish ANCP adjacency in case connection is lost
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NasIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Ip address of BRAS listening for ANCP connections
			NasServicePort (obj(ixnetwork_restpy.multivalue.Multivalue)): BRAS TCP port number used to listen for ANCP connections
			PartitionId (obj(ixnetwork_restpy.multivalue.Multivalue)): Partition ID to be used in adjacency negotiation
			RemoteLoopback (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable/Disable DSL Remote Line Conectivity Testing Capability
			Standard (obj(ixnetwork_restpy.multivalue.Multivalue)): Define ANCP Standard to be used.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TransactionalMulticast (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable/Disable advertise Transactional Multicast capability
			TriggerAccessLoopEvents (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable sending Port Up/ Port Down events when AN is Started / Stopped. Does not apply if flapping is enabled on the Access Loop
			UnlimitedRedial (obj(ixnetwork_restpy.multivalue.Multivalue)): Limit the Number of attempts to establish ANCP adjacency in case connection is lost

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp.Ancp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp import Ancp
		return self._select(Ancp(self), locals())

	def add_Ancp(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ancp on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp.Ancp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp import Ancp
		return self._create(Ancp(self), locals())

	def Bfdv4Interface(self, Active=None, AggregateBfdSession=None, ConfigureEchoSourceIp=None, Count=None, DescriptiveName=None, EchoRxInterval=None, EchoTimeOut=None, EchoTxInterval=None, EnableControlPlaneIndependent=None, EnableDemandMode=None, FlapTxIntervals=None, IpDiffServ=None, MinRxInterval=None, Multiplier=None, Name=None, NoOfSessions=None, PollInterval=None, SourceIp4=None, Status=None, TimeoutMultiplier=None, TxInterval=None):
		"""Gets child instances of Bfdv4Interface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Bfdv4Interface will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConfigureEchoSourceIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Selecting this check box enables the ability to configure the source address IP of echo message
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EchoRxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The minimum interval, in milliseconds, between received BFD Echo packets that this interface is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets
			EchoTimeOut (obj(ixnetwork_restpy.multivalue.Multivalue)): The interval, in milliseconds, that the interface waits for a response to the last Echo packet sent out
			EchoTxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Echo packets
			EnableControlPlaneIndependent (obj(ixnetwork_restpy.multivalue.Multivalue)): This check box enables Control Plane Independent Mode. If set, the interface's BFD is implemented in the forwarding plane and can continue to function through disruptions in the control plane
			EnableDemandMode (obj(ixnetwork_restpy.multivalue.Multivalue)): This check box enables Demand Mode. In this mode, it is assumed the interface has an independent way of verifying it has connectivity to the other system. Once a BFD session is established, the systems stop sending BFD Control packets, except when either system feels the need to verify connectivity explicitly. In this case, a short sequence of BFD Control packets is sent
			FlapTxIntervals (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of Tx packets sent from device after which session flaps for BFD. A value of zero means no flapping
			IpDiffServ (obj(ixnetwork_restpy.multivalue.Multivalue)): IP DiffServ/TOSByte (Dec)
			MinRxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			PollInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The interval, in milliseconds, between exchanges of Control Messages in Demand Mode
			SourceIp4 (obj(ixnetwork_restpy.multivalue.Multivalue)): If Configure Echo Source-IP is selected, the IPv4 source address of the Echo Message
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TimeoutMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): The negotiated transmit interval, multiplied by this value, provides the detection time for the interface
			TxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface.Bfdv4Interface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface import Bfdv4Interface
		return self._select(Bfdv4Interface(self), locals())

	def add_Bfdv4Interface(self, AggregateBfdSession="True", ConnectedVia=None, Multiplier="1", Name=None, NoOfSessions="0", StackedLayers=None):
		"""Adds a child instance of Bfdv4Interface on the server.

		Args:
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface.Bfdv4Interface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface import Bfdv4Interface
		return self._create(Bfdv4Interface(self), locals())

	def BgpIpv4Peer(self, ActAsRestarted=None, Active=None, AdvertiseEndOfRib=None, AlwaysIncludeTunnelEncExtCommunity=None, AsSetMode=None, Authentication=None, BgpId=None, BgpLsAsSetMode=None, BgpLsEnableAsPathSegments=None, BgpLsEnableCluster=None, BgpLsEnableExtendedCommunity=None, BgpLsNoOfASPathSegments=None, BgpLsNoOfClusters=None, BgpLsNoOfCommunities=None, BgpLsOverridePeerAsSetMode=None, CapabilityIpV4Mdt=None, CapabilityIpV4Mpls=None, CapabilityIpV4MplsVpn=None, CapabilityIpV4Multicast=None, CapabilityIpV4MulticastVpn=None, CapabilityIpV4Unicast=None, CapabilityIpV6Mpls=None, CapabilityIpV6MplsVpn=None, CapabilityIpV6Multicast=None, CapabilityIpV6MulticastVpn=None, CapabilityIpV6Unicast=None, CapabilityIpv4MplsAddPath=None, CapabilityIpv4UnicastAddPath=None, CapabilityIpv6MplsAddPath=None, CapabilityIpv6UnicastAddPath=None, CapabilityLinkStateNonVpn=None, CapabilityRouteConstraint=None, CapabilityRouteRefresh=None, CapabilitySRTEPoliciesV4=None, CapabilitySRTEPoliciesV6=None, CapabilityVpls=None, Capabilityipv4UnicastFlowSpec=None, Capabilityipv6UnicastFlowSpec=None, ConfigureKeepaliveTimer=None, Count=None, CustomSidType=None, DescriptiveName=None, DiscardIxiaGeneratedRoutes=None, DowntimeInSec=None, DutIp=None, Enable4ByteAs=None, EnableBfdRegistration=None, EnableBgpId=None, EnableBgpIdSameasRouterId=None, EnableBgpLsCommunity=None, EnableEPETraffic=None, EnableGracefulRestart=None, EnableLlgr=None, EthernetSegmentsCountV4=None, Evpn=None, FilterEvpn=None, FilterIpV4Mpls=None, FilterIpV4MplsVpn=None, FilterIpV4Multicast=None, FilterIpV4MulticastVpn=None, FilterIpV4Unicast=None, FilterIpV6Mpls=None, FilterIpV6MplsVpn=None, FilterIpV6Multicast=None, FilterIpV6MulticastVpn=None, FilterIpV6Unicast=None, FilterIpv4MulticastBgpMplsVpn=None, FilterIpv4UnicastFlowSpec=None, FilterIpv6MulticastBgpMplsVpn=None, FilterIpv6UnicastFlowSpec=None, FilterLinkState=None, FilterSRTEPoliciesV4=None, FilterSRTEPoliciesV6=None, FilterVpls=None, Flap=None, HoldTimer=None, IpVrfToIpVrfType=None, Ipv4MplsAddPathMode=None, Ipv4MplsCapability=None, Ipv4MulticastBgpMplsVpn=None, Ipv4MultipleMplsLabelsCapability=None, Ipv4UnicastAddPathMode=None, Ipv6MplsAddPathMode=None, Ipv6MplsCapability=None, Ipv6MulticastBgpMplsVpn=None, Ipv6MultipleMplsLabelsCapability=None, Ipv6UnicastAddPathMode=None, IrbInterfaceLabel=None, IrbIpv4Address=None, KeepaliveTimer=None, LocalAs2Bytes=None, LocalAs4Bytes=None, Md5Key=None, ModeOfBfdOperations=None, MplsLabelsCountForIpv4MplsRoute=None, MplsLabelsCountForIpv6MplsRoute=None, Multiplier=None, Name=None, NoOfEPEPeers=None, NoOfExtendedCommunities=None, NoOfPeerSet=None, NoOfUserDefinedAfiSafi=None, NumBgpLsId=None, NumBgpLsInstanceIdentifier=None, NumBgpUpdatesGeneratedPerIteration=None, NumberFlowSpecRangeV4=None, NumberFlowSpecRangeV6=None, NumberSRTEPolicies=None, OperationalModel=None, RestartTime=None, RoutersMacOrIrbMacAddress=None, SRGBRangeCount=None, SendIxiaSignatureWithRoutes=None, StaleTime=None, Status=None, TcpWindowSizeInBytes=None, Ttl=None, Type=None, UpdateInterval=None, UptimeInSec=None, VplsEnableNextHop=None, VplsNextHop=None):
		"""Gets child instances of BgpIpv4Peer from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIpv4Peer will be returned.

		Args:
			ActAsRestarted (obj(ixnetwork_restpy.multivalue.Multivalue)): Act as restarted
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseEndOfRib (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise End-Of-RIB
			AlwaysIncludeTunnelEncExtCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Always Include Tunnel Encapsulation Extended Community
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Authentication (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Type
			BgpId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP ID
			BgpLsAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			BgpLsEnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			BgpLsEnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			BgpLsEnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			BgpLsOverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			CapabilityIpV4Mdt (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 MDT
			CapabilityIpV4Mpls (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 MPLS
			CapabilityIpV4MplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 MPLS VPN
			CapabilityIpV4Multicast (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Multicast
			CapabilityIpV4MulticastVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Multicast VPN
			CapabilityIpV4Unicast (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Unicast
			CapabilityIpV6Mpls (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 MPLS
			CapabilityIpV6MplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 MPLS VPN
			CapabilityIpV6Multicast (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Multicast
			CapabilityIpV6MulticastVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Multicast VPN
			CapabilityIpV6Unicast (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Unicast
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv4UnicastAddPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv4 Unicast Add Path
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			CapabilityIpv6UnicastAddPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv6 Unicast Add Path
			CapabilityLinkStateNonVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Non-VPN
			CapabilityRouteConstraint (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Constraint
			CapabilityRouteRefresh (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Refresh
			CapabilitySRTEPoliciesV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv4 SR TE Policy Capability
			CapabilitySRTEPoliciesV6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6 SR TE Policy Capability
			CapabilityVpls (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS
			Capabilityipv4UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Unicast Flow Spec
			Capabilityipv6UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Unicast Flow Spec
			ConfigureKeepaliveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Keepalive Timer
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CustomSidType (obj(ixnetwork_restpy.multivalue.Multivalue)): moved to port data in bgp/srv6 Custom SID Type
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardIxiaGeneratedRoutes (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard Ixia Generated Routes
			DowntimeInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime in Seconds
			DutIp (obj(ixnetwork_restpy.multivalue.Multivalue)): DUT IP
			Enable4ByteAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 4-Byte AS
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableBgpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BGP ID
			EnableBgpIdSameasRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP ID Same as Router ID
			EnableBgpLsCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableEPETraffic (bool): Enable EPE Traffic
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Graceful Restart
			EnableLlgr (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable LLGR
			EthernetSegmentsCountV4 (number): Number of Ethernet Segments
			Evpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for EVPN
			FilterEvpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for EVPN filter
			FilterIpV4Mpls (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 MPLS
			FilterIpV4MplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 MPLS VPN
			FilterIpV4Multicast (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 Multicast
			FilterIpV4MulticastVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 Multicast VPN
			FilterIpV4Unicast (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 Unicast
			FilterIpV6Mpls (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 MPLS
			FilterIpV6MplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 MPLS VPN
			FilterIpV6Multicast (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 Multicast
			FilterIpV6MulticastVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 Multicast VPN
			FilterIpV6Unicast (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 Unicast
			FilterIpv4MulticastBgpMplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv4 Multicast BGP/MPLS VPN filter
			FilterIpv4UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv4 Unicast Flow Spec
			FilterIpv6MulticastBgpMplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv6 Multicast BGP/MPLS VPN filter
			FilterIpv6UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter IPv6 Unicast Flow Spec
			FilterLinkState (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter Link State
			FilterSRTEPoliciesV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv4 SR TE Policy Filter
			FilterSRTEPoliciesV6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6 SR TE Policy Filter
			FilterVpls (obj(ixnetwork_restpy.multivalue.Multivalue)): Filter VPLS
			Flap (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap
			HoldTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Hold Timer
			IpVrfToIpVrfType (str(interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsAddPathMode (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 MPLS Add Path Mode
			Ipv4MplsCapability (bool): IPv4 MPLS Capability
			Ipv4MulticastBgpMplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv4 Multicast BGP/MPLS VPN
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability
			Ipv4UnicastAddPathMode (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Unicast Add Path Mode
			Ipv6MplsAddPathMode (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 MPLS Add Path Mode
			Ipv6MplsCapability (bool): IPv6 MPLS Capability
			Ipv6MulticastBgpMplsVpn (obj(ixnetwork_restpy.multivalue.Multivalue)): Check box for IPv6 Multicast BGP/MPLS VPN
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability
			Ipv6UnicastAddPathMode (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Unicast Add Path Mode
			IrbInterfaceLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2
			IrbIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IRB IPv4 Address
			KeepaliveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Keepalive Timer
			LocalAs2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Local AS# (2-Bytes)
			LocalAs4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Local AS# (4-Bytes)
			Md5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): MD5 Key
			ModeOfBfdOperations (obj(ixnetwork_restpy.multivalue.Multivalue)): Mode of BFD Operations
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEPEPeers (number): 
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfPeerSet (number): 
			NoOfUserDefinedAfiSafi (number): Count of User Defined AFI SAFI
			NumBgpLsId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP LS Instance ID
			NumBgpLsInstanceIdentifier (obj(ixnetwork_restpy.multivalue.Multivalue)): IGP Multi instance unique identifier. 0 is default single-instance IGP. (e.g. for OSPFv3 it is possible to separately run 4 instances of OSPFv3 with peer, one advertising v4 only, another v6 only and other 2 mcast v4 and v6 respectively) .
			NumBgpUpdatesGeneratedPerIteration (obj(ixnetwork_restpy.multivalue.Multivalue)): Num BGP Updates Generated Per Iteration
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			OperationalModel (obj(ixnetwork_restpy.multivalue.Multivalue)): Operational Model
			RestartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Time
			RoutersMacOrIrbMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Router's MAC/IRB MAC Address
			SRGBRangeCount (number): SRGB Range Count
			SendIxiaSignatureWithRoutes (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Ixia Signature With Routes
			StaleTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Stale Time/ LLGR Stale Time
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TcpWindowSizeInBytes (obj(ixnetwork_restpy.multivalue.Multivalue)): TCP Window Size (in bytes)
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): TTL
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type
			UpdateInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Update Interval
			UptimeInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime in Seconds
			VplsEnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS Enable Next Hop
			VplsNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS Next Hop

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer.BgpIpv4Peer))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer import BgpIpv4Peer
		return self._select(BgpIpv4Peer(self), locals())

	def add_BgpIpv4Peer(self, BgpLsNoOfASPathSegments="1", BgpLsNoOfClusters="1", BgpLsNoOfCommunities="1", CapabilityIpv4MplsAddPath="False", CapabilityIpv6MplsAddPath="False", ConnectedVia=None, EnableEPETraffic="False", EthernetSegmentsCountV4="0", IpVrfToIpVrfType="interfacefullWithUnnumberedCorefacingIRB", Ipv4MplsCapability="False", Ipv4MultipleMplsLabelsCapability="False", Ipv6MplsCapability="False", Ipv6MultipleMplsLabelsCapability="False", MplsLabelsCountForIpv4MplsRoute="1", MplsLabelsCountForIpv6MplsRoute="1", Multiplier="1", Name=None, NoOfEPEPeers="0", NoOfExtendedCommunities="1", NoOfPeerSet="0", NoOfUserDefinedAfiSafi="0", NumberFlowSpecRangeV4="0", NumberFlowSpecRangeV6="0", NumberSRTEPolicies="0", SRGBRangeCount="1", StackedLayers=None):
		"""Adds a child instance of BgpIpv4Peer on the server.

		Args:
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableEPETraffic (bool): Enable EPE Traffic
			EthernetSegmentsCountV4 (number): Number of Ethernet Segments
			IpVrfToIpVrfType (str(interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsCapability (bool): IPv4 MPLS Capability
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability
			Ipv6MplsCapability (bool): IPv6 MPLS Capability
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEPEPeers (number): 
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfPeerSet (number): 
			NoOfUserDefinedAfiSafi (number): Count of User Defined AFI SAFI
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			SRGBRangeCount (number): SRGB Range Count
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer.BgpIpv4Peer)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer import BgpIpv4Peer
		return self._create(BgpIpv4Peer(self), locals())

	def Dhcpv4relayAgent(self, Count=None, DescriptiveName=None, Dhcp4RelayAddress=None, Dhcp4RelayAgentGlobalAndPortData=None, Dhcp4ServerAddress=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of Dhcpv4relayAgent from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv4relayAgent will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Dhcp4RelayAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Complete description here
			Dhcp4RelayAgentGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			Dhcp4ServerAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Complete description here
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent.Dhcpv4relayAgent))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent import Dhcpv4relayAgent
		return self._select(Dhcpv4relayAgent(self), locals())

	def add_Dhcpv4relayAgent(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Dhcpv4relayAgent on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent.Dhcpv4relayAgent)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent import Dhcpv4relayAgent
		return self._create(Dhcpv4relayAgent(self), locals())

	def Dhcpv4server(self, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Status=None, Subnet=None, SubnetAddrAssign=None, UseRapidCommit=None):
		"""Gets child instances of Dhcpv4server from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv4server will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			Subnet (obj(ixnetwork_restpy.multivalue.Multivalue)): Choose which subnet to be used for address assignment.
			SubnetAddrAssign (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables DHCP Server to assign addresses based on subnet. The leased address is created dynamically by overwriting the subnet portion defined in the Address Pool with the subnet option present in the requests from the clients behind relays.
			UseRapidCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables DHCP Server to negotiate leases with rapid commit for DHCP Clients that request it.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server.Dhcpv4server))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server import Dhcpv4server
		return self._select(Dhcpv4server(self), locals())

	def add_Dhcpv4server(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Dhcpv4server on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server.Dhcpv4server)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server import Dhcpv4server
		return self._create(Dhcpv4server(self), locals())

	def Geneve(self, Count=None, DescriptiveName=None, EnableUdpCsum=None, Ipv4Remote=None, Multiplier=None, Name=None, Status=None, UdpDestPort=None, Vni=None):
		"""Gets child instances of Geneve from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Geneve will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableUdpCsum (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable UDP checksum for outgoing packets
			Ipv4Remote (obj(ixnetwork_restpy.multivalue.Multivalue)): The IPv4 address of the remote tunnel endpoint
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UdpDestPort (obj(ixnetwork_restpy.multivalue.Multivalue)): The UDP port used for GENEVE communication
			Vni (obj(ixnetwork_restpy.multivalue.Multivalue)): The virtual network identifier for this tunnel endpoint

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve.Geneve))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve import Geneve
		return self._select(Geneve(self), locals())

	def add_Geneve(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Geneve on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve.Geneve)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve import Geneve
		return self._create(Geneve(self), locals())

	def Greoipv4(self, Count=None, DescriptiveName=None, DestIp=None, EnableChecksum=None, EnableKey=None, EnableSequenceNumber=None, InKey=None, Multiplier=None, Name=None, OutKey=None, SrcIp=None, Status=None):
		"""Gets child instances of Greoipv4 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Greoipv4 will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination IPv4 address
			EnableChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Checksum.
			EnableKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Key.
			EnableSequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Sequence Number.
			InKey (obj(ixnetwork_restpy.multivalue.Multivalue)): In Key.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OutKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Out Key.
			SrcIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Source IPv4 address
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4.Greoipv4))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4 import Greoipv4
		return self._select(Greoipv4(self), locals())

	def add_Greoipv4(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Greoipv4 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4.Greoipv4)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4 import Greoipv4
		return self._create(Greoipv4(self), locals())

	def IgmpHost(self, Active=None, Count=None, DescriptiveName=None, EnableIptv=None, EnableProxyReporting=None, GQResponseMode=None, GSResponseMode=None, ImResponse=None, JlMultiplier=None, Multiplier=None, Name=None, NoOfGrpRanges=None, ReportFreq=None, RouterAlert=None, Status=None, USResponseMode=None, VersionType=None):
		"""Gets child instances of IgmpHost from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IgmpHost will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableIptv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPTV
			EnableProxyReporting (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Proxy Reporting
			GQResponseMode (obj(ixnetwork_restpy.multivalue.Multivalue)): General Query Response Mode
			GSResponseMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Specific Response Mode
			ImResponse (obj(ixnetwork_restpy.multivalue.Multivalue)): Immediate Response
			JlMultiplier (number): No. of Join/Leave messages to send per opertation
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfGrpRanges (number): Defines the number of group range per host required
			ReportFreq (obj(ixnetwork_restpy.multivalue.Multivalue)): Report Frequency measured in seconds
			RouterAlert (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables Router Alert option of IPv4 Packet
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			USResponseMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Unsolicited Response Mode
			VersionType (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the IGMP Version Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost.IgmpHost))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost import IgmpHost
		return self._select(IgmpHost(self), locals())

	def add_IgmpHost(self, ConnectedVia=None, JlMultiplier="1", Multiplier="1", Name=None, NoOfGrpRanges="1", StackedLayers=None):
		"""Adds a child instance of IgmpHost on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			JlMultiplier (number): No. of Join/Leave messages to send per opertation
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfGrpRanges (number): Defines the number of group range per host required
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost.IgmpHost)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost import IgmpHost
		return self._create(IgmpHost(self), locals())

	def IgmpQuerier(self, Active=None, Count=None, DescriptiveName=None, DiscardLearntInfo=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, Multiplier=None, Name=None, ProxyQuerier=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseInterval=None, SpecificQueryTransmissionCount=None, StartupQueryCount=None, Status=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, VersionType=None):
		"""Gets child instances of IgmpQuerier from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IgmpQuerier will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLearntInfo (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard Learned Info
			GeneralQueryInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): General Query Interval in seconds
			GeneralQueryResponseInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): General Query Response Interval in milliseconds
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ProxyQuerier (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Proxy Querier
			RobustnessVariable (obj(ixnetwork_restpy.multivalue.Multivalue)): Robustness Variable
			RouterAlert (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Alert
			SpecificQueryResponseInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Specific Query Response Interval in milliseconds
			SpecificQueryTransmissionCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Specific Query Transmission Count
			StartupQueryCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Startup Query Count
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportElection (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Election
			SupportOlderVersionHost (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Older Version Host
			SupportOlderVersionQuerier (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Older Version Querier
			VersionType (obj(ixnetwork_restpy.multivalue.Multivalue)): Version

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier.IgmpQuerier))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier import IgmpQuerier
		return self._select(IgmpQuerier(self), locals())

	def add_IgmpQuerier(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of IgmpQuerier on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier.IgmpQuerier)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier import IgmpQuerier
		return self._create(IgmpQuerier(self), locals())

	def Lac(self, BaseLnsIp=None, BearerCapability=None, BearerType=None, ControlMsgsRetryCounter=None, Count=None, DescriptiveName=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableExcludeHdlc=None, EnableHelloRequest=None, EnableRedial=None, FramingCapability=None, HelloRequestInterval=None, InitRetransmitInterval=None, LacHostName=None, LacSecret=None, MaxRedialAttempts=None, MaxRetransmitInterval=None, Multiplier=None, Name=None, OffsetByte=None, OffsetLength=None, ReceiveWindowSize=None, RedialInterval=None, Status=None, TunnelAuthentication=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAVPs=None, UseLengthBitInPayload=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
		"""Gets child instances of Lac from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Lac will be returned.

		Args:
			BaseLnsIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Defines the base address to be used by the L2TP tunnel
			BearerCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates to the DUT the bearer device types from which incoming calls will be accepted.
			BearerType (obj(ixnetwork_restpy.multivalue.Multivalue)): The bearer type.
			ControlMsgsRetryCounter (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of L2TP retries
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableControlChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, UDP checksum is enabled on control plane packets
			EnableDataChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, UDP checksum is enabled on data plane packets
			EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
			EnableHelloRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, L2TP hello request is enabled
			EnableRedial (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, L2TP redial is enabled
			FramingCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Designates sync or async framing
			HelloRequestInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for L2TP hello request, in seconds
			InitRetransmitInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The initial amount of time that can elapse before an unacknowledged control message is retransmitted.
			LacHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): LAC Hostname used for tunnel authentication.
			LacSecret (obj(ixnetwork_restpy.multivalue.Multivalue)): Secret value used for tunnel authentication.
			MaxRedialAttempts (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of L2TP redial attempts
			MaxRetransmitInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The maximum amount of time that can elapse for receiving a reply for a control message.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OffsetByte (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP offset byte. Applicable only if offset bit is set.
			OffsetLength (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP offset length in bytes. Applicable only if offset bit set.
			ReceiveWindowSize (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP Receive Window Size
			RedialInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP redial timeout, in seconds
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TunnelAuthentication (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables or disables L2TP tunnel authentication
			UdpDestinationPort (obj(ixnetwork_restpy.multivalue.Multivalue)): UDP port to employ for tunneling destinations
			UdpSourcePort (obj(ixnetwork_restpy.multivalue.Multivalue)): UDP port to employ for tunneling sources
			UseHiddenAVPs (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, Attribute Value Pair hiding is enabled
			UseLengthBitInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, length bit is set in L2TP data packets.
			UseOffsetBitInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, offset bit is enabled in L2TP data packets
			UseSequenceNoInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, sequence bit is set in L2TP data packets.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac.Lac))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac import Lac
		return self._select(Lac(self), locals())

	def add_Lac(self, ConnectedVia=None, EnableExcludeHdlc="False", Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Lac on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac.Lac)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac import Lac
		return self._create(Lac(self), locals())

	def LdpBasicRouter(self, Active=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LdpVersion=None, LeafRangesCountV4=None, Multiplier=None, Name=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV4=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpBasicRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpBasicRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
		return self._select(LdpBasicRouter(self), locals())

	def add_LdpBasicRouter(self, ConnectedVia=None, LdpVersion="version1", LeafRangesCountV4="0", Multiplier="1", Name=None, RootRangesCountV4="0", StackedLayers=None):
		"""Adds a child instance of LdpBasicRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
		return self._create(LdpBasicRouter(self), locals())

	def LdpConnectedInterface(self, Active=None, Authentication=None, BasicHelloInterval=None, BasicHoldTime=None, Count=None, DescriptiveName=None, EnableBfdRegistration=None, LabelSpaceID=None, MD5Key=None, Multiplier=None, Name=None, OperationMode=None, Status=None):
		"""Gets child instances of LdpConnectedInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpConnectedInterface will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Authentication (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of cryptographic authentication to be used on this link interface
			BasicHelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of seconds between this router's Hello packets.
			BasicHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum length of time that a sending LSR will retain the record of Hellos sent by the receiving LSR, without receiving another Hello message.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			LabelSpaceID (obj(ixnetwork_restpy.multivalue.Multivalue)): Identifies the set of labels that will be used. Part of the LDP Identifier.
			MD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): A value to be used as the secret MD5 Key.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of LDP Label Advertisement.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface.LdpConnectedInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface import LdpConnectedInterface
		return self._select(LdpConnectedInterface(self), locals())

	def add_LdpConnectedInterface(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of LdpConnectedInterface on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface.LdpConnectedInterface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface import LdpConnectedInterface
		return self._create(LdpConnectedInterface(self), locals())

	def LdpTargetedRouter(self, Active=None, BfdOpeMode=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableBfdRegistration=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, Ipv6peerCount=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LabelSpaceID=None, LdpVersion=None, LeafRangesCountV4=None, Multiplier=None, Name=None, OperationMode=None, PeerCount=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV4=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpTargetedRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpTargetedRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BfdOpeMode (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD Operation Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LabelSpaceID (obj(ixnetwork_restpy.multivalue.Multivalue)): Identifies the set of labels that will be used. Part of the LDP Identifier
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of LDP Label Advertisement
			PeerCount (number): The number of Target Peers configured for this LDP router
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
		return self._select(LdpTargetedRouter(self), locals())

	def add_LdpTargetedRouter(self, ConnectedVia=None, Ipv6peerCount="0", LdpVersion="version1", LeafRangesCountV4="0", Multiplier="1", Name=None, PeerCount="0", RootRangesCountV4="0", StackedLayers=None):
		"""Adds a child instance of LdpTargetedRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeerCount (number): The number of Target Peers configured for this LDP router
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
		return self._create(LdpTargetedRouter(self), locals())

	def Lns(self, BearerCapability=None, BearerType=None, ControlMsgsRetryCounter=None, Count=None, CredentialsCount=None, DescriptiveName=None, EnableControlChecksum=None, EnableDataChecksum=None, EnableExcludeHdlc=None, EnableHelloRequest=None, FramingCapability=None, HelloRequestInterval=None, InitRetransmitInterval=None, LacHostName=None, LacSecret=None, LnsHostName=None, MaxRetransmitInterval=None, Multiplier=None, Name=None, NoCallTimeout=None, OffsetByte=None, OffsetLength=None, ReceiveWindowSize=None, Status=None, TunnelAuthentication=None, UdpDestinationPort=None, UdpSourcePort=None, UseHiddenAVPs=None, UseLengthBitInPayload=None, UseOffsetBitInPayload=None, UseSequenceNoInPayload=None):
		"""Gets child instances of Lns from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Lns will be returned.

		Args:
			BearerCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates to the DUT the bearer device types from which incoming calls will be accepted.
			BearerType (obj(ixnetwork_restpy.multivalue.Multivalue)): The bearer type.
			ControlMsgsRetryCounter (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of L2TP retries
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CredentialsCount (number): Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableControlChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, UDP checksum is enabled on control plane packets
			EnableDataChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, UDP checksum is enabled on data plane packets
			EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
			EnableHelloRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, L2TP hello request is enabled
			FramingCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Designates sync or async framing
			HelloRequestInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for L2TP hello request, in seconds
			InitRetransmitInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The initial amount of time that can elapse before an unacknowledged control message is retransmitted.
			LacHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the hostname used in authentication.
			LacSecret (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP secret to be used in authentication
			LnsHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP hostname sent by Ixia port when acting as LNS
			MaxRetransmitInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The maximum amount of time that can elapse for receiving a reply for a control message.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoCallTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for no call establishment, in seconds
			OffsetByte (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP offset byte. Applicable only if offset bit is set.
			OffsetLength (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP offset length in bytes. Applicable only if offset bit set.
			ReceiveWindowSize (obj(ixnetwork_restpy.multivalue.Multivalue)): L2TP Receive Window Size
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TunnelAuthentication (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables or disables L2TP tunnel authentication
			UdpDestinationPort (obj(ixnetwork_restpy.multivalue.Multivalue)): UDP port to employ for tunneling destinations
			UdpSourcePort (obj(ixnetwork_restpy.multivalue.Multivalue)): UDP port to employ for tunneling sources
			UseHiddenAVPs (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, Attribute Value Pair hiding is enabled
			UseLengthBitInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, length bit is set in L2TP data packets.
			UseOffsetBitInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, offset bit is enabled in L2TP data packets
			UseSequenceNoInPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If checked, sequence bit is set in L2TP data packets.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns.Lns))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns import Lns
		return self._select(Lns(self), locals())

	def add_Lns(self, ConnectedVia=None, CredentialsCount="1", EnableExcludeHdlc="False", Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Lns on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CredentialsCount (number): Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.
			EnableExcludeHdlc (bool): If checked, HDLC header is not encoded in the L2TP packets.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns.Lns)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns import Lns
		return self._create(Lns(self), locals())

	def MplsOam(self, Active=None, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, Count=None, DescriptiveName=None, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddressNumbered=None, DownstreamInterfaceAddressUnnumbered=None, DownstreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDSIflag=None, EnableDownstreamMappingTlv=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumbeTlv=None, MinRxInterval=None, Multiplier=None, Name=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, Status=None, TimeoutMultiplier=None, TxInterval=None, VendorEnterpriseNumber=None):
		"""Gets child instances of MplsOam from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MplsOam will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BfdCvType (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the BFD Connectivity Verification type
			BfdDiscriminatorEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the last BFD Discriminator value. This value should be greater than the BFD Discriminator Start value
			BfdDiscriminatorStart (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the first BFD Discriminator value
			ControlChannel (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the communication control channel
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestinationAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): The destination IPv4 Address
			DownstreamAddressType (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the address Type of the downstream traffic
			DownstreamInterfaceAddressNumbered (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the interface address of the downstream traffic in IPv4 format
			DownstreamInterfaceAddressUnnumbered (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the interface address of the downstream traffic
			DownstreamIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the IPv4/IPv6 address of the downstream traffic
			EchoRequestInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting
			EchoResponseTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the minimum timeout interval, in milliseconds, between received Echo packets
			EnableDSIflag (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the activation of the DS I Flag
			EnableDownstreamMappingTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the enable of the downstream mapping TLV
			EnableDsNflag (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the activation of the DS N Flag
			EnableFecValidation (obj(ixnetwork_restpy.multivalue.Multivalue)): Selection of the check box enables FEC validation
			EnablePeriodicPing (obj(ixnetwork_restpy.multivalue.Multivalue)): If true, the router is pinged at regular intervals
			FlapTxIntervals (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping
			IncludePadTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If true, includes Pad TLV in triggered ping
			IncludeVendorEnterpriseNumbeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If true, include the TLV number of the vendor, in triggered ping
			MinRxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PadTlvFirstOctet (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the selection of the first octet of the Pad TLV
			PadTlvLength (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the specification of the length of the Pad TLV
			ReplyMode (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the selection of the mode of reply
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TimeoutMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface
			TxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets
			VendorEnterpriseNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): This signifies the specification of the enterprise number of the vendor

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam.MplsOam))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam import MplsOam
		return self._select(MplsOam(self), locals())

	def add_MplsOam(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of MplsOam on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam.MplsOam)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam import MplsOam
		return self._create(MplsOam(self), locals())

	def NetconfClient(self, Active=None, CapabilitiesBase1Dot0=None, CapabilitiesBase1Dot1=None, CapabilitiesCandidate=None, CapabilitiesConfirmedCommit=None, CapabilitiesInterleave=None, CapabilitiesNotification=None, CapabilitiesRollbackOnError=None, CapabilitiesStartup=None, CapabilitiesUrl=None, CapabilitiesValidate=None, CapabilitiesWritableRunning=None, CapabilitiesXpath=None, Count=None, DecryptedCapture=None, DescriptiveName=None, EnablePassphrase=None, Multiplier=None, Name=None, NumberOfCommandSnippetsPerClient=None, OutputDirectory=None, Passphrase=None, Password=None, PortNumber=None, PrivateKeyDirectory=None, PrivateKeyFileName=None, SaveReplyXML=None, ServerIpv4Address=None, SshAuthenticationMechanism=None, Status=None, UserName=None):
		"""Gets child instances of NetconfClient from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetconfClient will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			CapabilitiesBase1Dot0 (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether base1.0 support should be advertised in Capabilities.
			CapabilitiesBase1Dot1 (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether base1.1 support should be advertised in Capabilities.
			CapabilitiesCandidate (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability candidate to make changes into an intermediate candidate database. Normally this is preferred over writable-running.
			CapabilitiesConfirmedCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability confirmed-commit to specify ability to commit a group of commands or none as a batch.
			CapabilitiesInterleave (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability interleave to interleave notifications and responses.
			CapabilitiesNotification (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability notification to aynchronously handle notifications from Netconf server device connected to.
			CapabilitiesRollbackOnError (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability rollback to rollback partial changes make changes on detection of error during validate or commit.
			CapabilitiesStartup (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability startup to make changes in config persistent on device restart.
			CapabilitiesUrl (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability url to specify netconf commands using url.
			CapabilitiesValidate (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability validate to specify ability to validate a netconf command prior to commit.
			CapabilitiesWritableRunning (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability writable-running to directly modify running config.
			CapabilitiesXpath (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability xpath to specify netconf commands and filters using xpath extensions.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DecryptedCapture (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether SSH packets for this session will be captured and stored on client in decrypted form.Note that this is not linked to IxNetwork control or data capture which will capture the packets in encrypted format only.Also note that this option should be avoided if Continuous Tranmission mode is enabled for any of the Command Snippets which can leadto huge capture files being generated which could in turn affect Stop time since during Stop, the captures are transferred to the client.The Decrypted Capture can be viewed by either doing right-click on a client where this option is enabled and doing Get Decrypted Capture( allowed on 5 clients at a time ; each of the captures will be opened in a new Wireshark pop-up) OR by stopping the client and then directly opening it from the configured Output Directory from inside the current run folder/capture.This option can be enabled even when a session is already up in which case the capture will be started from that point of time.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnablePassphrase (obj(ixnetwork_restpy.multivalue.Multivalue)): If the Private Key was passphrase protected, this should be enabled to allow configuration of passphrase used.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfCommandSnippetsPerClient (number): Number of Command Snippets per client.Maximum 100 are allowed per client.
			OutputDirectory (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the decrypted capture, if enabled, and server replies, if enabled, will be stored.
			Passphrase (obj(ixnetwork_restpy.multivalue.Multivalue)): The passphrase with which the Private Key was additionally protected during generation. For multiple clients and assymetric passphrases( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
			Password (obj(ixnetwork_restpy.multivalue.Multivalue)): Password for Username/Password mode.
			PortNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): The TCP Port Number the Netconf Server is listening on to which to connect.
			PrivateKeyDirectory (obj(ixnetwork_restpy.multivalue.Multivalue)): Directory containing Private Key file for this session.
			PrivateKeyFileName (obj(ixnetwork_restpy.multivalue.Multivalue)): File containing Private Key.(e.g. generated using ssh_keygen) . For multiple clients and assymetric key file names( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
			SaveReplyXML (obj(ixnetwork_restpy.multivalue.Multivalue)): If this is enabled, Hellos and replies to commands sent via Command Snippets or global command (such as 'get') by the Netconf Server will be stored in the Output Directoryin current run folder/Replies. Any RPC errors recieved will be stored in a separate Error directory for convenience of debugging error scenarios.This option can be enabled even when a session is already up in which case the replies will be saved from that point of time.
			ServerIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the IPv4 address of the DUT to which the Netconf Server should connect.
			SshAuthenticationMechanism (obj(ixnetwork_restpy.multivalue.Multivalue)): The authentication mechanism for connecting to Netconf Server.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UserName (obj(ixnetwork_restpy.multivalue.Multivalue)): Username for Username/Password mode and also used for Key-based Authentication as the username.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient.NetconfClient))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient import NetconfClient
		return self._select(NetconfClient(self), locals())

	def add_NetconfClient(self, ConnectedVia=None, Multiplier="1", Name=None, NumberOfCommandSnippetsPerClient="2", StackedLayers=None):
		"""Adds a child instance of NetconfClient on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfCommandSnippetsPerClient (number): Number of Command Snippets per client.Maximum 100 are allowed per client.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient.NetconfClient)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient import NetconfClient
		return self._create(NetconfClient(self), locals())

	def NetconfServer(self, Active=None, CapabilitiesBase1Dot0=None, CapabilitiesBase1Dot1=None, CapabilitiesCandidate=None, CapabilitiesConfirmedCommit=None, CapabilitiesInterleave=None, CapabilitiesNotification=None, CapabilitiesRollbackOnError=None, CapabilitiesStartup=None, CapabilitiesUrl=None, CapabilitiesValidate=None, CapabilitiesWritableRunning=None, CapabilitiesXpath=None, ClientIpv4Address=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Password=None, PublicKeyDirectory=None, PublicKeyFileName=None, SshAuthenticationMechanism=None, Status=None, UserName=None):
		"""Gets child instances of NetconfServer from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetconfServer will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			CapabilitiesBase1Dot0 (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether base1.0 support should be advertised in Capabilities.
			CapabilitiesBase1Dot1 (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether base1.1 support should be advertised in Capabilities.
			CapabilitiesCandidate (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability candidate to make changes into an intermediate candidate database. Normally this is preferred over writable-running.
			CapabilitiesConfirmedCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability confirmed-commit to specify ability to commit a group of commands or none as a batch.
			CapabilitiesInterleave (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability interleave to interleave notifications and responses.
			CapabilitiesNotification (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability notification to aynchronously send notifications to Netconf client.
			CapabilitiesRollbackOnError (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability rollback to rollback partial changes make changes on detection of error during validate or commit.
			CapabilitiesStartup (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability startup to make changes in config persistent on device restart.
			CapabilitiesUrl (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability url to specify netconf commands using url.
			CapabilitiesValidate (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability validate to specify ability to validate a netconf command prior to commit.
			CapabilitiesWritableRunning (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability writable-running to directly modify running config.
			CapabilitiesXpath (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether supports capability xpath to specify netconf commands and filters using xpath extensions.
			ClientIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the IPv4 address of the Netconf Client which will connect with this Server.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Password (obj(ixnetwork_restpy.multivalue.Multivalue)): Password for Username/Password mode.
			PublicKeyDirectory (obj(ixnetwork_restpy.multivalue.Multivalue)): Directory containing public key file for this session
			PublicKeyFileName (obj(ixnetwork_restpy.multivalue.Multivalue)): File containing public key (e.g. generated using ssh_keygen). For multiple server rows and assymetric public key filenames( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
			SshAuthenticationMechanism (obj(ixnetwork_restpy.multivalue.Multivalue)): The authentication mechanism for connecting to Netconf Client.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UserName (obj(ixnetwork_restpy.multivalue.Multivalue)): Username for Username/Password mode and Username for Key-Based authentication mode if applicable.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver.NetconfServer))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver import NetconfServer
		return self._select(NetconfServer(self), locals())

	def add_NetconfServer(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of NetconfServer on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver.NetconfServer)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver import NetconfServer
		return self._create(NetconfServer(self), locals())

	def Ntpclock(self, AcceptNTPPacketswithCryptoNAK=None, Active=None, Count=None, DescriptiveName=None, IsParentV6=None, MaximumFrequencyTolerance=None, Mimimumsurvivorcount=None, Multiplier=None, Name=None, NtpServerCount=None, Precision=None, Status=None):
		"""Gets child instances of Ntpclock from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ntpclock will be returned.

		Args:
			AcceptNTPPacketswithCryptoNAK (bool): Accept NTP Packets with Crypto-NAK
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			IsParentV6 (bool): Parent v6
			MaximumFrequencyTolerance (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum frequency tolerance (ppm)
			Mimimumsurvivorcount (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum survivor count
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NtpServerCount (number): NTP server Count
			Precision (obj(ixnetwork_restpy.multivalue.Multivalue)): Precision(log2 seconds)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock.Ntpclock))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock import Ntpclock
		return self._select(Ntpclock(self), locals())

	def add_Ntpclock(self, AcceptNTPPacketswithCryptoNAK="False", ConnectedVia=None, IsParentV6="True", Multiplier="1", Name=None, NtpServerCount="1", StackedLayers=None):
		"""Adds a child instance of Ntpclock on the server.

		Args:
			AcceptNTPPacketswithCryptoNAK (bool): Accept NTP Packets with Crypto-NAK
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			IsParentV6 (bool): Parent v6
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NtpServerCount (number): NTP server Count
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock.Ntpclock)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock import Ntpclock
		return self._create(Ntpclock(self), locals())

	def OpenFlowController(self, AcceptUnconfiguredChannel=None, Active=None, AuxConnTimeout=None, AuxNonHelloStartupOption=None, BadVersionErrorAction=None, Count=None, DelFlowsAtStartup=None, DescriptiveName=None, DirectoryName=None, EchoInterval=None, EchoTimeOut=None, FeatRequestTimeout=None, FeatureRquestTimeoutAction=None, FileCaCertificate=None, FileCertificate=None, FilePrivKey=None, InstallFlowForLLDP=None, InstallLLDPFlow=None, LLDPDestinactionMac=None, LldpDstMacAddress=None, ModeOfConnection=None, Multiplier=None, Name=None, NumberOfChannels=None, PeriodicEcho=None, PeriodicLLDP=None, PeriodicLLDPInterval=None, ResponseTimeout=None, SendPortFeatureAtStartup=None, SetAsyncConfig=None, SetSwitchConfig=None, StartupEmptyTableFeatureRequest=None, StartupFeatureRequest=None, Status=None, TcpPort=None, TimeoutOption=None, TimeoutOptionValue=None, TlsVersion=None, TriggerLldp=None, TypeOfConnection=None, Version=None, VersionSupported=None):
		"""Gets child instances of OpenFlowController from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OpenFlowController will be returned.

		Args:
			AcceptUnconfiguredChannel (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, un-configured channels are accepted for this interface.
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuxConnTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The inactive time in milliseconds after which the auxiliary connection will timeout and close.
			AuxNonHelloStartupOption (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the action from the following options for non-hello message when connection is established. The options are: 1) Accept Connection 2) Return Error
			BadVersionErrorAction (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the action to be performed when an invalid version error occurs. The options are: 1) Re-send Hello 2) Terminate Connection
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DelFlowsAtStartup (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, Controller sends an OpenFlow delete message (for all wild card entries) at start-up. This deletes all existing flows in the DUT.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the Certificate and Key Files are available
			EchoInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The periodic interval in seconds at which the Interface sends Echo Request Packets.
			EchoTimeOut (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the echo request times out when they have been sent for a specified number of times, or when the time value specified has lapsed, but no response is received
			FeatRequestTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The inactive time in milliseconds after which the feature request will timeout.
			FeatureRquestTimeoutAction (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the action to be performed when a feature request times out. The options are: 1) Re-send Feature Request 2) Terminate Connection
			FileCaCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload a CA Certificate file for TLS session.
			FileCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload the certificate file for TLS session.
			FilePrivKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload the private key file for TLS session.
			InstallFlowForLLDP (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the controller sends add flow to each connected switch in such a way that each switch forwards LLDP packet to all other connected switches.
			InstallLLDPFlow (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LLDP Flow is installed.
			LLDPDestinactionMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the LLDP Destination MAC address.
			LldpDstMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The destination MAC Address for the LLDP packet.
			ModeOfConnection (obj(ixnetwork_restpy.multivalue.Multivalue)): The mode of connection used for the Interface. Options include: 1) Active 2) Passive 3) Mixed
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
			PeriodicEcho (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the Interface sends echo requests periodically to keep the OpenFlow session connected.
			PeriodicLLDP (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the interface sends LLDP packets periodically to discover new links.
			PeriodicLLDPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The periodic interval in milliseconds at which the Interface sends LLDP packets.
			ResponseTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The time in milliseconds after which the trigger request times out, if no response is received
			SendPortFeatureAtStartup (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, port Description request is sent when the connection is established
			SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
			SetSwitchConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
			StartupEmptyTableFeatureRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the Table Feature Request is sent at start up.
			StartupFeatureRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, port feature request is sent when the connection is established.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the TCP port for this interface
			TimeoutOption (obj(ixnetwork_restpy.multivalue.Multivalue)): The types of timeout options supported. Choose one of the following: 1) Multiplier 2) Timeout Value
			TimeoutOptionValue (obj(ixnetwork_restpy.multivalue.Multivalue)): The value specified for the selected Timeout option.
			TlsVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): TLS version selection
			TriggerLldp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LLDP is triggered
			TypeOfConnection (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of connection used for the Interface. Options include: 1) TCP 2) TLS
			Version (number): Implementation Version
			VersionSupported (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates the supported OpenFlow version number.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller.OpenFlowController))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller import OpenFlowController
		return self._select(OpenFlowController(self), locals())

	def add_OpenFlowController(self, ConnectedVia=None, Multiplier="1", Name=None, NumberOfChannels="1", SetAsyncConfig="False", SetSwitchConfig="False", StackedLayers=None):
		"""Adds a child instance of OpenFlowController on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
			SetAsyncConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
			SetSwitchConfig (bool): Un-checked state means getting the async config, Checked means setting asynchronous config with available parameters
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller.OpenFlowController)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller import OpenFlowController
		return self._create(OpenFlowController(self), locals())

	def OpenFlowSwitch(self, Active=None, AuxConnTimeout=None, AuxNonHelloStartupOption=None, BadVersionErrorAction=None, BandTypes=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, Capabilities=None, ControllerFlowTxRate=None, Count=None, DatapathDesc=None, DatapathId=None, DatapathIdHex=None, DescriptiveName=None, DirectoryName=None, EchoInterval=None, EchoTimeOut=None, EnableHelloElement=None, FileCaCertificate=None, FileCertificate=None, FilePrivKey=None, FlowRemovedMask=None, FlowRemovedMaskSlave=None, GroupCapabilities=None, GroupType=None, HardwareDesc=None, InterPacketInBurstGap=None, ManufacturerDesc=None, MaxBandPerMeter=None, MaxColorValue=None, MaxNumberOfBucketsPerGroups=None, MaxPacketInBytes=None, MeterCapabilities=None, Multiplier=None, Name=None, NumMeter=None, NumberOfBuffers=None, NumberOfChannels=None, NumberOfHostPorts=None, NumberOfPacketIn=None, NumberOfPorts=None, NumberOfTableRanges=None, NumberOfTopologyPorts=None, NumberOfUnconnectedPorts=None, PacketInMaskMaster=None, PacketInMaskSlave=None, PacketInReplyDelay=None, PacketInReplyTimeout=None, PacketInTxBurst=None, PacketOutRxRate=None, PeriodicEcho=None, PortStatusMaskMaster=None, PortStatusMaskSlave=None, SerialNumber=None, SoftwareDesc=None, Status=None, StoreFlows=None, SwitchDesc=None, TableMissAction=None, TcpPort=None, TimeoutOption=None, TimeoutOptionValue=None, TlsVersion=None, TransactionID=None, TypeOfConnection=None, VersionSupported=None):
		"""Gets child instances of OpenFlowSwitch from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OpenFlowSwitch will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AuxConnTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The inactive time in milliseconds after which the auxiliary connection will timeout and close.
			AuxNonHelloStartupOption (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the action from the following options for non-hello message when connection is established. The options are: 1) Accept Connection 2) Return Error
			BadVersionErrorAction (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the action to be performed when an invalid version error occurs. The options are: 1) Re-send Hello 2) Terminate Connection
			BandTypes (obj(ixnetwork_restpy.multivalue.Multivalue)): Select meter band types from the list
			BarrierReplyDelayType (obj(ixnetwork_restpy.multivalue.Multivalue)): Select the Barrier Reply Delay Type
			BarrierReplyMaxDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Barrier Reply Max Delay in milli seconds.
			Capabilities (obj(ixnetwork_restpy.multivalue.Multivalue)): Capabilities
			ControllerFlowTxRate (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, statistics is published showing the rate at which Flows are transmitted per second, by the Controller
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DatapathDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): The description of the Data Path used.
			DatapathId (obj(ixnetwork_restpy.multivalue.Multivalue)): The Datapath ID of the OF Channel.
			DatapathIdHex (obj(ixnetwork_restpy.multivalue.Multivalue)): The Datapath ID in Hex of the OF Channel.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the Certificate and Key Files are available
			EchoInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The periodic interval in seconds at which the Interface sends Echo Request Packets.
			EchoTimeOut (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the echo request times out when they have been sent for a specified number of times, or when the time value specified has lapsed, but no response is received
			EnableHelloElement (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Element
			FileCaCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload a CA Certificate file for TLS session.
			FileCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload the certificate file for TLS session.
			FilePrivKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Browse and upload the private key file for TLS session.
			FlowRemovedMask (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the flow removed message types that will not be received when the controller has the Master role
			FlowRemovedMaskSlave (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the flow removed message types that will not be received when the controller has the Slave role
			GroupCapabilities (obj(ixnetwork_restpy.multivalue.Multivalue)): Group configuration flags: Weight:Support weight for select groups. Liveness:Support liveness for select groups. Chaining:Support chaining groups. Check Loops:Check chaining for loops and delete.
			GroupType (obj(ixnetwork_restpy.multivalue.Multivalue)): Can be of the following types per switch: 1)All: Execute all buckets in the group. 2)Select:Execute one bucket in the group. 3)Indirect:Execute the one defined bucket in this group. 4)Fast Failover:Execute the first live bucket.
			HardwareDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): The description of the hardware used.
			InterPacketInBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the duration (in milliseconds) for which the switch waits between successive packet-in bursts.The default value is 1,000 milliseconds.
			ManufacturerDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): The description of the manufacturer. The default value is Ixia.
			MaxBandPerMeter (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of bands per meter
			MaxColorValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Color Value
			MaxNumberOfBucketsPerGroups (obj(ixnetwork_restpy.multivalue.Multivalue)): To specify the maximum number of group buckets each group can have.
			MaxPacketInBytes (obj(ixnetwork_restpy.multivalue.Multivalue)): The maximum length of the Packet-in messages in bytes.
			MeterCapabilities (obj(ixnetwork_restpy.multivalue.Multivalue)): Select meter capabilities from the list
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumMeter (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of Openflow meters configured for the switch
			NumberOfBuffers (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the maximum number of packets the switch can buffer when sending packets to the controller using packet-in messages.
			NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
			NumberOfHostPorts (number): Number of Host Ports per Switch
			NumberOfPacketIn (number): Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
			NumberOfPorts (number): Number of Ports per Switch
			NumberOfTableRanges (number): Number of Tables per Switch
			NumberOfTopologyPorts (number): Number of Topology Ports per Switch
			NumberOfUnconnectedPorts (number): Number of Unconnected Ports per Switch
			PacketInMaskMaster (obj(ixnetwork_restpy.multivalue.Multivalue)): Packet In Mask Master
			PacketInMaskSlave (obj(ixnetwork_restpy.multivalue.Multivalue)): Packet In Mask Slave
			PacketInReplyDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, delay between packet-in and the corresponding packet-out or flow mod is published.
			PacketInReplyTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The amount of time, in seconds, that the switch keeps the packet-in message in buffer, if it does not receive any corresponding packet-out or flow mod.
			PacketInTxBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the number of packet-in transmitting packets that can be sent in a single burst within the time frame specified by the Inter PacketIn Burst Gap value.
			PacketOutRxRate (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, packet_out rx rate and packet_in tx rate is calculated for the switch.
			PeriodicEcho (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the Interface sends echo requests periodically to keep the OpenFlow session connected.
			PortStatusMaskMaster (obj(ixnetwork_restpy.multivalue.Multivalue)): Port Status Mask Master
			PortStatusMaskSlave (obj(ixnetwork_restpy.multivalue.Multivalue)): Port Status Mask Slave
			SerialNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): The serial number used.
			SoftwareDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): The description of the software used.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			StoreFlows (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the flow information sent by the Controller are learned by the Switch.
			SwitchDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): A description of the Switch
			TableMissAction (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify what the Switch should do when there is no match for the packets
			TcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the TCP port for this interface
			TimeoutOption (obj(ixnetwork_restpy.multivalue.Multivalue)): The types of timeout options supported. Choose one of the following: 1) Multiplier 2) Timeout Value
			TimeoutOptionValue (obj(ixnetwork_restpy.multivalue.Multivalue)): The value specified for the selected Timeout option.
			TlsVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): TLS version selection
			TransactionID (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, PacketIn Delay Calculation will be done by matching transaction ID
			TypeOfConnection (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of connection used for the Interface. Options include: 1) TCP 2) TLS
			VersionSupported (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates the supported OpenFlow version number.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch.OpenFlowSwitch))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch import OpenFlowSwitch
		return self._select(OpenFlowSwitch(self), locals())

	def add_OpenFlowSwitch(self, ConnectedVia=None, Multiplier="1", Name=None, NumberOfChannels="1", NumberOfPacketIn="0", NumberOfTableRanges="2", NumberOfUnconnectedPorts="1", StackedLayers=None):
		"""Adds a child instance of OpenFlowSwitch on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
			NumberOfPacketIn (number): Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
			NumberOfTableRanges (number): Number of Tables per Switch
			NumberOfUnconnectedPorts (number): Number of Unconnected Ports per Switch
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch.OpenFlowSwitch)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch import OpenFlowSwitch
		return self._create(OpenFlowSwitch(self), locals())

	def Ospfv2(self, Active=None, AdjSID=None, AreaId=None, AreaIdIp=None, Authentication=None, AuthenticationPassword=None, BFlag=None, Count=None, DeadInterval=None, Dedicated1Plus1=None, Dedicated1To1=None, DemandCircuit=None, DescriptiveName=None, EnLinkProtection=None, EnableAdjSID=None, EnableBfdRegistration=None, EnableFast2wayConvergence=None, EnableFastHello=None, EnableSRLG=None, Enhanced=None, ExternalAttribute=None, ExternalCapability=None, ExtraTraffic=None, HelloInterval=None, HelloMultiplier=None, LFlag=None, MaxMtu=None, Md5Key=None, Md5KeyId=None, Metric=None, MulticastCapability=None, Multiplier=None, Name=None, NeighborIp=None, NetworkType=None, NssaCapability=None, OpaqueLsaForwarded=None, Priority=None, Reserved40=None, Reserved80=None, SFlag=None, Shared=None, SrlgCount=None, Status=None, SuppressHello=None, TypeAreaId=None, TypeOfServiceRouting=None, Unprotected=None, Unused=None, VFlag=None, ValidateRxMtu=None, Weight=None):
		"""Gets child instances of Ospfv2 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv2 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Adjacency SID
			AreaId (obj(ixnetwork_restpy.multivalue.Multivalue)): OSPF Area ID for a non-connected interface, displayed in Interger format
			AreaIdIp (obj(ixnetwork_restpy.multivalue.Multivalue)): OSPF Area ID for a non-connected interface, displayed in IP Address format
			Authentication (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication
			AuthenticationPassword (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Password
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Backup Flag
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Dead Interval
			Dedicated1Plus1 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
			Dedicated1To1 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
			DemandCircuit (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 7
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnLinkProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the link protection on the OSPF link between two mentioned interfaces.
			EnableAdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Adj SID
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableFast2wayConvergence (bool): Enable 2-way Adj Fast Convergence
			EnableFastHello (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Fast Hello
			EnableSRLG (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the SRLG on the OSPF link between two mentioned interfaces.
			Enhanced (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
			ExternalAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 4
			ExternalCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 1
			ExtraTraffic (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Interval
			HelloMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Multiplier
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local/Global Flag
			MaxMtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Max MTU Value
			Md5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): MD5 Key
			Md5KeyId (obj(ixnetwork_restpy.multivalue.Multivalue)): MD5 Key ID
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Routing Metric
			MulticastCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 2
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NeighborIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Neighbor IP when connected network is Point to Multipoint
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			NssaCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 3
			OpaqueLsaForwarded (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 6
			Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): Priority (when DR/BDR)
			Reserved40 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x40.
			Reserved80 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x80.
			SFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Flag
			Shared (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SuppressHello (obj(ixnetwork_restpy.multivalue.Multivalue)): Suppress Hello for BGP-LS
			TypeAreaId (obj(ixnetwork_restpy.multivalue.Multivalue)): Area ID Type
			TypeOfServiceRouting (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 0
			Unprotected (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
			Unused (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 7
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value/Index Flag
			ValidateRxMtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Validate Received MTU
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2.Ospfv2))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2 import Ospfv2
		return self._select(Ospfv2(self), locals())

	def add_Ospfv2(self, ConnectedVia=None, EnableFast2wayConvergence="True", Multiplier="1", Name=None, SrlgCount="1", StackedLayers=None):
		"""Adds a child instance of Ospfv2 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableFast2wayConvergence (bool): Enable 2-way Adj Fast Convergence
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2.Ospfv2)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2 import Ospfv2
		return self._create(Ospfv2(self), locals())

	def Ovsdbcontroller(self, ClearDumpDbFiles=None, ConnectionType=None, ControllerTcpPort=None, Count=None, DescriptiveName=None, DirectoryName=None, DumpdbDirectoryName=None, EnableLogging=None, EnableOvsdbServerIp=None, ErrorCode=None, ErrorDesc=None, ErrorLogDirectoryName=None, ErrorLogicalSwitchName=None, ErrorPhysicalSwitchName=None, ErrorTimeStamp=None, FileCaCertificate=None, FileCertificate=None, FileHWGatewayCertificate=None, FilePrivKey=None, HSCConfiguration=None, LatestDumpDbFileNames=None, LatestErrorFileNames=None, Multiplier=None, Name=None, OvsdbSchema=None, OvsdbServerIp=None, PseudoConnectedTo=None, PseudoConnectedToBfd=None, PseudoConnectedToVxlanReplicator=None, PseudoMultiplier=None, PseudoMultiplierBfd=None, PseudoMultiplierVxlanReplicator=None, ServerAddDeleteConnectionError=None, ServerAddDeleteStatus=None, ServerConnectionIp=None, Status=None, TableNames=None, TimeOut=None, VerifyHWGatewayCertificate=None, VerifyPeerCertificate=None, Vxlan=None, VxlanReplicator=None):
		"""Gets child instances of Ovsdbcontroller from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ovsdbcontroller will be returned.

		Args:
			ClearDumpDbFiles (obj(ixnetwork_restpy.multivalue.Multivalue)): 
			ConnectionType (obj(ixnetwork_restpy.multivalue.Multivalue)): Connection should use TCP or TLS
			ControllerTcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the TCP port for the Controller
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the Certificate and Key Files are available
			DumpdbDirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the DumpDb Files are available
			EnableLogging (bool): If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
			EnableOvsdbServerIp (obj(ixnetwork_restpy.multivalue.Multivalue)): 
			ErrorCode (obj(ixnetwork_restpy.multivalue.Multivalue)): Error Code
			ErrorDesc (obj(ixnetwork_restpy.multivalue.Multivalue)): Description of Error occured
			ErrorLogDirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the ErrorLog Files are available
			ErrorLogicalSwitchName (obj(ixnetwork_restpy.multivalue.Multivalue)): Error occured for this Logical Switch Name
			ErrorPhysicalSwitchName (obj(ixnetwork_restpy.multivalue.Multivalue)): Error occured for this Physical Switch Name
			ErrorTimeStamp (obj(ixnetwork_restpy.multivalue.Multivalue)): Time Stamp at which Last Error occurred
			FileCaCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): CA Certificate File
			FileCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Certificate File
			FileHWGatewayCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): HW Gateway Certificate File
			FilePrivKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Private Key File
			HSCConfiguration (obj(ixnetwork_restpy.multivalue.Multivalue)): Each VTEP has its own Hardware Switch Controller.
			LatestDumpDbFileNames (str): Api to fetch latest DumpDb Files
			LatestErrorFileNames (str): Api to fetch latest Error Files
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OvsdbSchema (obj(ixnetwork_restpy.multivalue.Multivalue)): Database schema
			OvsdbServerIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The IP address of the DUT or Ovs Server.
			PseudoConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoConnectedToBfd (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoConnectedToVxlanReplicator (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoMultiplier (number): Multiplier for GUI-only connection
			PseudoMultiplierBfd (number): Multiplier for GUI-only connection
			PseudoMultiplierVxlanReplicator (number): Multiplier for GUI-only connection
			ServerAddDeleteConnectionError (str): API to retrieve error occured while Adding/ Deleting Server
			ServerAddDeleteStatus (str): Status of all servers Added/Deleted to Controller. Use Get Server Add/Delete Status, right click action to get current status
			ServerConnectionIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The IP address of the DUT or Ovs Server which needs to be Added/Deleted.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TableNames (obj(ixnetwork_restpy.multivalue.Multivalue)): 
			TimeOut (number): Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
			VerifyHWGatewayCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Verify HW Gateway Certificate
			VerifyPeerCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Verify Peer Certificate
			Vxlan (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 
			VxlanReplicator (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller.Ovsdbcontroller))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller import Ovsdbcontroller
		return self._select(Ovsdbcontroller(self), locals())

	def add_Ovsdbcontroller(self, ConnectedVia=None, EnableLogging="False", LatestDumpDbFileNames=None, LatestErrorFileNames=None, Multiplier="1", Name=None, PseudoConnectedTo=None, PseudoConnectedToBfd=None, PseudoConnectedToVxlanReplicator=None, ServerAddDeleteConnectionError=None, StackedLayers=None, TimeOut="1000", Vxlan=None, VxlanReplicator=None):
		"""Adds a child instance of Ovsdbcontroller on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableLogging (bool): If true, Port debug logs will be recorded, Maximum recording will be upto 500 MB .
			LatestDumpDbFileNames (str): Api to fetch latest DumpDb Files
			LatestErrorFileNames (str): Api to fetch latest Error Files
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PseudoConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoConnectedToBfd (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoConnectedToVxlanReplicator (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			ServerAddDeleteConnectionError (str): API to retrieve error occured while Adding/ Deleting Server
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TimeOut (number): Transact request Time Out in seconds. For scale scenarios increase this Timeout value.
			Vxlan (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 
			VxlanReplicator (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller.Ovsdbcontroller)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller import Ovsdbcontroller
		return self._create(Ovsdbcontroller(self), locals())

	def Ovsdbserver(self, ConnectionType=None, Count=None, DescriptiveName=None, DirectoryName=None, FileCaCertificate=None, FileCertificate=None, FilePrivKey=None, ManagerCount=None, Multiplier=None, Name=None, OvsdbSchema=None, PseudoConnectedTo=None, PseudoMultiplier=None, ServerTcpPort=None, Status=None, Vxlan=None):
		"""Gets child instances of Ovsdbserver from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ovsdbserver will be returned.

		Args:
			ConnectionType (obj(ixnetwork_restpy.multivalue.Multivalue)): Connection should use TCP or TLS
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DirectoryName (obj(ixnetwork_restpy.multivalue.Multivalue)): Location of Directory in Client where the Certificate and Key Files are available
			FileCaCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): CA Certificate File
			FileCertificate (obj(ixnetwork_restpy.multivalue.Multivalue)): Certificate File
			FilePrivKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Private Key File
			ManagerCount (number): Number of Managers the OVSDB Server will initiate connections to
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OvsdbSchema (obj(ixnetwork_restpy.multivalue.Multivalue)): Database schema
			PseudoConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			PseudoMultiplier (number): Multiplier for GUI-only connection
			ServerTcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): Specify the TCP port for the Server
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			Vxlan (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver.Ovsdbserver))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver import Ovsdbserver
		return self._select(Ovsdbserver(self), locals())

	def add_Ovsdbserver(self, ConnectedVia=None, ManagerCount="0", Multiplier="1", Name=None, PseudoConnectedTo=None, StackedLayers=None, Vxlan=None):
		"""Adds a child instance of Ovsdbserver on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ManagerCount (number): Number of Managers the OVSDB Server will initiate connections to
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PseudoConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): GUI-only connection
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			Vxlan (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver.Ovsdbserver)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver import Ovsdbserver
		return self._create(Ovsdbserver(self), locals())

	def Pcc(self, Active=None, Active_pre_established_lsps=None, Authentication=None, BurstInterval=None, Count=None, DeadInterval=None, DescriptiveName=None, ErrorValue=None, ExpectedInitiatedLspsForTraffic=None, KeepaliveInterval=None, MD5Key=None, MaxLspsPerPcRpt=None, MaxReconnectInterval=None, MaxRequestedLspPerInterval=None, MaxSyncLspPerInterval=None, MaximumSidDepth=None, Multiplier=None, Name=None, NumberOfBackupPCEs=None, PccPpagTLVType=None, PceIpv4Address=None, PreEstablishedSrLspsPerPcc=None, RateControl=None, ReconnectInterval=None, RequestedLspsPerPcc=None, ReturnInstantiationError=None, SrPceCapability=None, StateTimeoutInterval=None, Status=None, TcpPort=None):
		"""Gets child instances of Pcc from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Pcc will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Active_pre_established_lsps (number): 
			Authentication (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of cryptographic authentication to be used on this link interface
			BurstInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Interval in milisecond in which desired rate of messages needs to be maintained.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the time interval, after the expiration of which, a PCEP peer declares the session down if no PCEP message has been received.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ErrorValue (obj(ixnetwork_restpy.multivalue.Multivalue)): To configure the type of error. Editable only if Return Instantiation Error is enabled.
			ExpectedInitiatedLspsForTraffic (number): Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
			KeepaliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Frequency/Time Interval of sending PCEP messages to keep the session active.
			MD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): A value to be used as the secret MD5 Key.
			MaxLspsPerPcRpt (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls the maximum LSP information that can be present in a Path report message when the session is stateful session.
			MaxReconnectInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the maximum time interval, by which recoonect timer will be increased upto.
			MaxRequestedLspPerInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of LSP computation request messages can be sent per interval.
			MaxSyncLspPerInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of LSP sync can be sent per interval.
			MaximumSidDepth (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum SID Depth field (MSD) specifies the maximum number of SIDs that a PCC is capable of imposing on a packet. Editable only if SR PCE Capability is enabled.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfBackupPCEs (number): Number of Backup PCEs
			PccPpagTLVType (obj(ixnetwork_restpy.multivalue.Multivalue)): PPAG TLV Type specifies PCC's capability of interpreting this type of PPAG TLV
			PceIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 address of the PCE. This column is greyed out in case of PCCv6.
			PreEstablishedSrLspsPerPcc (number): Pre-Established SR LSPs per PCC
			RateControl (obj(ixnetwork_restpy.multivalue.Multivalue)): The rate control is an optional feature associated with PCE initiated LSP.
			ReconnectInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the time interval, after the expiration of which, retry to establish the broken session by PCC happen.
			RequestedLspsPerPcc (number): Requested LSPs per PCC
			ReturnInstantiationError (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, then PCC will reply PCErr upon receiving PCInitiate message.
			SrPceCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): The SR PCE Capability TLV is an optional TLV associated with the OPEN Object to exchange SR capability of PCEP speakers.
			StateTimeoutInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the time interval, after the expiration of which, LSP is cleaned up by PCC.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): PCEP operates over TCP using a registered TCP port (default - 4189). This allows the requirements of reliable messaging and flow control to bemet without further protocol work. This control can be configured when user does not want to use the default one.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc.Pcc))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc import Pcc
		return self._select(Pcc(self), locals())

	def add_Pcc(self, Active_pre_established_lsps="0", ConnectedVia=None, ExpectedInitiatedLspsForTraffic="0", Multiplier="1", Name=None, NumberOfBackupPCEs="0", PreEstablishedSrLspsPerPcc="0", RequestedLspsPerPcc="0", StackedLayers=None):
		"""Adds a child instance of Pcc on the server.

		Args:
			Active_pre_established_lsps (number): 
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ExpectedInitiatedLspsForTraffic (number): Based on the value in this control the number of Expected Initiated LSPs for Traffic can be configured. This is used for traffic only.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfBackupPCEs (number): Number of Backup PCEs
			PreEstablishedSrLspsPerPcc (number): Pre-Established SR LSPs per PCC
			RequestedLspsPerPcc (number): Requested LSPs per PCC
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc.Pcc)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc import Pcc
		return self._create(Pcc(self), locals())

	def Pce(self, Active=None, Count=None, DescriptiveName=None, MaxPendingConnection=None, MaxUnknownMessage=None, MaxUnknownRequest=None, Multiplier=None, Name=None, PceActionMode=None, Status=None, TcpPort=None):
		"""Gets child instances of Pce from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Pce will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			MaxPendingConnection (obj(ixnetwork_restpy.multivalue.Multivalue)): This control allows the user to configure the maximum number of pending connections that an IXIA PCE controller will process concurrently.
			MaxUnknownMessage (obj(ixnetwork_restpy.multivalue.Multivalue)): This control allows the user to configure the maximum number of unknown messages that PCE will receive before closing the session. If the PCE receives unrecognized messages at a rate equal or greater than this value per minute, the PCE MUST send a PCEP CLOSE message with this as the close value. The PCE MUST close the TCP session and MUST NOT send any further PCEP messages on the PCEP session.
			MaxUnknownRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): This control allows the user to configure the maximum number of unknown requests that PCE will receive before closing the session. If the PCE receives PCRep/ PCReq messages with unknown requests at a rate equal or greater than this value per minute, the PCE MUST send a PCEP CLOSE message with this as the close value. The PCE MUST close the TCP session and MUST NOT send any further PCEP messages on the PCEP session.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PceActionMode (str(none|reset|rsvpPcInitiate|rsvpPcrep|rsvpPcupd|srPcrep)): PCE Mode of Action
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TcpPort (obj(ixnetwork_restpy.multivalue.Multivalue)): PCEP operates over TCP using a registered TCP port (default - 4189). This allows the requirements of reliable messaging and flow control to be met without further protocol work. This control can be configured when user does not want to use the default one.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce.Pce))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce import Pce
		return self._select(Pce(self), locals())

	def add_Pce(self, ConnectedVia=None, Multiplier="1", Name=None, PceActionMode="none", StackedLayers=None):
		"""Adds a child instance of Pce on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PceActionMode (str(none|reset|rsvpPcInitiate|rsvpPcrep|rsvpPcupd|srPcrep)): PCE Mode of Action
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce.Pce)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce import Pce
		return self._create(Pce(self), locals())

	def PimV4Interface(self, Active=None, AutoPickNeighbor=None, BootstrapHashMaskLength=None, BootstrapInterval=None, BootstrapPriority=None, BootstrapTimeout=None, Count=None, CrpRanges=None, DescriptiveName=None, DisableTriggered=None, DiscardLearnedRpInfo=None, EnableBfdRegistration=None, EnableBootstrap=None, EnablePrune=None, ForceSemantic=None, HelloHoldTime=None, HelloInterval=None, JoinPrunes=None, LanPruneTbit=None, LearnSelectedRpSet=None, Multiplier=None, Name=None, OverrideInterval=None, PruneDelay=None, SendBidirectional=None, SendGenerationIdOption=None, SendGenerationMode=None, Sources=None, Status=None, SupportUnicastBsm=None, TriggeredHelloDelay=None, V4Neighbor=None):
		"""Gets child instances of PimV4Interface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PimV4Interface will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AutoPickNeighbor (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the time-saving Auto Pick feature is enabled-and the Upstream Neighbor field is not available for use. The Upstream Neighbor address used in the Join/Prune message is determined automatically from received Hello messages. The first time a Hello message is received-containing a Source (link-local) address that does not belong to this interface, that source address will be used as the Upstream Neighbor address. If not selected, the user can type in the link-local address in the Upstream Neighbor IP field (see Neighbor field below)-to be used for the upstream neighbor address field in the Join/Prune message.
			BootstrapHashMaskLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Hash Mask Length of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
			BootstrapInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The time interval (in seconds) between two consecutive bootstrap messages sent by the BSR.
			BootstrapPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Priority of the Bootstrap Router (BSR) that is set with the same name in all Bootstrap Messages sent by this BSR.
			BootstrapTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Amount of time (in seconds) of not receiving any Bootstrap Messages, after which, the BSR if candidate at that point of time will decide that the currently elected BSR has gone down and will restart BSR election procedure.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CrpRanges (number): Number of C-RP Ranges
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DisableTriggered (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, the triggered hello delay function is disabled.
			DiscardLearnedRpInfo (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, disregards group mappings learnt from Bootstrap Message (in case not acting as elected BSR) or from Candidate RP Advertisement (in case of elected BSR).
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableBootstrap (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, enables the PIM-SM interface to participate in Bootstrap Router election procedure.
			EnablePrune (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the LAN Prune (propagation) Delay is enabled for this PIM-SM interface. (This Indicates that this option is present in the Hello message.)
			ForceSemantic (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, this forces the BSR to send only one group specific RP list per bootstrap message, even if there is space in the packet to push in more RP list information pertaining to a different group.
			HelloHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The timeout period in seconds specified in Hello messages. It is the length of time the receiver of this message must keep the neighbor reachable. The default is 3.5 times the Hello Interval (105 seconds).
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The PIM-SM Hello Interval is the length of time in seconds between the transmissions of Hello messages. The default is 30 seconds.
			JoinPrunes (number): Number of Join/Prunes
			LanPruneTbit (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, the T flag bit in the LAN Prune Delay option of the Hello message is set (= 1). Setting this bit specifies that the sending PIM-SM router has the ability to disable Join message suppression
			LearnSelectedRpSet (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, displays the best RP per group (member of selected RP set).
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OverrideInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): (in ms) The delay interval for randomizing the transmission time for override messages-when scheduling a delayed Join message. The default value is 2,500 milliseconds (ms). The valid range is 100 to 7FFF msec. (This is part of the LAN Prune Delay option included in Hello messages).
			PruneDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): (in ms) The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface. The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
			SendBidirectional (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, sets the bi-directional PIM-SM flag bit (= 1), per IETF DRAFT draft-ietf-pim-bidir-04. (Note: Designated Forwarder election is not currently supported.)
			SendGenerationIdOption (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, enables the Send Generation ID Option, and the Generation ID Mode field will become available to make a mode selection.
			SendGenerationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The mode for creating the 32-bit value for the Generation Identifier (GenID) option in the Hello message. A new GenID is created each time an interface (or router) starts or restarts PIM-SM forwarding. A change in this value indicates to the neighbor(s) that a change of state may have occurred, and that the old PIM-SM states information received from those interfaces should be discarded. Choose one of: Incremental-the GenID increases by 1 for each successive Hello Message sent from this emulated PIM-SM router. Random-each Hello message sent from this emulated PIM-SM router will have a randomly-generated GenID. Constant (the default)-the GenID remains the same in all of the Hello Messages sent from this emulated. PIM-SM router.
			Sources (number): Number of Sources
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportUnicastBsm (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, this supports the sending and processing of Unicast bootstrap messages.
			TriggeredHelloDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.
			V4Neighbor (obj(ixnetwork_restpy.multivalue.Multivalue)): (Auto Pick Neighbor must be disabled/not selected to make this field active) The user can manually type in the link-local address to be used for the Upstream Neighbor address field in the Join/Prune message.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface.PimV4Interface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface import PimV4Interface
		return self._select(PimV4Interface(self), locals())

	def add_PimV4Interface(self, ConnectedVia=None, CrpRanges="0", JoinPrunes="0", Multiplier="1", Name=None, Sources="0", StackedLayers=None):
		"""Adds a child instance of PimV4Interface on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CrpRanges (number): Number of C-RP Ranges
			JoinPrunes (number): Number of Join/Prunes
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Sources (number): Number of Sources
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface.PimV4Interface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface import PimV4Interface
		return self._create(PimV4Interface(self), locals())

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

	def RsvpteIf(self, Active=None, ActualRestartTime=None, AdvertisedRestartTime=None, AuthenticationAlgorithm=None, AuthenticationKeyForReceivedPackets=None, AuthenticationKeyForSentPackets=None, AuthenticationKeyIdentifier=None, AutoGenerateAuthenticationKeyIdentifier=None, BundleMessageThresholdTime=None, CheckIntegrityForReceivedPackets=None, Count=None, DescriptiveName=None, DutIp=None, EnableBfdRegistration=None, EnableBundleMessageSending=None, EnableBundleMessageThresholdTimer=None, EnableGracefulRestartHelperMode=None, EnableGracefulRestartRestartingMode=None, EnableHelloExtension=None, EnableRefreshReduction=None, GenerateSequenceNumberBasedOnRealTime=None, HandshakeRequired=None, HelloInterval=None, HelloTimeoutMultiplier=None, InitialSequenceNumber=None, LabelReqRefCount=None, LabelSpaceEnd=None, LabelSpaceStart=None, Multiplier=None, Name=None, NumberOfRestarts=None, RecoveryTime=None, RestartStartTime=None, RestartUpTime=None, Status=None, SummaryRefreshInterval=None, UseSameAuthenticationKeyForPeer=None, UsingGatewayIp=None):
		"""Gets child instances of RsvpteIf from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RsvpteIf will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ActualRestartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Actual Restart Time (ms)
			AdvertisedRestartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertised Restart Time (ms)
			AuthenticationAlgorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Algorithm
			AuthenticationKeyForReceivedPackets (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Key for Received Packets
			AuthenticationKeyForSentPackets (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Key for Sent Packets
			AuthenticationKeyIdentifier (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Key Identifier
			AutoGenerateAuthenticationKeyIdentifier (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Generate Authentication Key Identifier
			BundleMessageThresholdTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Bundle Message Threshold Time (ms)
			CheckIntegrityForReceivedPackets (obj(ixnetwork_restpy.multivalue.Multivalue)): Check Integrity for Received Packets
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DutIp (obj(ixnetwork_restpy.multivalue.Multivalue)): DUT IP
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableBundleMessageSending (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Bundle Message Sending
			EnableBundleMessageThresholdTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Bundle Message Threshold Timer
			EnableGracefulRestartHelperMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Helper-Mode
			EnableGracefulRestartRestartingMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Restarting-Mode
			EnableHelloExtension (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Extension
			EnableRefreshReduction (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Refresh Reduction
			GenerateSequenceNumberBasedOnRealTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Generate Sequence Number Based on Real Time
			HandshakeRequired (obj(ixnetwork_restpy.multivalue.Multivalue)): Handshake Required
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Interval (ms)
			HelloTimeoutMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Timeout Multiplier
			InitialSequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Initial Sequence Number
			LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
			LabelSpaceEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Space End
			LabelSpaceStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Space Start
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfRestarts (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of Restarts
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Recovery Time (ms)
			RestartStartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Start Time (ms)
			RestartUpTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Up Time (ms)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SummaryRefreshInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Summary Refresh Interval (ms)
			UseSameAuthenticationKeyForPeer (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Same Authentication Key for Peer
			UsingGatewayIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Using Gateway IP

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif.RsvpteIf))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif import RsvpteIf
		return self._select(RsvpteIf(self), locals())

	def add_RsvpteIf(self, ConnectedVia=None, LabelReqRefCount="0", Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of RsvpteIf on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LabelReqRefCount (number): Number of Label Req in RSVP-TE DG
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif.RsvpteIf)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif import RsvpteIf
		return self._create(RsvpteIf(self), locals())

	def RsvpteLsps(self, Active=None, Count=None, DescriptiveName=None, EnableP2PEgress=None, ExpectedPceInitiatedLspsCount=None, IngressP2PLsps=None, Multiplier=None, Name=None, P2mpEgressTunnelCount=None, P2mpIngressLspCount=None, Status=None):
		"""Gets child instances of RsvpteLsps from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RsvpteLsps will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
			ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
			IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
			P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps.RsvpteLsps))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps import RsvpteLsps
		return self._select(RsvpteLsps(self), locals())

	def add_RsvpteLsps(self, ConnectedVia=None, EnableP2PEgress="True", ExpectedPceInitiatedLspsCount="0", IngressP2PLsps="1", Multiplier="1", Name=None, P2mpEgressTunnelCount="0", P2mpIngressLspCount="0", StackedLayers=None):
		"""Adds a child instance of RsvpteLsps on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
			ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
			IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
			P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps.RsvpteLsps)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps import RsvpteLsps
		return self._create(RsvpteLsps(self), locals())

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

	def Vxlan(self, Count=None, DescriptiveName=None, EnableStaticInfo=None, ExternalLearning=None, Ipv4_multicast=None, Multiplier=None, Name=None, OvsdbConnectorMultiplier=None, RunningMode=None, StaticInfoCount=None, Status=None, Vni=None):
		"""Gets child instances of Vxlan from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Vxlan will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
			ExternalLearning (bool): If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
			Ipv4_multicast (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Multicast Address.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OvsdbConnectorMultiplier (number): Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
			RunningMode (str(none|ovsdbControllerBfdStack|ovsdbStack)): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
			StaticInfoCount (number): number of unicast VTEP
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			Vni (obj(ixnetwork_restpy.multivalue.Multivalue)): VXLAN Network Identifier.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan.Vxlan))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan import Vxlan
		return self._select(Vxlan(self), locals())

	def add_Vxlan(self, ConnectedVia=None, EnableStaticInfo="False", ExternalLearning="False", Multiplier="1", Name=None, OvsdbConnectorMultiplier="1", RunningMode="none", StackedLayers=None, StaticInfoCount="1"):
		"""Adds a child instance of Vxlan on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableStaticInfo (bool): If true, VXLAN will use unicast entries for VTEP information instead of multicast learning.
			ExternalLearning (bool): If true, VXLAN will use information received from another protocol which will handle the learning mechanism.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OvsdbConnectorMultiplier (number): Ovsdb to Vxlan multiplier, when part of OVSDB Server stack.
			RunningMode (str(none|ovsdbControllerBfdStack|ovsdbStack)): There will be different behaviours based on role (normal=0, ovsdb controller stack=1, bfd stack=2.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StaticInfoCount (number): number of unicast VTEP

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan.Vxlan)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan import Vxlan
		return self._create(Vxlan(self), locals())

	@property
	def Address(self):
		"""IPv4 addresses of the devices

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('address')

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
	def GatewayIp(self):
		"""IPv4 addresses of the Gateways for the devices

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('gatewayIp')

	@property
	def ManualGatewayMac(self):
		"""User specified Gateway MAC addresses

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('manualGatewayMac')

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
	def Prefix(self):
		"""The length (in bits) of the mask to be used in conjunction with all the addresses created in the range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefix')

	@property
	def ResolveGateway(self):
		"""Enables the gateway MAC address discovery.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('resolveGateway')

	@property
	def ResolvedGatewayMac(self):
		"""The resolved gateway's MAC addresses

		Returns:
			list(str)
		"""
		return self._get_attribute('resolvedGatewayMac')

	@property
	def SessionInfo(self):
		"""Logs additional information about the session state.

		Returns:
			list(str[interfaceRemoved|none|resolveMacFailed])
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

	def remove(self):
		"""Deletes a child instance of Ipv4 on the server.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def SendArp(self, Arg1):
		"""Executes the sendArp operation on the server.

		Send ARP request to configured gateway IP to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendArp', payload=locals(), response_object=None)

	def SendArp(self, Arg1, SessionIndices):
		"""Executes the sendArp operation on the server.

		Send ARP request to configured gateway IP to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendArp', payload=locals(), response_object=None)

	def SendArp(self, Arg1, SessionIndices):
		"""Executes the sendArp operation on the server.

		Send ARP request to configured gateway IP to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendArp', payload=locals(), response_object=None)

	def SendArpManual(self, DestIP):
		"""Executes the sendArpManual operation on the server.

		Send ARP request to specified IP for selected IPv4 items.

		Args:
			DestIP (str): This parameter requires a destIP of type kString

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendArpManual', payload=locals(), response_object=None)

	def SendArpManual(self, DestIP, SessionIndices):
		"""Executes the sendArpManual operation on the server.

		Send ARP request to specified IP for selected IPv4 items.

		Args:
			DestIP (str): This parameter requires a destIP of type kString
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendArpManual', payload=locals(), response_object=None)

	def SendArpManual(self, SessionIndices, DestIP):
		"""Executes the sendArpManual operation on the server.

		Send ARP request to specified IP for selected IPv4 items.

		Args:
			SessionIndices (str): This parameter requires a destIP of type kString
			DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendArpManual', payload=locals(), response_object=None)

	def SendPing(self, DestIP):
		"""Executes the sendPing operation on the server.

		Send ping for selected IPv4 items.

		Args:
			DestIP (str): This parameter requires a destIP of type kString

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendPing', payload=locals(), response_object=None)

	def SendPing(self, DestIP, SessionIndices):
		"""Executes the sendPing operation on the server.

		Send ping for selected IPv4 items.

		Args:
			DestIP (str): This parameter requires a destIP of type kString
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendPing', payload=locals(), response_object=None)

	def SendPing(self, SessionIndices, DestIP):
		"""Executes the sendPing operation on the server.

		Send ping for selected IPv4 items.

		Args:
			SessionIndices (str): This parameter requires a destIP of type kString
			DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendPing', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
