from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Pppoxserver(Base):
	"""PPPoX Server
	"""

	_SDM_NAME = 'pppoxserver'

	def __init__(self, parent):
		super(Pppoxserver, self).__init__(parent)

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

	def Bfdv6Interface(self, Active=None, AggregateBfdSession=None, ConfigureEchoSourceIp=None, Count=None, DescriptiveName=None, EchoRxInterval=None, EchoTimeOut=None, EchoTxInterval=None, EnableControlPlaneIndependent=None, EnableDemandMode=None, FlapTxIntervals=None, IpDiffServ=None, MinRxInterval=None, Multiplier=None, Name=None, NoOfSessions=None, PollInterval=None, SourceIp6=None, Status=None, TimeoutMultiplier=None, TxInterval=None):
		"""Gets child instances of Bfdv6Interface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Bfdv6Interface will be returned.

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
			SourceIp6 (obj(ixnetwork_restpy.multivalue.Multivalue)): If Configure Echo Source-IP is selected, the IPv6 source address of the Echo Message
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TimeoutMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): The negotiated transmit interval, multiplied by this value, provides the detection time for the interface
			TxInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface.Bfdv6Interface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface import Bfdv6Interface
		return self._select(Bfdv6Interface(self), locals())

	def add_Bfdv6Interface(self, AggregateBfdSession="True", ConnectedVia=None, Multiplier="1", Name=None, NoOfSessions="0", StackedLayers=None):
		"""Adds a child instance of Bfdv6Interface on the server.

		Args:
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface.Bfdv6Interface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface import Bfdv6Interface
		return self._create(Bfdv6Interface(self), locals())

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

	def BgpIpv6Peer(self, ActAsRestarted=None, Active=None, AdvertiseEndOfRib=None, AlwaysIncludeTunnelEncExtCommunity=None, AsSetMode=None, Authentication=None, BgpId=None, BgpLsAsSetMode=None, BgpLsEnableAsPathSegments=None, BgpLsEnableCluster=None, BgpLsEnableExtendedCommunity=None, BgpLsNoOfASPathSegments=None, BgpLsNoOfClusters=None, BgpLsNoOfCommunities=None, BgpLsOverridePeerAsSetMode=None, CapabilityIpV4Mdt=None, CapabilityIpV4Mpls=None, CapabilityIpV4MplsVpn=None, CapabilityIpV4Multicast=None, CapabilityIpV4MulticastVpn=None, CapabilityIpV4Unicast=None, CapabilityIpV6Mpls=None, CapabilityIpV6MplsVpn=None, CapabilityIpV6Multicast=None, CapabilityIpV6MulticastVpn=None, CapabilityIpV6Unicast=None, CapabilityIpv4MplsAddPath=None, CapabilityIpv4UnicastAddPath=None, CapabilityIpv6MplsAddPath=None, CapabilityIpv6UnicastAddPath=None, CapabilityLinkStateNonVpn=None, CapabilityNHEncodingCapabilities=None, CapabilityRouteConstraint=None, CapabilityRouteRefresh=None, CapabilitySRTEPoliciesV4=None, CapabilitySRTEPoliciesV6=None, CapabilityVpls=None, Capabilityipv4UnicastFlowSpec=None, Capabilityipv6UnicastFlowSpec=None, ConfigureKeepaliveTimer=None, CopyTtl=None, Count=None, CustomSidType=None, DescriptiveName=None, DiscardIxiaGeneratedRoutes=None, DowntimeInSec=None, DutIp=None, EnSRv6DataPlane=None, Enable4ByteAs=None, EnableBfdRegistration=None, EnableBgpId=None, EnableBgpIdSameAsRouterId=None, EnableBgpLsCommunity=None, EnableEPETraffic=None, EnableGracefulRestart=None, EnableLlgr=None, EnableReducedEncapsulation=None, EthernetSegmentsCountV6=None, Evpn=None, FilterEvpn=None, FilterIpV4Mpls=None, FilterIpV4MplsVpn=None, FilterIpV4Multicast=None, FilterIpV4MulticastVpn=None, FilterIpV4Unicast=None, FilterIpV6Mpls=None, FilterIpV6MplsVpn=None, FilterIpV6Multicast=None, FilterIpV6MulticastVpn=None, FilterIpV6Unicast=None, FilterIpv4MulticastBgpMplsVpn=None, FilterIpv4UnicastFlowSpec=None, FilterIpv6MulticastBgpMplsVpn=None, FilterIpv6UnicastFlowSpec=None, FilterLinkState=None, FilterSRTEPoliciesV4=None, FilterSRTEPoliciesV6=None, FilterVpls=None, Flap=None, HoldTimer=None, IpVrfToIpVrfType=None, Ipv4MplsAddPathMode=None, Ipv4MplsCapability=None, Ipv4MulticastBgpMplsVpn=None, Ipv4MultipleMplsLabelsCapability=None, Ipv4UnicastAddPathMode=None, Ipv6MplsAddPathMode=None, Ipv6MplsCapability=None, Ipv6MulticastBgpMplsVpn=None, Ipv6MultipleMplsLabelsCapability=None, Ipv6UnicastAddPathMode=None, IrbInterfaceLabel=None, IrbIpv6Address=None, KeepaliveTimer=None, LocalAs2Bytes=None, LocalAs4Bytes=None, MaxSidPerSrh=None, Md5Key=None, ModeOfBfdOperations=None, MplsLabelsCountForIpv4MplsRoute=None, MplsLabelsCountForIpv6MplsRoute=None, Multiplier=None, Name=None, NoOfEPEPeers=None, NoOfExtendedCommunities=None, NoOfPeerSet=None, NoOfUserDefinedAfiSafi=None, NumBgpLsId=None, NumBgpLsInstanceIdentifier=None, NumBgpUpdatesGeneratedPerIteration=None, NumberFlowSpecRangeV4=None, NumberFlowSpecRangeV6=None, NumberSRTEPolicies=None, OperationalModel=None, RestartTime=None, RoutersMacOrIrbMacAddress=None, SRGBRangeCount=None, SendIxiaSignatureWithRoutes=None, Srv6Ttl=None, StaleTime=None, Status=None, TcpWindowSizeInBytes=None, Ttl=None, Type=None, UpdateInterval=None, UptimeInSec=None, UseStaticPolicy=None, VplsEnableNextHop=None, VplsNextHop=None):
		"""Gets child instances of BgpIpv6Peer from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIpv6Peer will be returned.

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
			CapabilityNHEncodingCapabilities (obj(ixnetwork_restpy.multivalue.Multivalue)): Extended Next Hop Encoding Capability
			CapabilityRouteConstraint (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Constraint
			CapabilityRouteRefresh (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Refresh
			CapabilitySRTEPoliciesV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv4 SR TE Policy Capability
			CapabilitySRTEPoliciesV6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6 SR TE Policy Capability
			CapabilityVpls (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS
			Capabilityipv4UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Unicast Flow Spec
			Capabilityipv6UnicastFlowSpec (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Unicast Flow Spec
			ConfigureKeepaliveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Keepalive Timer
			CopyTtl (bool): Copy TTL from customer packet to outer IPv6 header
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			CustomSidType (obj(ixnetwork_restpy.multivalue.Multivalue)): moved to port data in bgp/srv6 Custom SID Type
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardIxiaGeneratedRoutes (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard Ixia Generated Routes
			DowntimeInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime in Seconds
			DutIp (obj(ixnetwork_restpy.multivalue.Multivalue)): DUT IP
			EnSRv6DataPlane (bool): Ingress Peer Supports SRv6 VPN
			Enable4ByteAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable 4-Byte AS
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableBgpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BGP ID
			EnableBgpIdSameAsRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP ID Same as Router ID
			EnableBgpLsCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableEPETraffic (bool): Enable EPE Traffic
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Graceful Restart
			EnableLlgr (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable LLGR
			EnableReducedEncapsulation (bool): Enable Reduced Encapsulation in Data-Plane for SRv6
			EthernetSegmentsCountV6 (number): Number of Ethernet Segments
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
			IrbIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IRB IPv6 Address
			KeepaliveTimer (obj(ixnetwork_restpy.multivalue.Multivalue)): Keepalive Timer
			LocalAs2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Local AS# (2-Bytes)
			LocalAs4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Local AS# (4-Bytes)
			MaxSidPerSrh (number): Max number of SIDs a SRH can have
			Md5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): MD5 Key
			ModeOfBfdOperations (obj(ixnetwork_restpy.multivalue.Multivalue)): Mode of BFD Operations
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEPEPeers (number): 
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfPeerSet (number): 
			NoOfUserDefinedAfiSafi (number): Count of User defined AFI SAFI
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
			Srv6Ttl (number): TTL value to be used in outer IPv6 header
			StaleTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Stale Time/ LLGR Stale Time
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TcpWindowSizeInBytes (obj(ixnetwork_restpy.multivalue.Multivalue)): TCP Window Size (in bytes)
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): TTL
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type
			UpdateInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Update Interval
			UptimeInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime in Seconds
			UseStaticPolicy (bool): If enabled then SRTE policy will be advertised
			VplsEnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS Enable Next Hop
			VplsNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS Next Hop

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer.BgpIpv6Peer))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer import BgpIpv6Peer
		return self._select(BgpIpv6Peer(self), locals())

	def add_BgpIpv6Peer(self, BgpLsNoOfASPathSegments="1", BgpLsNoOfClusters="1", BgpLsNoOfCommunities="1", CapabilityIpv4MplsAddPath="False", CapabilityIpv6MplsAddPath="False", ConnectedVia=None, CopyTtl="False", EnSRv6DataPlane="False", EnableEPETraffic="False", EnableReducedEncapsulation="True", EthernetSegmentsCountV6="0", IpVrfToIpVrfType="interfacefullWithUnnumberedCorefacingIRB", Ipv4MplsCapability="False", Ipv4MultipleMplsLabelsCapability="False", Ipv6MplsCapability="False", Ipv6MultipleMplsLabelsCapability="False", MaxSidPerSrh="3", MplsLabelsCountForIpv4MplsRoute="1", MplsLabelsCountForIpv6MplsRoute="1", Multiplier="1", Name=None, NoOfEPEPeers="0", NoOfExtendedCommunities="1", NoOfPeerSet="0", NoOfUserDefinedAfiSafi="0", NumberFlowSpecRangeV4="0", NumberFlowSpecRangeV6="0", NumberSRTEPolicies="0", SRGBRangeCount="1", Srv6Ttl="62", StackedLayers=None, UseStaticPolicy="True"):
		"""Adds a child instance of BgpIpv6Peer on the server.

		Args:
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CopyTtl (bool): Copy TTL from customer packet to outer IPv6 header
			EnSRv6DataPlane (bool): Ingress Peer Supports SRv6 VPN
			EnableEPETraffic (bool): Enable EPE Traffic
			EnableReducedEncapsulation (bool): Enable Reduced Encapsulation in Data-Plane for SRv6
			EthernetSegmentsCountV6 (number): Number of Ethernet Segments
			IpVrfToIpVrfType (str(interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsCapability (bool): IPv4 MPLS Capability
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability
			Ipv6MplsCapability (bool): IPv6 MPLS Capability
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability
			MaxSidPerSrh (number): Max number of SIDs a SRH can have
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEPEPeers (number): 
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfPeerSet (number): 
			NoOfUserDefinedAfiSafi (number): Count of User defined AFI SAFI
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			SRGBRangeCount (number): SRGB Range Count
			Srv6Ttl (number): TTL value to be used in outer IPv6 header
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			UseStaticPolicy (bool): If enabled then SRTE policy will be advertised

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer.BgpIpv6Peer)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer import BgpIpv6Peer
		return self._create(BgpIpv6Peer(self), locals())

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

	def Dhcpv6server(self, Count=None, DescriptiveName=None, DnsDomain=None, IpDns1=None, IpDns2=None, Multiplier=None, Name=None, PoolCount=None, ReconfviaRelay=None, Status=None, SubnetAddrAssign=None, UseRapidCommit=None):
		"""Gets child instances of Dhcpv6server from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv6server will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DnsDomain (obj(ixnetwork_restpy.multivalue.Multivalue)): The domain name to be searched during name resolution advertised in DHCP Offer and Reply messages.
			IpDns1 (obj(ixnetwork_restpy.multivalue.Multivalue)): The first DNS address advertised in DHCP Offer and Reply messages.
			IpDns2 (obj(ixnetwork_restpy.multivalue.Multivalue)): The second DNS address advertised in DHCP Offer and Reply messages.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PoolCount (number): number of DHCP pools a single server has
			ReconfviaRelay (obj(ixnetwork_restpy.multivalue.Multivalue)): If Enabled allows Reconfigure to be sent from server to Client via RelayAgent
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SubnetAddrAssign (obj(ixnetwork_restpy.multivalue.Multivalue)): Enabled DHCPv6 Server to assign IP based on Relay Agent IP Address Subnet.
			UseRapidCommit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables DHCP Server to negotiate leases with rapid commit for DHCP Clients that request it.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server.Dhcpv6server))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server import Dhcpv6server
		return self._select(Dhcpv6server(self), locals())

	def add_Dhcpv6server(self, ConnectedVia=None, Multiplier="1", Name=None, PoolCount="1", StackedLayers=None):
		"""Adds a child instance of Dhcpv6server on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PoolCount (number): number of DHCP pools a single server has
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server.Dhcpv6server)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6server import Dhcpv6server
		return self._create(Dhcpv6server(self), locals())

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

	def MldHost(self, Active=None, Count=None, DescriptiveName=None, EnableIptv=None, EnableProxyReporting=None, GQResponseMode=None, GSResponseMode=None, ImResponse=None, JlMultiplier=None, Multiplier=None, Name=None, NoOfGrpRanges=None, ReportFreq=None, RouterAlert=None, Status=None, USResponseMode=None, VersionType=None):
		"""Gets child instances of MldHost from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MldHost will be returned.

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
			VersionType (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the MLD Version Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost.MldHost))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost import MldHost
		return self._select(MldHost(self), locals())

	def add_MldHost(self, ConnectedVia=None, JlMultiplier="1", Multiplier="1", Name=None, NoOfGrpRanges="1", StackedLayers=None):
		"""Adds a child instance of MldHost on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			JlMultiplier (number): No. of Join/Leave messages to send per opertation
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfGrpRanges (number): Defines the number of group range per host required
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost.MldHost)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost import MldHost
		return self._create(MldHost(self), locals())

	def MldQuerier(self, Active=None, Count=None, DescriptiveName=None, DiscardLearntInfo=None, GeneralQueryInterval=None, GeneralQueryResponseInterval=None, Multiplier=None, Name=None, ProxyQuerier=None, RobustnessVariable=None, RouterAlert=None, SpecificQueryResponseInterval=None, SpecificQueryTransmissionCount=None, StartupQueryCount=None, Status=None, SupportElection=None, SupportOlderVersionHost=None, SupportOlderVersionQuerier=None, VersionType=None):
		"""Gets child instances of MldQuerier from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MldQuerier will be returned.

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
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier.MldQuerier))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier import MldQuerier
		return self._select(MldQuerier(self), locals())

	def add_MldQuerier(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of MldQuerier on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier.MldQuerier)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier import MldQuerier
		return self._create(MldQuerier(self), locals())

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

	def Ospfv3(self, Active=None, AreaId=None, AreaIdIp=None, AuthAlgo=None, Count=None, DeadInterval=None, DemandCircuit=None, DescriptiveName=None, EnableAuthentication=None, EnableBfdRegistration=None, EnableFastHello=None, EnableIgnoreDbDescMtu=None, ExternalCapability=None, HelloInterval=None, HelloMultiplier=None, InstanceId=None, Key=None, LinkMetric=None, Multiplier=None, Name=None, NetworkType=None, NssaCapability=None, Priority=None, Router=None, SaId=None, Status=None, TypeAreaId=None, V6=None):
		"""Gets child instances of Ospfv3 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv3 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AreaId (obj(ixnetwork_restpy.multivalue.Multivalue)): OSPFv3 Area ID for a non-connected interface, displayed in Interger format
			AreaIdIp (obj(ixnetwork_restpy.multivalue.Multivalue)): OSPFv3 Area ID for a non-connected interface, displayed in IP Address format
			AuthAlgo (obj(ixnetwork_restpy.multivalue.Multivalue)): Authentication Algorithms
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Dead Interval
			DemandCircuit (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 5
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAuthentication (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Authentication
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableFastHello (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Fast Hello
			EnableIgnoreDbDescMtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore DB-Desc MTU
			ExternalCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 1
			HelloInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Interval
			HelloMultiplier (obj(ixnetwork_restpy.multivalue.Multivalue)): Hello Multiplier
			InstanceId (obj(ixnetwork_restpy.multivalue.Multivalue)): Instance ID
			Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Key
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Type
			NssaCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 3
			Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): Priority (when DR/BDR)
			Router (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 4
			SaId (obj(ixnetwork_restpy.multivalue.Multivalue)): Security Association ID
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TypeAreaId (obj(ixnetwork_restpy.multivalue.Multivalue)): Area ID Type
			V6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Option bit 0

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3.Ospfv3))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3 import Ospfv3
		return self._select(Ospfv3(self), locals())

	def add_Ospfv3(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ospfv3 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3.Ospfv3)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3 import Ospfv3
		return self._create(Ospfv3(self), locals())

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

	def PimV6Interface(self, Active=None, AutoPickNeighbor=None, BootstrapHashMaskLength=None, BootstrapInterval=None, BootstrapPriority=None, BootstrapTimeout=None, Count=None, CrpRanges=None, DescriptiveName=None, DisableTriggered=None, DiscardLearnedRpInfo=None, EnableBfdRegistration=None, EnableBootstrap=None, EnablePrune=None, ForceSemantic=None, HelloHoldTime=None, HelloInterval=None, JoinPrunes=None, LanPruneTbit=None, LearnSelectedRpSet=None, Multiplier=None, Name=None, NeighborV6Address=None, OverrideInterval=None, PruneDelay=None, SendBidirectional=None, SendGenerationIdOption=None, SendGenerationMode=None, Sources=None, Status=None, SupportUnicastBsm=None, TriggeredHelloDelay=None):
		"""Gets child instances of PimV6Interface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PimV6Interface will be returned.

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
			NeighborV6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): (Auto Pick Neighbor must be disabled/not selected to make this field active) The user can manually type in the link-local address to be used for the Upstream Neighbor address field in the Join/Prune message.
			OverrideInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): (in ms) The delay interval for randomizing the transmission time for override messages-when scheduling a delayed Join message. The default value is 2,500 milliseconds (ms). The valid range is 100 to 7FFF msec. (This is part of the LAN Prune Delay option included in Hello messages).
			PruneDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): (in ms) The value of the LAN Prune (propagation) Delay for this PIM-SM interface. The expected delay for messages propagated on the link. It indicates to an upstream router how long to wait for a Join override message before it prunes an interface. The default value is 500 msec. The valid range is 100 to 0x7FFF msec. (LAN Prune Delay is an Option included in Hello messages.)
			SendBidirectional (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, sets the bi-directional PIM-SM flag bit (= 1), per IETF DRAFT draft-ietf-pim-bidir-04. (Note: Designated Forwarder election is not currently supported.)
			SendGenerationIdOption (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, enables the Send Generation ID Option, and the Generation ID Mode field will become available to make a mode selection.
			SendGenerationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The mode for creating the 32-bit value for the Generation Identifier (GenID) option in the Hello message. A new GenID is created each time an interface (or router) starts or restarts PIM-SM forwarding. A change in this value indicates to the neighbor(s) that a change of state may have occurred, and that the old PIM-SM states information received from those interfaces should be discarded. Choose one of: Incremental-the GenID increases by 1 for each successive Hello Message sent from this emulated PIM-SM router. Random-each Hello message sent from this emulated PIM-SM router will have a randomly-generated GenID. Constant (the default)-the GenID remains the same in all of the Hello Messages sent from this emulated. PIM-SM router.
			Sources (number): Number of Sources
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportUnicastBsm (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, this supports the sending and processing of Unicast bootstrap messages.
			TriggeredHelloDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): The time (in seconds) after which the router senses a delay in sending or receiving PIM-SM hello message.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface.PimV6Interface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface import PimV6Interface
		return self._select(PimV6Interface(self), locals())

	def add_PimV6Interface(self, ConnectedVia=None, CrpRanges="0", JoinPrunes="0", Multiplier="1", Name=None, Sources="0", StackedLayers=None):
		"""Adds a child instance of PimV6Interface on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CrpRanges (number): Number of C-RP Ranges
			JoinPrunes (number): Number of Join/Prunes
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Sources (number): Number of Sources
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface.PimV6Interface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface import PimV6Interface
		return self._create(PimV6Interface(self), locals())

	@property
	def PppoxServerSessions(self):
		"""Returns the one and only one PppoxServerSessions object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserversessions.PppoxServerSessions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserversessions import PppoxServerSessions
		return self._read(PppoxServerSessions(self), None)

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
	def AcName(self):
		"""Access Concentrator Name - this option is only available for PPP servers.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('acName')

	@property
	def AcceptAnyAuthValue(self):
		"""Configures a PAP/CHAP authenticator to accept all offered usernames, passwords, and base domain names

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('acceptAnyAuthValue')

	@property
	def AuthRetries(self):
		"""Number of PPP authentication retries

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authRetries')

	@property
	def AuthTimeout(self):
		"""Timeout for PPP authentication, in seconds.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authTimeout')

	@property
	def AuthType(self):
		"""The authentication type to use during link setup.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authType')

	@property
	def ClientBaseIID(self):
		"""Obsolete - use clientIID instead.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientBaseIID')

	@property
	def ClientBaseIp(self):
		"""The base IP address to be used when creating PPP client addresses. This property is used as an incrementor for the 'clientIpIncr' property

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientBaseIp')

	@property
	def ClientIID(self):
		"""The base IPv6CP (RFC5072) interface identifier for the PPP client. Used in conjunction with 'clientIIDIncr' as its incrementor. Valid for IPv6 only. The identifier is used in assigned global and local scope addresses created after negotiation.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientIID')

	@property
	def ClientIIDIncr(self):
		"""Client IPv6CP interface identifier increment, used in conjuction with the base identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientIIDIncr')

	@property
	def ClientIpIncr(self):
		"""The incrementor for the clientBaseIp property address when multiple PPP addresses are created.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('clientIpIncr')

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
	def DnsServerList(self):
		"""DNS server list separacted by semicolon

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dnsServerList')

	@property
	def EchoReqInterval(self):
		"""Keep alive interval, in seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('echoReqInterval')

	@property
	def EnableDnsRa(self):
		"""Enable RDNSS routing advertisments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableDnsRa')

	@property
	def EnableEchoReq(self):
		"""?

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableEchoReq')

	@property
	def EnableEchoRsp(self):
		"""?

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableEchoRsp')

	@property
	def EnableMaxPayload(self):
		"""Enables PPP Max Payload tag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableMaxPayload')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def Ipv6AddrPrefixLen(self):
		"""Address prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6AddrPrefixLen')

	@property
	def Ipv6PoolPrefix(self):
		"""Pool prefix for the IPv6 IP pool.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6PoolPrefix')

	@property
	def Ipv6PoolPrefixLen(self):
		"""Pool prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6PoolPrefixLen')

	@property
	def LcpAccm(self):
		"""Async-Control-Character-Map

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpAccm')

	@property
	def LcpEnableAccm(self):
		"""Enable Async-Control-Character-Map

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpEnableAccm')

	@property
	def LcpMaxFailure(self):
		"""Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpMaxFailure')

	@property
	def LcpRetries(self):
		"""Number of LCP retries

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpRetries')

	@property
	def LcpStartDelay(self):
		"""Delay time in milliseconds to wait before sending LCP Config Request packet

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpStartDelay')

	@property
	def LcpTermRetries(self):
		"""Number of LCP Termination Retries

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpTermRetries')

	@property
	def LcpTimeout(self):
		"""Timeout for LCP phase, in seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lcpTimeout')

	@property
	def MruNegotiation(self):
		"""Enable MRU Negotiation

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mruNegotiation')

	@property
	def Mtu(self):
		"""Max Transmit Unit for PPP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mtu')

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
	def NcpRetries(self):
		"""Number of NCP retries

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ncpRetries')

	@property
	def NcpTimeout(self):
		"""Timeout for NCP phase, in seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ncpTimeout')

	@property
	def NcpType(self):
		"""IP address type (IPv4 or IPv6) for Network Control Protocol

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ncpType')

	@property
	def PppoxServerGlobalAndPortData(self):
		"""Global and Port Settings

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)
		"""
		return self._get_attribute('pppoxServerGlobalAndPortData')

	@property
	def ServerBaseIID(self):
		"""Obsolete - use serverIID instead.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverBaseIID')

	@property
	def ServerBaseIp(self):
		"""The base IP address to be used when create PPP server addresses. This property is used in conjunction with the 'IPv4 Server IP Increment By' property.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverBaseIp')

	@property
	def ServerDnsOptions(self):
		"""The server DNS options.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverDnsOptions')

	@property
	def ServerIID(self):
		"""The base IPv6CP (RFC5072) interface identifier for the PPP server, used in conjunction with 'serverIIDIncr' as incrementor. Valid for IPv6 only.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverIID')

	@property
	def ServerIIDIncr(self):
		"""Server IPv6CP interface identifier increment, used in conjuction with the base identifier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverIIDIncr')

	@property
	def ServerIpIncr(self):
		"""Server IP increment, used in conjuction with 'IPv4 Server IP' property

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverIpIncr')

	@property
	def ServerNcpOptions(self):
		"""Specifies the NCP configuration mode.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverNcpOptions')

	@property
	def ServerNetmask(self):
		"""The netmask that the server will assign to the client when the Server Netmask Options parameter is set to Supply Netmask.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverNetmask')

	@property
	def ServerNetmaskOptions(self):
		"""The server netmask option.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverNetmaskOptions')

	@property
	def ServerPrimaryDnsAddress(self):
		"""The primary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverPrimaryDnsAddress')

	@property
	def ServerSecondaryDnsAddress(self):
		"""The secondary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to Supply Primary and Secondary.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSecondaryDnsAddress')

	@property
	def ServerSignalDslTypeTlv(self):
		"""DSL-Type TLV to be inserted in PPPoE VSA Tag.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalDslTypeTlv')

	@property
	def ServerSignalIWF(self):
		"""This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADO and PADS packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalIWF')

	@property
	def ServerSignalLoopChar(self):
		"""This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADO and PADS packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalLoopChar')

	@property
	def ServerSignalLoopEncapsulation(self):
		"""This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADO and PADS packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalLoopEncapsulation')

	@property
	def ServerSignalLoopId(self):
		"""This parameter enables or disables the insertion of sub-options 0x01 and 0x02 (Remote ID and Circuit ID) into the DSL tag in PADO and PADS packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalLoopId')

	@property
	def ServerSignalPonTypeTlv(self):
		"""PON-Type TLV to be inserted in PPPoE VSA Tag.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverSignalPonTypeTlv')

	@property
	def ServerV6NcpOptions(self):
		"""Specifies the NCP configuration mode.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverV6NcpOptions')

	@property
	def ServerWinsOptions(self):
		"""The WINS server discovery mode.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverWinsOptions')

	@property
	def ServerWinsPrimaryAddress(self):
		"""The primary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverWinsPrimaryAddress')

	@property
	def ServerWinsSecondaryAddress(self):
		"""The secondary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to Supply Primary and Secondary.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serverWinsSecondaryAddress')

	@property
	def ServiceName(self):
		"""Access Concentrator Service Name - this option is only available for PPP servers.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('serviceName')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SessionsCount(self):
		"""Number of PPP clients a single server can accept (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('sessionsCount')
	@SessionsCount.setter
	def SessionsCount(self, value):
		self._set_attribute('sessionsCount', value)

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
		"""Deletes a child instance of Pppoxserver on the server.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pppoxserver object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
