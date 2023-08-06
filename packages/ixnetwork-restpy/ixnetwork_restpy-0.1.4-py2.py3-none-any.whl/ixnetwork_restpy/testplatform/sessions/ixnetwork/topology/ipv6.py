from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6(Base):
	"""Static IPV6
	"""

	_SDM_NAME = 'ipv6'

	def __init__(self, parent):
		super(Ipv6, self).__init__(parent)

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

	def Dhcpv6relayAgent(self, Count=None, DescriptiveName=None, Dhcp6RelayAddress=None, Dhcp6RelayAgentGlobalAndPortData=None, Dhcp6ServerAddress=None, LightweightDhcp6RelayAgentGlobalAndPortData=None, Multiplier=None, Name=None, ReconfviaRelay=None, Status=None):
		"""Gets child instances of Dhcpv6relayAgent from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Dhcpv6relayAgent will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Dhcp6RelayAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Complete description here
			Dhcp6RelayAgentGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			Dhcp6ServerAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Complete description here
			LightweightDhcp6RelayAgentGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ReconfviaRelay (obj(ixnetwork_restpy.multivalue.Multivalue)): If Enabled allows Reconfigure to be sent from server to Client via RelayAgent
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent.Dhcpv6relayAgent))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent import Dhcpv6relayAgent
		return self._select(Dhcpv6relayAgent(self), locals())

	def add_Dhcpv6relayAgent(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Dhcpv6relayAgent on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent.Dhcpv6relayAgent)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv6relayagent import Dhcpv6relayAgent
		return self._create(Dhcpv6relayAgent(self), locals())

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

	def Greoipv6(self, Count=None, DescriptiveName=None, DestIp=None, EnableChecksum=None, EnableKey=None, EnableSequenceNumber=None, InKey=None, Multiplier=None, Name=None, OutKey=None, SrcIp=None, Status=None):
		"""Gets child instances of Greoipv6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Greoipv6 will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination IPv6 address
			EnableChecksum (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Checksum.
			EnableKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Key.
			EnableSequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Sequence Number.
			InKey (obj(ixnetwork_restpy.multivalue.Multivalue)): In Key.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OutKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Out Key.
			SrcIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Source IPv6 address
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6.Greoipv6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6 import Greoipv6
		return self._select(Greoipv6(self), locals())

	def add_Greoipv6(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Greoipv6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6.Greoipv6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv6 import Greoipv6
		return self._create(Greoipv6(self), locals())

	def Ipv6sr(self, Active=None, CleanupFlag=None, Count=None, DescriptiveName=None, FirstSegment=None, Multiplier=None, Name=None, NumberSegments=None, OamFlag=None, OuterDestAddr=None, OuterSrcAddr=None, ProtectedFlag=None, SID0=None, SIDEnable0=None, SegmentsLeft=None, Status=None, TunnelDescription=None, UseAsIngress=None):
		"""Gets child instances of Ipv6sr from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv6sr will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			CleanupFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set when the SRH has to be removed from the packet when the packet reaches the last segment
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			FirstSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Count of enabled SID List -1
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberSegments (number): Maximum available index of the Segments List in SRH header (0 Based Index)
			OamFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates that this packet will be Operations And Management
			OuterDestAddr (obj(ixnetwork_restpy.multivalue.Multivalue)): Controlled by Segments Left, index from enabled SID List
			OuterSrcAddr (obj(ixnetwork_restpy.multivalue.Multivalue)): Outer IPv6 Source Address
			ProtectedFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set when the packet has been rerouted through FRR mechanism by an SR endpoint node
			SID0 (obj(ixnetwork_restpy.multivalue.Multivalue)): Segment Item Address
			SIDEnable0 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable This Segment
			SegmentsLeft (obj(ixnetwork_restpy.multivalue.Multivalue)): Segments Left (0 Based Index)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TunnelDescription (obj(ixnetwork_restpy.multivalue.Multivalue)): Tunnel Description
			UseAsIngress (obj(ixnetwork_restpy.multivalue.Multivalue)): Use This Device As Ingress

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr.Ipv6sr))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr import Ipv6sr
		return self._select(Ipv6sr(self), locals())

	def add_Ipv6sr(self, ConnectedVia=None, Multiplier="1", Name=None, NumberSegments="0", StackedLayers=None):
		"""Adds a child instance of Ipv6sr on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberSegments (number): Maximum available index of the Segments List in SRH header (0 Based Index)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr.Ipv6sr)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6sr import Ipv6sr
		return self._create(Ipv6sr(self), locals())

	def LdpBasicRouterV6(self, Active=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV6=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpBasicRouterV6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpBasicRouterV6 will be returned.

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
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
		return self._select(LdpBasicRouterV6(self), locals())

	def add_LdpBasicRouterV6(self, ConnectedVia=None, LdpVersion="version1", LeafRangesCountV6="0", Multiplier="1", Name=None, RootRangesCountV6="0", StackedLayers=None):
		"""Adds a child instance of LdpBasicRouterV6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
		return self._create(LdpBasicRouterV6(self), locals())

	def LdpTargetedRouterV6(self, Active=None, BfdOpeMode=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableBfdRegistration=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, Ipv6peerCount=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LabelSpaceID=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, OperationMode=None, PeerCount=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV6=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpTargetedRouterV6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpTargetedRouterV6 will be returned.

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
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of LDP Label Advertisement
			PeerCount (number): The number of Target Peers configured for this LDP router
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
		return self._select(LdpTargetedRouterV6(self), locals())

	def add_LdpTargetedRouterV6(self, ConnectedVia=None, Ipv6peerCount="0", LdpVersion="version1", LeafRangesCountV6="0", Multiplier="1", Name=None, PeerCount="0", RootRangesCountV6="0", StackedLayers=None):
		"""Adds a child instance of LdpTargetedRouterV6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeerCount (number): The number of Target Peers configured for this LDP router
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
		return self._create(LdpTargetedRouterV6(self), locals())

	def Ldpv6ConnectedInterface(self, Active=None, Authentication=None, BasicHelloInterval=None, BasicHoldTime=None, Count=None, DescriptiveName=None, EnableBfdRegistration=None, LabelSpaceID=None, MD5Key=None, Multiplier=None, Name=None, OperationMode=None, Status=None):
		"""Gets child instances of Ldpv6ConnectedInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ldpv6ConnectedInterface will be returned.

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
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface.Ldpv6ConnectedInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface import Ldpv6ConnectedInterface
		return self._select(Ldpv6ConnectedInterface(self), locals())

	def add_Ldpv6ConnectedInterface(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ldpv6ConnectedInterface on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface.Ldpv6ConnectedInterface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6connectedinterface import Ldpv6ConnectedInterface
		return self._create(Ldpv6ConnectedInterface(self), locals())

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
	def Address(self):
		"""IPv6 addresses of the devices

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
		"""Gateways of the layer

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
			list(str[duplicateAddress|interfaceRemoved|none|resolveMacFailed])
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
		"""Deletes a child instance of Ipv6 on the server.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def SendNs(self, Arg1):
		"""Executes the sendNs operation on the server.

		Send Neighbor Solicitation request to configured gateway IP address to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendNs', payload=locals(), response_object=None)

	def SendNs(self, Arg1, SessionIndices):
		"""Executes the sendNs operation on the server.

		Send Neighbor Solicitation request to configured gateway IP address to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendNs', payload=locals(), response_object=None)

	def SendNs(self, Arg1, SessionIndices):
		"""Executes the sendNs operation on the server.

		Send Neighbor Solicitation request to configured gateway IP address to resolve Gateway MAC for selected items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('sendNs', payload=locals(), response_object=None)

	def SendNsManual(self, DestIP):
		"""Executes the sendNsManual operation on the server.

		Send Neighbor Solicitation request to specified IP address for selected items.

		Args:
			DestIP (str): This parameter requires a destIP of type kString

		Returns:
			list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendNsManual', payload=locals(), response_object=None)

	def SendNsManual(self, DestIP, SessionIndices):
		"""Executes the sendNsManual operation on the server.

		Send Neighbor Solicitation request to specified IP address for selected items.

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
		return self._execute('sendNsManual', payload=locals(), response_object=None)

	def SendNsManual(self, SessionIndices, DestIP):
		"""Executes the sendNsManual operation on the server.

		Send Neighbor Solicitation request to specified IP address for selected items.

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
		return self._execute('sendNsManual', payload=locals(), response_object=None)

	def SendPing(self, DestIP):
		"""Executes the sendPing operation on the server.

		Send ping for selected IPv6 items.

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

		Send ping for selected IPv6 items.

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

		Send ping for selected IPv6 items.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
