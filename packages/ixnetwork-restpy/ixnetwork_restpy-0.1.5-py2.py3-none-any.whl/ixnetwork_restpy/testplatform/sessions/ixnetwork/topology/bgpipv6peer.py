from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BgpIpv6Peer(Base):
	"""Bgp IPv6 Peer
	"""

	_SDM_NAME = 'bgpIpv6Peer'

	def __init__(self, parent):
		super(BgpIpv6Peer, self).__init__(parent)

	@property
	def BgpCustomAfiSafiv6(self):
		"""Returns the one and only one BgpCustomAfiSafiv6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv6.BgpCustomAfiSafiv6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv6 import BgpCustomAfiSafiv6
		return self._read(BgpCustomAfiSafiv6(self), None)

	@property
	def BgpEpePeerList(self):
		"""Returns the one and only one BgpEpePeerList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist.BgpEpePeerList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist import BgpEpePeerList
		return self._read(BgpEpePeerList(self), None)

	@property
	def BgpEpePeerSetList(self):
		"""Returns the one and only one BgpEpePeerSetList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeersetlist.BgpEpePeerSetList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeersetlist import BgpEpePeerSetList
		return self._read(BgpEpePeerSetList(self), None)

	@property
	def BgpEthernetSegmentV6(self):
		"""Returns the one and only one BgpEthernetSegmentV6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv6.BgpEthernetSegmentV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv6 import BgpEthernetSegmentV6
		return self._read(BgpEthernetSegmentV6(self), None)

	@property
	def BgpFlowSpecRangesList(self):
		"""Returns the one and only one BgpFlowSpecRangesList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist.BgpFlowSpecRangesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist import BgpFlowSpecRangesList
		return self._read(BgpFlowSpecRangesList(self), None)

	@property
	def BgpFlowSpecRangesListV4(self):
		"""Returns the one and only one BgpFlowSpecRangesListV4 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4.BgpFlowSpecRangesListV4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4 import BgpFlowSpecRangesListV4
		return self._read(BgpFlowSpecRangesListV4(self), None)

	@property
	def BgpFlowSpecRangesListV6(self):
		"""Returns the one and only one BgpFlowSpecRangesListV6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6.BgpFlowSpecRangesListV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6 import BgpFlowSpecRangesListV6
		return self._read(BgpFlowSpecRangesListV6(self), None)

	def BgpIPv6EvpnEvi(self, Active=None, AdRouteLabel=None, AdvertiseL3vniSeparately=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigPMSITunnelId=None, AutoConfigureRdIpAddress=None, BMacFirstLabel=None, BMacSecondLabel=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableBMacSecondLabel=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableL3TargetOnlyForRouteType5=None, EnableL3vniTargetList=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EsiType=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, Ipv4NextHop=None, Ipv6NextHop=None, L3vniImportRtListSameAsL3vniExportRtList=None, LocalPreference=None, MultiExitDiscriminator=None, MulticastTunnelType=None, Multiplier=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NumBroadcastDomainV6=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInL3vniExportRouteTargetList=None, NumRtInL3vniImportRouteTargetList=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PmsiTunnelIDv4=None, PmsiTunnelIDv6=None, RdEvi=None, RdIpAddress=None, SetNextHop=None, SetNextHopIpType=None, Status=None, UpstreamDownstreamAssignedMplsLabel=None, UseIpv4MappedIpv6Address=None, UseUpstreamDownstreamAssignedMplsLabel=None):
		"""Gets child instances of BgpIPv6EvpnEvi from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPv6EvpnEvi will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdRouteLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): AD Route Label
			AdvertiseL3vniSeparately (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise L3 Route Separately
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			AutoConfigPMSITunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Configure PMSI Tunnel ID
			AutoConfigureRdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto-Configure RD IP Addresses
			BMacFirstLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC First Label
			BMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC Second Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableBMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable B MAC Second Label
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableL3TargetOnlyForRouteType5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target only for Route Type 5
			EnableL3vniTargetList (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target List
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EsiType (obj(ixnetwork_restpy.multivalue.Multivalue)): ESI Type
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PmsiTunnelIDv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			PmsiTunnelIDv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			RdEvi (obj(ixnetwork_restpy.multivalue.Multivalue)): RD EVI
			RdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): RD IP Addresses
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned MPLS Label
			UseIpv4MappedIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Use IPv4 Mapped IPv6 Address
			UseUpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned MPLS Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi.BgpIPv6EvpnEvi))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi import BgpIPv6EvpnEvi
		return self._select(BgpIPv6EvpnEvi(self), locals())

	def add_BgpIPv6EvpnEvi(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", L3vniImportRtListSameAsL3vniExportRtList="True", Multiplier="1", Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1", NumBroadcastDomainV6="1", NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInL3vniExportRouteTargetList="1", NumRtInL3vniImportRouteTargetList="1", StackedLayers=None):
		"""Adds a child instance of BgpIPv6EvpnEvi on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi.BgpIPv6EvpnEvi)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi import BgpIPv6EvpnEvi
		return self._create(BgpIPv6EvpnEvi(self), locals())

	def BgpIPv6EvpnPbb(self, Active=None, AdRouteLabel=None, AdvertiseL3vniSeparately=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigPMSITunnelId=None, AutoConfigureRdIpAddress=None, BMacFirstLabel=None, BMacSecondLabel=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableBMacSecondLabel=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableL3TargetOnlyForRouteType5=None, EnableL3vniTargetList=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EsiType=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, Ipv4NextHop=None, Ipv6NextHop=None, L3vniImportRtListSameAsL3vniExportRtList=None, LocalPreference=None, MultiExitDiscriminator=None, MulticastTunnelType=None, Multiplier=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NumBroadcastDomainV6=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInL3vniExportRouteTargetList=None, NumRtInL3vniImportRouteTargetList=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PmsiTunnelIDv4=None, PmsiTunnelIDv6=None, RdEvi=None, RdIpAddress=None, SetNextHop=None, SetNextHopIpType=None, Status=None, UpstreamDownstreamAssignedMplsLabel=None, UseIpv4MappedIpv6Address=None, UseUpstreamDownstreamAssignedMplsLabel=None):
		"""Gets child instances of BgpIPv6EvpnPbb from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPv6EvpnPbb will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdRouteLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): AD Route Label
			AdvertiseL3vniSeparately (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise L3 Route Separately
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			AutoConfigPMSITunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Configure PMSI Tunnel ID
			AutoConfigureRdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto-Configure RD IP Addresses
			BMacFirstLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC First Label
			BMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC Second Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableBMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable B MAC Second Label
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableL3TargetOnlyForRouteType5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target only for Route Type 5
			EnableL3vniTargetList (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target List
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EsiType (obj(ixnetwork_restpy.multivalue.Multivalue)): ESI Type
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PmsiTunnelIDv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			PmsiTunnelIDv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			RdEvi (obj(ixnetwork_restpy.multivalue.Multivalue)): RD EVI
			RdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): RD IP Addresses
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned MPLS Label
			UseIpv4MappedIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Use IPv4 Mapped IPv6 Address
			UseUpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned MPLS Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb.BgpIPv6EvpnPbb))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb import BgpIPv6EvpnPbb
		return self._select(BgpIPv6EvpnPbb(self), locals())

	def add_BgpIPv6EvpnPbb(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", L3vniImportRtListSameAsL3vniExportRtList="True", Multiplier="1", Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1", NumBroadcastDomainV6="1", NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInL3vniExportRouteTargetList="1", NumRtInL3vniImportRouteTargetList="1", StackedLayers=None):
		"""Adds a child instance of BgpIPv6EvpnPbb on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb.BgpIPv6EvpnPbb)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb import BgpIPv6EvpnPbb
		return self._create(BgpIPv6EvpnPbb(self), locals())

	def BgpIPv6EvpnVXLAN(self, Active=None, AdRouteLabel=None, AdvertiseL3vniSeparately=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigPMSITunnelId=None, AutoConfigureRdIpAddress=None, BMacFirstLabel=None, BMacSecondLabel=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableBMacSecondLabel=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableL3TargetOnlyForRouteType5=None, EnableL3vniTargetList=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EsiType=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, Ipv4NextHop=None, Ipv6NextHop=None, L3vniImportRtListSameAsL3vniExportRtList=None, LocalPreference=None, MultiExitDiscriminator=None, MulticastTunnelType=None, MulticastTunnelTypeVxlan=None, Multiplier=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NumBroadcastDomainV6=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInL3vniExportRouteTargetList=None, NumRtInL3vniImportRouteTargetList=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PmsiTunnelIDv4=None, PmsiTunnelIDv6=None, RdEvi=None, RdIpAddress=None, SetNextHop=None, SetNextHopIpType=None, Status=None, UpstreamDownstreamAssignedMplsLabel=None, UseIpv4MappedIpv6Address=None, UseUpstreamDownstreamAssignedMplsLabel=None):
		"""Gets child instances of BgpIPv6EvpnVXLAN from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPv6EvpnVXLAN will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdRouteLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): AD Route Label
			AdvertiseL3vniSeparately (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise L3 Route Separately
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			AutoConfigPMSITunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Configure PMSI Tunnel ID
			AutoConfigureRdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto-Configure RD IP Addresses
			BMacFirstLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC First Label
			BMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC Second Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableBMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable B MAC Second Label
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableL3TargetOnlyForRouteType5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target only for Route Type 5
			EnableL3vniTargetList (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target List
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EsiType (obj(ixnetwork_restpy.multivalue.Multivalue)): ESI Type
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			MulticastTunnelTypeVxlan (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PmsiTunnelIDv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			PmsiTunnelIDv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			RdEvi (obj(ixnetwork_restpy.multivalue.Multivalue)): RD EVI
			RdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): RD IP Addresses
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned MPLS Label
			UseIpv4MappedIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Use IPv4 Mapped IPv6 Address
			UseUpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned MPLS Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan.BgpIPv6EvpnVXLAN))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan import BgpIPv6EvpnVXLAN
		return self._select(BgpIPv6EvpnVXLAN(self), locals())

	def add_BgpIPv6EvpnVXLAN(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", L3vniImportRtListSameAsL3vniExportRtList="True", Multiplier="1", Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1", NumBroadcastDomainV6="1", NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInL3vniExportRouteTargetList="1", NumRtInL3vniImportRouteTargetList="1", StackedLayers=None):
		"""Adds a child instance of BgpIPv6EvpnVXLAN on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan.BgpIPv6EvpnVXLAN)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan import BgpIPv6EvpnVXLAN
		return self._create(BgpIPv6EvpnVXLAN(self), locals())

	def BgpIPv6EvpnVXLANVpws(self, Active=None, AdRouteLabel=None, AdvertiseL3vniSeparately=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigPMSITunnelId=None, AutoConfigureRdIpAddress=None, BMacFirstLabel=None, BMacSecondLabel=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableBMacSecondLabel=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableL3TargetOnlyForRouteType5=None, EnableL3vniTargetList=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EsiType=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, Ipv4NextHop=None, Ipv6NextHop=None, L3vniImportRtListSameAsL3vniExportRtList=None, LocalPreference=None, MultiExitDiscriminator=None, MulticastTunnelType=None, MulticastTunnelTypeVxlan=None, Multiplier=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NumBroadcastDomainV6=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInL3vniExportRouteTargetList=None, NumRtInL3vniImportRouteTargetList=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PmsiTunnelIDv4=None, PmsiTunnelIDv6=None, RdEvi=None, RdIpAddress=None, SetNextHop=None, SetNextHopIpType=None, Status=None, UpstreamDownstreamAssignedMplsLabel=None, UseIpv4MappedIpv6Address=None, UseUpstreamDownstreamAssignedMplsLabel=None):
		"""Gets child instances of BgpIPv6EvpnVXLANVpws from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPv6EvpnVXLANVpws will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdRouteLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): AD Route Label
			AdvertiseL3vniSeparately (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise L3 Route Separately
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			AutoConfigPMSITunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Configure PMSI Tunnel ID
			AutoConfigureRdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto-Configure RD IP Addresses
			BMacFirstLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC First Label
			BMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC Second Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableBMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable B MAC Second Label
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableL3TargetOnlyForRouteType5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target only for Route Type 5
			EnableL3vniTargetList (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target List
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EsiType (obj(ixnetwork_restpy.multivalue.Multivalue)): ESI Type
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			MulticastTunnelTypeVxlan (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PmsiTunnelIDv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			PmsiTunnelIDv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			RdEvi (obj(ixnetwork_restpy.multivalue.Multivalue)): RD EVI
			RdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): RD IP Addresses
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned MPLS Label
			UseIpv4MappedIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Use IPv4 Mapped IPv6 Address
			UseUpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned MPLS Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws.BgpIPv6EvpnVXLANVpws))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws import BgpIPv6EvpnVXLANVpws
		return self._select(BgpIPv6EvpnVXLANVpws(self), locals())

	def add_BgpIPv6EvpnVXLANVpws(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", L3vniImportRtListSameAsL3vniExportRtList="True", Multiplier="1", Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1", NumBroadcastDomainV6="1", NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInL3vniExportRouteTargetList="1", NumRtInL3vniImportRouteTargetList="1", StackedLayers=None):
		"""Adds a child instance of BgpIPv6EvpnVXLANVpws on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws.BgpIPv6EvpnVXLANVpws)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws import BgpIPv6EvpnVXLANVpws
		return self._create(BgpIPv6EvpnVXLANVpws(self), locals())

	def BgpIPv6EvpnVpws(self, Active=None, AdRouteLabel=None, AdvertiseL3vniSeparately=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, AutoConfigPMSITunnelId=None, AutoConfigureRdIpAddress=None, BMacFirstLabel=None, BMacSecondLabel=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableBMacSecondLabel=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableL3TargetOnlyForRouteType5=None, EnableL3vniTargetList=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EsiType=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, Ipv4NextHop=None, Ipv6NextHop=None, L3vniImportRtListSameAsL3vniExportRtList=None, LocalPreference=None, MultiExitDiscriminator=None, MulticastTunnelType=None, Multiplier=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, NumBroadcastDomainV6=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInL3vniExportRouteTargetList=None, NumRtInL3vniImportRouteTargetList=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PmsiTunnelIDv4=None, PmsiTunnelIDv6=None, RdEvi=None, RdIpAddress=None, SetNextHop=None, SetNextHopIpType=None, Status=None, UpstreamDownstreamAssignedMplsLabel=None, UseIpv4MappedIpv6Address=None, UseUpstreamDownstreamAssignedMplsLabel=None):
		"""Gets child instances of BgpIPv6EvpnVpws from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPv6EvpnVpws will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdRouteLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): AD Route Label
			AdvertiseL3vniSeparately (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise L3 Route Separately
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			AutoConfigPMSITunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Configure PMSI Tunnel ID
			AutoConfigureRdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto-Configure RD IP Addresses
			BMacFirstLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC First Label
			BMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): B MAC Second Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableBMacSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable B MAC Second Label
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableL3TargetOnlyForRouteType5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target only for Route Type 5
			EnableL3vniTargetList (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable L3 Target List
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EsiType (obj(ixnetwork_restpy.multivalue.Multivalue)): ESI Type
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PmsiTunnelIDv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			PmsiTunnelIDv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): PMSI Tunnel ID
			RdEvi (obj(ixnetwork_restpy.multivalue.Multivalue)): RD EVI
			RdIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): RD IP Addresses
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned MPLS Label
			UseIpv4MappedIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Use IPv4 Mapped IPv6 Address
			UseUpstreamDownstreamAssignedMplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned MPLS Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws.BgpIPv6EvpnVpws))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws import BgpIPv6EvpnVpws
		return self._select(BgpIPv6EvpnVpws(self), locals())

	def add_BgpIPv6EvpnVpws(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", L3vniImportRtListSameAsL3vniExportRtList="True", Multiplier="1", Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1", NumBroadcastDomainV6="1", NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInL3vniExportRouteTargetList="1", NumRtInL3vniImportRouteTargetList="1", StackedLayers=None):
		"""Adds a child instance of BgpIPv6EvpnVpws on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			L3vniImportRtListSameAsL3vniExportRtList (bool): L3 Import RT List Same As L3 Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			NumBroadcastDomainV6 (number): The number of broadcast domain to be configured under EVI
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInL3vniExportRouteTargetList (number): Number of RTs in L3 Export Route Target List(multiplier)
			NumRtInL3vniImportRouteTargetList (number): Number of RTs in L3 Import Route Target List(multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws.BgpIPv6EvpnVpws)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws import BgpIPv6EvpnVpws
		return self._create(BgpIPv6EvpnVpws(self), locals())

	def BgpIpv6AdL2Vpn(self, Active=None, AsNumberVplsId=None, AsNumberVplsRd=None, AsNumberVplsRt=None, AssignedNumberVplsId=None, AssignedNumberVplsRd=None, AssignedNumberVplsRt=None, Count=None, DescriptiveName=None, ImportRDAsRT=None, ImportVplsIdAsRd=None, IpAddressVplsId=None, IpAddressVplsRd=None, IpAddressVplsRt=None, Multiplier=None, Name=None, NumberVsiId=None, Status=None, TypeVplsId=None, TypeVplsRd=None, TypeVplsRt=None, TypeVsiId=None):
		"""Gets child instances of BgpIpv6AdL2Vpn from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIpv6AdL2Vpn will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AsNumberVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS ID AS Number
			AsNumberVplsRd (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Distinguisher AS Number
			AsNumberVplsRt (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Target AS Number
			AssignedNumberVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS ID Assigned Number
			AssignedNumberVplsRd (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Distinguisher Assigned Number
			AssignedNumberVplsRt (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Target Assigned Number
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ImportRDAsRT (obj(ixnetwork_restpy.multivalue.Multivalue)): Use RD As RT
			ImportVplsIdAsRd (obj(ixnetwork_restpy.multivalue.Multivalue)): Use VPLS ID As Route Distinguisher
			IpAddressVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS ID IP Address
			IpAddressVplsRd (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Distinguisher IP Address
			IpAddressVplsRt (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Target IP Address
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberVsiId (obj(ixnetwork_restpy.multivalue.Multivalue)): VSI ID Number
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TypeVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): VPLS ID Type
			TypeVplsRd (obj(ixnetwork_restpy.multivalue.Multivalue)): RD Type
			TypeVplsRt (obj(ixnetwork_restpy.multivalue.Multivalue)): RT Type
			TypeVsiId (obj(ixnetwork_restpy.multivalue.Multivalue)): VSI ID

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn.BgpIpv6AdL2Vpn))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn import BgpIpv6AdL2Vpn
		return self._select(BgpIpv6AdL2Vpn(self), locals())

	def add_BgpIpv6AdL2Vpn(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of BgpIpv6AdL2Vpn on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn.BgpIpv6AdL2Vpn)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn import BgpIpv6AdL2Vpn
		return self._create(BgpIpv6AdL2Vpn(self), locals())

	def BgpIpv6L2Site(self, Active=None, Count=None, DescriptiveName=None, DistinguishAsNumber=None, DistinguishAssignedNumber=None, DistinguishIpAddr=None, EnCluster=None, EnControlWord=None, EnSeqDelivery=None, MtuL2Site=None, Multiplier=None, Name=None, NumClusterPerL2Site=None, NumL2Sites=None, NumLabelBlocksPerL2Site=None, SiteId=None, Status=None, TargetAsNumber=None, TargetAssignedNumber=None, TargetIpAddr=None, TypeDistinguish=None, TypeTarget=None, VpnName=None):
		"""Gets child instances of BgpIpv6L2Site from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIpv6L2Site will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistinguishAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Distinguish AS Number
			DistinguishAssignedNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Distinguish Assigned Number
			DistinguishIpAddr (obj(ixnetwork_restpy.multivalue.Multivalue)): Distinguish IP Address
			EnCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnControlWord (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Control Word
			EnSeqDelivery (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Sequenced Delivery
			MtuL2Site (obj(ixnetwork_restpy.multivalue.Multivalue)): MTU
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumClusterPerL2Site (number): Number Of Clusters Per L2 Site
			NumL2Sites (obj(ixnetwork_restpy.multivalue.Multivalue)): No. Of L2 Sites
			NumLabelBlocksPerL2Site (number): Number Of Label Blocks Per L2 Site
			SiteId (obj(ixnetwork_restpy.multivalue.Multivalue)): Site ID
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TargetAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Target AS Number
			TargetAssignedNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Target Assigned Number
			TargetIpAddr (obj(ixnetwork_restpy.multivalue.Multivalue)): Target IP Address
			TypeDistinguish (obj(ixnetwork_restpy.multivalue.Multivalue)): Distinguish Type
			TypeTarget (obj(ixnetwork_restpy.multivalue.Multivalue)): Target Type
			VpnName (obj(ixnetwork_restpy.multivalue.Multivalue)): VPN Name

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site.BgpIpv6L2Site))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site import BgpIpv6L2Site
		return self._select(BgpIpv6L2Site(self), locals())

	def add_BgpIpv6L2Site(self, ConnectedVia=None, Multiplier="1", Name=None, NumClusterPerL2Site="1", NumLabelBlocksPerL2Site="1", StackedLayers=None):
		"""Adds a child instance of BgpIpv6L2Site on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumClusterPerL2Site (number): Number Of Clusters Per L2 Site
			NumLabelBlocksPerL2Site (number): Number Of Label Blocks Per L2 Site
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site.BgpIpv6L2Site)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site import BgpIpv6L2Site
		return self._create(BgpIpv6L2Site(self), locals())

	def BgpIpv6MVrf(self, Active=None, Count=None, DescriptiveName=None, ImportRtListSameAsExportRtList=None, IncludePmsiTunnelAttribute=None, MulticastDistinguisherAs4Number=None, MulticastDistinguisherAsNumber=None, MulticastDistinguisherAssignedNumber=None, MulticastDistinguisherIpAddress=None, MulticastDistinguisherType=None, MulticastTunnelType=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, SameAsExportRT=None, SameAsImportRT=None, Status=None, UpOrDownStreamAssignedLabel=None, UseUpOrDownStreamAssigneLabel=None):
		"""Gets child instances of BgpIpv6MVrf from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIpv6MVrf will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			IncludePmsiTunnelAttribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Include PMSI Tunnel Attribute
			MulticastDistinguisherAs4Number (obj(ixnetwork_restpy.multivalue.Multivalue)): VMulticast Distinguisher AS4 Number
			MulticastDistinguisherAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): VMulticast Distinguisher AS Number
			MulticastDistinguisherAssignedNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Distinguisher Assigned Number
			MulticastDistinguisherIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Distinguisher IP Address
			MulticastDistinguisherType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Distinguisher Type
			MulticastTunnelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Multicast Tunnel Type
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			RootAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Root Address
			RsvpP2mpId (obj(ixnetwork_restpy.multivalue.Multivalue)): RSVP P2MP ID
			RsvpP2mpIdAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): RSVP P2MP ID as Number
			RsvpTunnelId (obj(ixnetwork_restpy.multivalue.Multivalue)): RSVP Tunnel ID
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpOrDownStreamAssignedLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Upstream/Downstream Assigned Label
			UseUpOrDownStreamAssigneLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Upstream/Downstream Assigned Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf.BgpIpv6MVrf))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf import BgpIpv6MVrf
		return self._select(BgpIpv6MVrf(self), locals())

	def add_BgpIpv6MVrf(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", Multiplier="1", Name=None, NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInUmhExportRouteTargetList="1", NumRtInUmhImportRouteTargetList="1", SameAsExportRT="True", SameAsImportRT="True", StackedLayers=None):
		"""Adds a child instance of BgpIpv6MVrf on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf.BgpIpv6MVrf)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf import BgpIpv6MVrf
		return self._create(BgpIpv6MVrf(self), locals())

	def BgpLsAsPathSegmentList(self, Count=None, DescriptiveName=None, EnableASPathSegment=None, Name=None, NumberOfAsNumberInSegment=None, SegmentType=None):
		"""Gets child instances of BgpLsAsPathSegmentList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpLsAsPathSegmentList will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableASPathSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segment
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAsNumberInSegment (number): Number of AS Number In Segment
			SegmentType (obj(ixnetwork_restpy.multivalue.Multivalue)): SegmentType

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist.BgpLsAsPathSegmentList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist import BgpLsAsPathSegmentList
		return self._select(BgpLsAsPathSegmentList(self), locals())

	def BgpLsClusterIdList(self, ClusterId=None, Count=None, DescriptiveName=None, Name=None):
		"""Gets child instances of BgpLsClusterIdList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpLsClusterIdList will be returned.

		Args:
			ClusterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Cluster ID
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist.BgpLsClusterIdList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist import BgpLsClusterIdList
		return self._select(BgpLsClusterIdList(self), locals())

	def BgpLsCommunitiesList(self, AsNumber=None, Count=None, DescriptiveName=None, LastTwoOctets=None, Name=None, Type=None):
		"""Gets child instances of BgpLsCommunitiesList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpLsCommunitiesList will be returned.

		Args:
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS #
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LastTwoOctets (obj(ixnetwork_restpy.multivalue.Multivalue)): Last Two Octets
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist.BgpLsCommunitiesList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist import BgpLsCommunitiesList
		return self._select(BgpLsCommunitiesList(self), locals())

	def BgpLsExtendedCommunitiesList(self, AsNumber2Bytes=None, AsNumber4Bytes=None, AssignedNumber2Bytes=None, AssignedNumber4Bytes=None, ColorCOBits=None, ColorReservedBits=None, ColorValue=None, Count=None, DescriptiveName=None, Ip=None, LinkBandwidth=None, Name=None, OpaqueData=None, SubType=None, Type=None):
		"""Gets child instances of BgpLsExtendedCommunitiesList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpLsExtendedCommunitiesList will be returned.

		Args:
			AsNumber2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): AS 2-Bytes
			AsNumber4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): AS 4-Bytes
			AssignedNumber2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Assigned Number(2 Octets)
			AssignedNumber4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Assigned Number(4 Octets)
			ColorCOBits (obj(ixnetwork_restpy.multivalue.Multivalue)): Color CO Bits
			ColorReservedBits (obj(ixnetwork_restpy.multivalue.Multivalue)): Color Reserved Bits
			ColorValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Color Value
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Ip (obj(ixnetwork_restpy.multivalue.Multivalue)): IP
			LinkBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Bandwidth
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OpaqueData (obj(ixnetwork_restpy.multivalue.Multivalue)): Opaque Data
			SubType (obj(ixnetwork_restpy.multivalue.Multivalue)): SubType
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist.BgpLsExtendedCommunitiesList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist import BgpLsExtendedCommunitiesList
		return self._select(BgpLsExtendedCommunitiesList(self), locals())

	def BgpSRGBRangeSubObjectsList(self, Count=None, DescriptiveName=None, Name=None, SIDCount=None, StartSID=None):
		"""Gets child instances of BgpSRGBRangeSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpSRGBRangeSubObjectsList will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SIDCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The size of the SRGB Block
			StartSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Segment ID of the SRGB Block

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist.BgpSRGBRangeSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist import BgpSRGBRangeSubObjectsList
		return self._select(BgpSRGBRangeSubObjectsList(self), locals())

	@property
	def BgpSRTEPoliciesListV6(self):
		"""Returns the one and only one BgpSRTEPoliciesListV6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv6.BgpSRTEPoliciesListV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv6 import BgpSRTEPoliciesListV6
		return self._read(BgpSRTEPoliciesListV6(self), None)

	def BgpV6Vrf(self, Active=None, Count=None, DescriptiveName=None, ImportRtListSameAsExportRtList=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, Status=None):
		"""Gets child instances of BgpV6Vrf from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpV6Vrf will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf.BgpV6Vrf))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf import BgpV6Vrf
		return self._select(BgpV6Vrf(self), locals())

	def add_BgpV6Vrf(self, ConnectedVia=None, ImportRtListSameAsExportRtList="True", Multiplier="1", Name=None, NumRtInExportRouteTargetList="1", NumRtInImportRouteTargetList="1", NumRtInUmhExportRouteTargetList="1", NumRtInUmhImportRouteTargetList="1", SameAsExportRT="True", SameAsImportRT="True", StackedLayers=None):
		"""Adds a child instance of BgpV6Vrf on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf.BgpV6Vrf)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf import BgpV6Vrf
		return self._create(BgpV6Vrf(self), locals())

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

	def LearnedInfo(self, State=None, Type=None):
		"""Gets child instances of LearnedInfo from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LearnedInfo will be returned.

		Args:
			State (str): The state of the learned information query
			Type (str): The type of learned information

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
		return self._select(LearnedInfo(self), locals())

	def TlvProfile(self):
		"""Gets child instances of TlvProfile from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TlvProfile will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile.TlvProfile))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile import TlvProfile
		return self._select(TlvProfile(self), locals())

	@property
	def ActAsRestarted(self):
		"""Act as restarted

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actAsRestarted')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AdvertiseEndOfRib(self):
		"""Advertise End-Of-RIB

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseEndOfRib')

	@property
	def AlwaysIncludeTunnelEncExtCommunity(self):
		"""Always Include Tunnel Encapsulation Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('alwaysIncludeTunnelEncExtCommunity')

	@property
	def AsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSetMode')

	@property
	def Authentication(self):
		"""Authentication Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authentication')

	@property
	def BgpFsmState(self):
		"""Logs additional information about the BGP Peer State

		Returns:
			list(str[active|connect|error|established|idle|none|openConfirm|openSent])
		"""
		return self._get_attribute('bgpFsmState')

	@property
	def BgpId(self):
		"""BGP ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpId')

	@property
	def BgpLsAsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsAsSetMode')

	@property
	def BgpLsEnableAsPathSegments(self):
		"""Enable AS Path Segments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableAsPathSegments')

	@property
	def BgpLsEnableCluster(self):
		"""Enable Cluster

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableCluster')

	@property
	def BgpLsEnableExtendedCommunity(self):
		"""Enable Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableExtendedCommunity')

	@property
	def BgpLsNoOfASPathSegments(self):
		"""Number Of AS Path Segments Per Route Range

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfASPathSegments')
	@BgpLsNoOfASPathSegments.setter
	def BgpLsNoOfASPathSegments(self, value):
		self._set_attribute('bgpLsNoOfASPathSegments', value)

	@property
	def BgpLsNoOfClusters(self):
		"""Number of Clusters

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfClusters')
	@BgpLsNoOfClusters.setter
	def BgpLsNoOfClusters(self, value):
		self._set_attribute('bgpLsNoOfClusters', value)

	@property
	def BgpLsNoOfCommunities(self):
		"""Number of Communities

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfCommunities')
	@BgpLsNoOfCommunities.setter
	def BgpLsNoOfCommunities(self, value):
		self._set_attribute('bgpLsNoOfCommunities', value)

	@property
	def BgpLsOverridePeerAsSetMode(self):
		"""Override Peer AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsOverridePeerAsSetMode')

	@property
	def CapabilityIpV4Mdt(self):
		"""IPv4 MDT

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Mdt')

	@property
	def CapabilityIpV4Mpls(self):
		"""IPv4 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Mpls')

	@property
	def CapabilityIpV4MplsVpn(self):
		"""IPv4 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4MplsVpn')

	@property
	def CapabilityIpV4Multicast(self):
		"""IPv4 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Multicast')

	@property
	def CapabilityIpV4MulticastVpn(self):
		"""IPv4 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4MulticastVpn')

	@property
	def CapabilityIpV4Unicast(self):
		"""IPv4 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Unicast')

	@property
	def CapabilityIpV6Mpls(self):
		"""IPv6 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Mpls')

	@property
	def CapabilityIpV6MplsVpn(self):
		"""IPv6 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6MplsVpn')

	@property
	def CapabilityIpV6Multicast(self):
		"""IPv6 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Multicast')

	@property
	def CapabilityIpV6MulticastVpn(self):
		"""IPv6 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6MulticastVpn')

	@property
	def CapabilityIpV6Unicast(self):
		"""IPv6 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Unicast')

	@property
	def CapabilityIpv4MplsAddPath(self):
		"""IPv4 MPLS Add Path Capability

		Returns:
			bool
		"""
		return self._get_attribute('capabilityIpv4MplsAddPath')
	@CapabilityIpv4MplsAddPath.setter
	def CapabilityIpv4MplsAddPath(self, value):
		self._set_attribute('capabilityIpv4MplsAddPath', value)

	@property
	def CapabilityIpv4UnicastAddPath(self):
		"""Check box for IPv4 Unicast Add Path

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpv4UnicastAddPath')

	@property
	def CapabilityIpv6MplsAddPath(self):
		"""IPv6 MPLS Add Path Capability

		Returns:
			bool
		"""
		return self._get_attribute('capabilityIpv6MplsAddPath')
	@CapabilityIpv6MplsAddPath.setter
	def CapabilityIpv6MplsAddPath(self, value):
		self._set_attribute('capabilityIpv6MplsAddPath', value)

	@property
	def CapabilityIpv6UnicastAddPath(self):
		"""Check box for IPv6 Unicast Add Path

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpv6UnicastAddPath')

	@property
	def CapabilityLinkStateNonVpn(self):
		"""Link State Non-VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityLinkStateNonVpn')

	@property
	def CapabilityNHEncodingCapabilities(self):
		"""Extended Next Hop Encoding Capability

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityNHEncodingCapabilities')

	@property
	def CapabilityRouteConstraint(self):
		"""Route Constraint

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityRouteConstraint')

	@property
	def CapabilityRouteRefresh(self):
		"""Route Refresh

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityRouteRefresh')

	@property
	def CapabilitySRTEPoliciesV4(self):
		"""Enable IPv4 SR TE Policy Capability

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitySRTEPoliciesV4')

	@property
	def CapabilitySRTEPoliciesV6(self):
		"""Enable IPv6 SR TE Policy Capability

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitySRTEPoliciesV6')

	@property
	def CapabilityVpls(self):
		"""VPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityVpls')

	@property
	def Capabilityipv4UnicastFlowSpec(self):
		"""IPv4 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityipv4UnicastFlowSpec')

	@property
	def Capabilityipv6UnicastFlowSpec(self):
		"""IPv6 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityipv6UnicastFlowSpec')

	@property
	def ConfigureKeepaliveTimer(self):
		"""Configure Keepalive Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureKeepaliveTimer')

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
	def CopyTtl(self):
		"""Copy TTL from customer packet to outer IPv6 header

		Returns:
			bool
		"""
		return self._get_attribute('copyTtl')
	@CopyTtl.setter
	def CopyTtl(self, value):
		self._set_attribute('copyTtl', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def CustomSidType(self):
		"""moved to port data in bgp/srv6 Custom SID Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('customSidType')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DiscardIxiaGeneratedRoutes(self):
		"""Discard Ixia Generated Routes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('discardIxiaGeneratedRoutes')

	@property
	def DowntimeInSec(self):
		"""Downtime in Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downtimeInSec')

	@property
	def DutIp(self):
		"""DUT IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dutIp')

	@property
	def EnSRv6DataPlane(self):
		"""Ingress Peer Supports SRv6 VPN

		Returns:
			bool
		"""
		return self._get_attribute('enSRv6DataPlane')
	@EnSRv6DataPlane.setter
	def EnSRv6DataPlane(self, value):
		self._set_attribute('enSRv6DataPlane', value)

	@property
	def Enable4ByteAs(self):
		"""Enable 4-Byte AS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enable4ByteAs')

	@property
	def EnableBfdRegistration(self):
		"""Enable BFD Registration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBfdRegistration')

	@property
	def EnableBgpId(self):
		"""Enable BGP ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpId')

	@property
	def EnableBgpIdSameAsRouterId(self):
		"""BGP ID Same as Router ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpIdSameAsRouterId')

	@property
	def EnableBgpLsCommunity(self):
		"""Enable Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpLsCommunity')

	@property
	def EnableEPETraffic(self):
		"""Enable EPE Traffic

		Returns:
			bool
		"""
		return self._get_attribute('enableEPETraffic')
	@EnableEPETraffic.setter
	def EnableEPETraffic(self, value):
		self._set_attribute('enableEPETraffic', value)

	@property
	def EnableGracefulRestart(self):
		"""Enable Graceful Restart

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGracefulRestart')

	@property
	def EnableLlgr(self):
		"""Enable LLGR

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLlgr')

	@property
	def EnableReducedEncapsulation(self):
		"""Enable Reduced Encapsulation in Data-Plane for SRv6

		Returns:
			bool
		"""
		return self._get_attribute('enableReducedEncapsulation')
	@EnableReducedEncapsulation.setter
	def EnableReducedEncapsulation(self, value):
		self._set_attribute('enableReducedEncapsulation', value)

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def EthernetSegmentsCountV6(self):
		"""Number of Ethernet Segments

		Returns:
			number
		"""
		return self._get_attribute('ethernetSegmentsCountV6')
	@EthernetSegmentsCountV6.setter
	def EthernetSegmentsCountV6(self, value):
		self._set_attribute('ethernetSegmentsCountV6', value)

	@property
	def Evpn(self):
		"""Check box for EVPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('evpn')

	@property
	def FilterEvpn(self):
		"""Check box for EVPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterEvpn')

	@property
	def FilterIpV4Mpls(self):
		"""Filter IPv4 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Mpls')

	@property
	def FilterIpV4MplsVpn(self):
		"""Filter IPv4 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4MplsVpn')

	@property
	def FilterIpV4Multicast(self):
		"""Filter IPv4 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Multicast')

	@property
	def FilterIpV4MulticastVpn(self):
		"""Filter IPv4 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4MulticastVpn')

	@property
	def FilterIpV4Unicast(self):
		"""Filter IPv4 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Unicast')

	@property
	def FilterIpV6Mpls(self):
		"""Filter IPv6 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Mpls')

	@property
	def FilterIpV6MplsVpn(self):
		"""Filter IPv6 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6MplsVpn')

	@property
	def FilterIpV6Multicast(self):
		"""Filter IPv6 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Multicast')

	@property
	def FilterIpV6MulticastVpn(self):
		"""Filter IPv6 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6MulticastVpn')

	@property
	def FilterIpV6Unicast(self):
		"""Filter IPv6 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Unicast')

	@property
	def FilterIpv4MulticastBgpMplsVpn(self):
		"""Check box for IPv4 Multicast BGP/MPLS VPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv4MulticastBgpMplsVpn')

	@property
	def FilterIpv4UnicastFlowSpec(self):
		"""Filter IPv4 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv4UnicastFlowSpec')

	@property
	def FilterIpv6MulticastBgpMplsVpn(self):
		"""Check box for IPv6 Multicast BGP/MPLS VPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv6MulticastBgpMplsVpn')

	@property
	def FilterIpv6UnicastFlowSpec(self):
		"""Filter IPv6 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv6UnicastFlowSpec')

	@property
	def FilterLinkState(self):
		"""Filter Link State

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterLinkState')

	@property
	def FilterSRTEPoliciesV4(self):
		"""Enable IPv4 SR TE Policy Filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterSRTEPoliciesV4')

	@property
	def FilterSRTEPoliciesV6(self):
		"""Enable IPv6 SR TE Policy Filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterSRTEPoliciesV6')

	@property
	def FilterVpls(self):
		"""Filter VPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterVpls')

	@property
	def Flap(self):
		"""Flap

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flap')

	@property
	def HoldTimer(self):
		"""Hold Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdTimer')

	@property
	def IpVrfToIpVrfType(self):
		"""IP-VRF-to-IP-VRF Model Type

		Returns:
			str(interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB|interfaceLess)
		"""
		return self._get_attribute('ipVrfToIpVrfType')
	@IpVrfToIpVrfType.setter
	def IpVrfToIpVrfType(self, value):
		self._set_attribute('ipVrfToIpVrfType', value)

	@property
	def Ipv4MplsAddPathMode(self):
		"""IPv4 MPLS Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4MplsAddPathMode')

	@property
	def Ipv4MplsCapability(self):
		"""IPv4 MPLS Capability

		Returns:
			bool
		"""
		return self._get_attribute('ipv4MplsCapability')
	@Ipv4MplsCapability.setter
	def Ipv4MplsCapability(self, value):
		self._set_attribute('ipv4MplsCapability', value)

	@property
	def Ipv4MulticastBgpMplsVpn(self):
		"""Check box for IPv4 Multicast BGP/MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4MulticastBgpMplsVpn')

	@property
	def Ipv4MultipleMplsLabelsCapability(self):
		"""IPv4 Multiple MPLS Labels Capability

		Returns:
			bool
		"""
		return self._get_attribute('ipv4MultipleMplsLabelsCapability')
	@Ipv4MultipleMplsLabelsCapability.setter
	def Ipv4MultipleMplsLabelsCapability(self, value):
		self._set_attribute('ipv4MultipleMplsLabelsCapability', value)

	@property
	def Ipv4UnicastAddPathMode(self):
		"""IPv4 Unicast Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4UnicastAddPathMode')

	@property
	def Ipv6MplsAddPathMode(self):
		"""IPv6 MPLS Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6MplsAddPathMode')

	@property
	def Ipv6MplsCapability(self):
		"""IPv6 MPLS Capability

		Returns:
			bool
		"""
		return self._get_attribute('ipv6MplsCapability')
	@Ipv6MplsCapability.setter
	def Ipv6MplsCapability(self, value):
		self._set_attribute('ipv6MplsCapability', value)

	@property
	def Ipv6MulticastBgpMplsVpn(self):
		"""Check box for IPv6 Multicast BGP/MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6MulticastBgpMplsVpn')

	@property
	def Ipv6MultipleMplsLabelsCapability(self):
		"""IPv6 Multiple MPLS Labels Capability

		Returns:
			bool
		"""
		return self._get_attribute('ipv6MultipleMplsLabelsCapability')
	@Ipv6MultipleMplsLabelsCapability.setter
	def Ipv6MultipleMplsLabelsCapability(self, value):
		self._set_attribute('ipv6MultipleMplsLabelsCapability', value)

	@property
	def Ipv6UnicastAddPathMode(self):
		"""IPv6 Unicast Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6UnicastAddPathMode')

	@property
	def IrbInterfaceLabel(self):
		"""Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('irbInterfaceLabel')

	@property
	def IrbIpv6Address(self):
		"""IRB IPv6 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('irbIpv6Address')

	@property
	def KeepaliveTimer(self):
		"""Keepalive Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('keepaliveTimer')

	@property
	def LocalAs2Bytes(self):
		"""Local AS# (2-Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localAs2Bytes')

	@property
	def LocalAs4Bytes(self):
		"""Local AS# (4-Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localAs4Bytes')

	@property
	def LocalIpv6Ver2(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIpv6Ver2')

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

	@property
	def MaxSidPerSrh(self):
		"""Max number of SIDs a SRH can have

		Returns:
			number
		"""
		return self._get_attribute('maxSidPerSrh')
	@MaxSidPerSrh.setter
	def MaxSidPerSrh(self, value):
		self._set_attribute('maxSidPerSrh', value)

	@property
	def Md5Key(self):
		"""MD5 Key

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('md5Key')

	@property
	def ModeOfBfdOperations(self):
		"""Mode of BFD Operations

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('modeOfBfdOperations')

	@property
	def MplsLabelsCountForIpv4MplsRoute(self):
		"""MPLS Labels Count For IPv4 MPLS Route

		Returns:
			number
		"""
		return self._get_attribute('mplsLabelsCountForIpv4MplsRoute')
	@MplsLabelsCountForIpv4MplsRoute.setter
	def MplsLabelsCountForIpv4MplsRoute(self, value):
		self._set_attribute('mplsLabelsCountForIpv4MplsRoute', value)

	@property
	def MplsLabelsCountForIpv6MplsRoute(self):
		"""MPLS Labels Count For IPv6 MPLS Route

		Returns:
			number
		"""
		return self._get_attribute('mplsLabelsCountForIpv6MplsRoute')
	@MplsLabelsCountForIpv6MplsRoute.setter
	def MplsLabelsCountForIpv6MplsRoute(self, value):
		self._set_attribute('mplsLabelsCountForIpv6MplsRoute', value)

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
	def NoOfEPEPeers(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('noOfEPEPeers')
	@NoOfEPEPeers.setter
	def NoOfEPEPeers(self, value):
		self._set_attribute('noOfEPEPeers', value)

	@property
	def NoOfExtendedCommunities(self):
		"""Number of Extended Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfExtendedCommunities')
	@NoOfExtendedCommunities.setter
	def NoOfExtendedCommunities(self, value):
		self._set_attribute('noOfExtendedCommunities', value)

	@property
	def NoOfPeerSet(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('noOfPeerSet')
	@NoOfPeerSet.setter
	def NoOfPeerSet(self, value):
		self._set_attribute('noOfPeerSet', value)

	@property
	def NoOfUserDefinedAfiSafi(self):
		"""Count of User defined AFI SAFI

		Returns:
			number
		"""
		return self._get_attribute('noOfUserDefinedAfiSafi')
	@NoOfUserDefinedAfiSafi.setter
	def NoOfUserDefinedAfiSafi(self, value):
		self._set_attribute('noOfUserDefinedAfiSafi', value)

	@property
	def NumBgpLsId(self):
		"""BGP LS Instance ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpLsId')

	@property
	def NumBgpLsInstanceIdentifier(self):
		"""IGP Multi instance unique identifier. 0 is default single-instance IGP. (e.g. for OSPFv3 it is possible to separately run 4 instances of OSPFv3 with peer, one advertising v4 only, another v6 only and other 2 mcast v4 and v6 respectively) .

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpLsInstanceIdentifier')

	@property
	def NumBgpUpdatesGeneratedPerIteration(self):
		"""Num BGP Updates Generated Per Iteration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpUpdatesGeneratedPerIteration')

	@property
	def NumberFlowSpecRangeV4(self):
		"""Number of IPv4 Flow Spec Ranges

		Returns:
			number
		"""
		return self._get_attribute('numberFlowSpecRangeV4')
	@NumberFlowSpecRangeV4.setter
	def NumberFlowSpecRangeV4(self, value):
		self._set_attribute('numberFlowSpecRangeV4', value)

	@property
	def NumberFlowSpecRangeV6(self):
		"""Number of IPv6 Flow Spec Ranges

		Returns:
			number
		"""
		return self._get_attribute('numberFlowSpecRangeV6')
	@NumberFlowSpecRangeV6.setter
	def NumberFlowSpecRangeV6(self, value):
		self._set_attribute('numberFlowSpecRangeV6', value)

	@property
	def NumberSRTEPolicies(self):
		"""Count of SR TE Policies

		Returns:
			number
		"""
		return self._get_attribute('numberSRTEPolicies')
	@NumberSRTEPolicies.setter
	def NumberSRTEPolicies(self, value):
		self._set_attribute('numberSRTEPolicies', value)

	@property
	def OperationalModel(self):
		"""Operational Model

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('operationalModel')

	@property
	def RestartTime(self):
		"""Restart Time

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('restartTime')

	@property
	def RoutersMacOrIrbMacAddress(self):
		"""Router's MAC/IRB MAC Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routersMacOrIrbMacAddress')

	@property
	def SRGBRangeCount(self):
		"""SRGB Range Count

		Returns:
			number
		"""
		return self._get_attribute('sRGBRangeCount')
	@SRGBRangeCount.setter
	def SRGBRangeCount(self, value):
		self._set_attribute('sRGBRangeCount', value)

	@property
	def SendIxiaSignatureWithRoutes(self):
		"""Send Ixia Signature With Routes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendIxiaSignatureWithRoutes')

	@property
	def SessionInfo(self):
		"""Logs additional information about the session state

		Returns:
			list(str[aSRoutingLoopErrorRx|attributeFlagErrorRx|attributesLengthErrorRx|authenticationFailureErrorRx|badBGPIdentifierErrorRx|badMessageLengthErrorRx|badMessageTypeErrorRx|badPeerASErrorRx|bGPHeaderErrorRx|bGPHeaderErrorTx|bGPHoldTimerExpiredErrorRx|bGPOpenPacketErrorRx|bGPStateMachineErrorRx|bGPUpdatePacketErrorRx|ceaseErrorRx|ceaseNotificationErrorTx|connectionNotsynchronizedErrorRx|holdtimeExpiredErrorTx|invalidASPathErrorRx|invalidNetworkFieldErrorRx|invalidNextHopAttributeErrorRx|invalidOriginAttributeErrorRx|malformedAttributeListErrorRx|missingWellKnownAttributeErrorRx|none|openPacketErrTx|optionalAttributeErrorRx|stateMachineErrorTx|unacceptableHoldTimeErrorRx|unrecognizedWellKnownAttributeErrorRx|unspecifiedErrorRx|unspecifiedErrorTx|unspecifiedSubcodeErrorRx|unsupportedOptionalParameterErrorRx|unsupportedversionNumberErrorRx|updatePacketErrorTx])
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
	def Srv6Ttl(self):
		"""TTL value to be used in outer IPv6 header

		Returns:
			number
		"""
		return self._get_attribute('srv6Ttl')
	@Srv6Ttl.setter
	def Srv6Ttl(self, value):
		self._set_attribute('srv6Ttl', value)

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
	def StaleTime(self):
		"""Stale Time/ LLGR Stale Time

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('staleTime')

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
	def TcpWindowSizeInBytes(self):
		"""TCP Window Size (in bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tcpWindowSizeInBytes')

	@property
	def Ttl(self):
		"""TTL

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ttl')

	@property
	def Type(self):
		"""Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('type')

	@property
	def UpdateInterval(self):
		"""Update Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('updateInterval')

	@property
	def UptimeInSec(self):
		"""Uptime in Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('uptimeInSec')

	@property
	def UseStaticPolicy(self):
		"""If enabled then SRTE policy will be advertised

		Returns:
			bool
		"""
		return self._get_attribute('useStaticPolicy')
	@UseStaticPolicy.setter
	def UseStaticPolicy(self, value):
		self._set_attribute('useStaticPolicy', value)

	@property
	def VplsEnableNextHop(self):
		"""VPLS Enable Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vplsEnableNextHop')

	@property
	def VplsNextHop(self):
		"""VPLS Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vplsNextHop')

	def remove(self):
		"""Deletes a child instance of BgpIpv6Peer on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def BgpIPv4FlowSpecLearnedInfo(self, Arg1):
		"""Executes the bgpIPv4FlowSpecLearnedInfo operation on the server.

		Get IPv4 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv4FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BgpIPv4FlowSpecLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the bgpIPv4FlowSpecLearnedInfo operation on the server.

		Get IPv4 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv4FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BgpIPv4FlowSpecLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the bgpIPv4FlowSpecLearnedInfo operation on the server.

		Get IPv4 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv4FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BgpIPv6FlowSpecLearnedInfo(self, Arg1):
		"""Executes the bgpIPv6FlowSpecLearnedInfo operation on the server.

		Get IPv6 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv6FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BgpIPv6FlowSpecLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the bgpIPv6FlowSpecLearnedInfo operation on the server.

		Get IPv6 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv6FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BgpIPv6FlowSpecLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the bgpIPv6FlowSpecLearnedInfo operation on the server.

		Get IPv6 FlowSpec Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('bgpIPv6FlowSpecLearnedInfo', payload=locals(), response_object=None)

	def BreakTCPSession(self, Arg1, Notification_code, Notification_sub_code):
		"""Executes the breakTCPSession operation on the server.

		Break TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Notification_code (number): This parameter requires a notification_code of type kInteger
			Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('breakTCPSession', payload=locals(), response_object=None)

	def BreakTCPSession(self, Arg1, Notification_code, Notification_sub_code, SessionIndices):
		"""Executes the breakTCPSession operation on the server.

		Break TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Notification_code (number): This parameter requires a notification_code of type kInteger
			Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('breakTCPSession', payload=locals(), response_object=None)

	def BreakTCPSession(self, Arg1, SessionIndices, Notification_code, Notification_sub_code):
		"""Executes the breakTCPSession operation on the server.

		Break TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a notification_code of type kInteger
			Notification_code (number): This parameter requires a notification_sub_code of type kInteger
			Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('breakTCPSession', payload=locals(), response_object=None)

	def Breaktcpsession(self, Arg2, Arg3, Arg4):
		"""Executes the breaktcpsession operation on the server.

		Break BGP Peer Range TCP Session.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
			Arg3 (number): Notification Code
			Arg4 (number): Notification Sub Code

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('breaktcpsession', payload=locals(), response_object=None)

	def ClearAllLearnedInfo(self, Arg1):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfoInClient(self, Arg2):
		"""Executes the clearAllLearnedInfoInClient operation on the server.

		Clears ALL routes from GUI grid for the selected BGP Peers.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('clearAllLearnedInfoInClient', payload=locals(), response_object=None)

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

	def GetADVPLSLearnedInfo(self, Arg1):
		"""Executes the getADVPLSLearnedInfo operation on the server.

		Get ADVPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getADVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetADVPLSLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getADVPLSLearnedInfo operation on the server.

		Get ADVPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getADVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetADVPLSLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getADVPLSLearnedInfo operation on the server.

		Get ADVPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getADVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetADVPLSLearnedInfo(self, Arg2):
		"""Executes the getADVPLSLearnedInfo operation on the server.

		Fetches AD-VPLS routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getADVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg1):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg2):
		"""Executes the getAllLearnedInfo operation on the server.

		Gets ALL routes learnt and stored by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetbgpIpv4FlowSpecLearnedInfoLearnedInfo(self, Arg2):
		"""Executes the getbgpIpv4FlowSpecLearnedInfoLearnedInfo operation on the server.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

		Returns:
			list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getbgpIpv4FlowSpecLearnedInfoLearnedInfo', payload=locals(), response_object=None)

	def GetbgpIpv6FlowSpecLearnedInfoLearnedInfo(self, Arg2):
		"""Executes the getbgpIpv6FlowSpecLearnedInfoLearnedInfo operation on the server.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

		Returns:
			list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getbgpIpv6FlowSpecLearnedInfoLearnedInfo', payload=locals(), response_object=None)

	def GetbgpSrTeLearnedInfoLearnedInfo(self, Arg2):
		"""Executes the getbgpSrTeLearnedInfoLearnedInfo operation on the server.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

		Returns:
			list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getbgpSrTeLearnedInfoLearnedInfo', payload=locals(), response_object=None)

	def GetEVPNLearnedInfo(self, Arg1):
		"""Executes the getEVPNLearnedInfo operation on the server.

		Get EVPN Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getEVPNLearnedInfo', payload=locals(), response_object=None)

	def GetEVPNLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getEVPNLearnedInfo operation on the server.

		Get EVPN Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getEVPNLearnedInfo', payload=locals(), response_object=None)

	def GetEVPNLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getEVPNLearnedInfo operation on the server.

		Get EVPN Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getEVPNLearnedInfo', payload=locals(), response_object=None)

	def GetEVPNLearnedInfo(self, Arg2):
		"""Executes the getEVPNLearnedInfo operation on the server.

		Fetches EVPN MAC IP routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getEVPNLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4LearnedInfo(self, Arg1):
		"""Executes the getIPv4LearnedInfo operation on the server.

		Get IPv4 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4LearnedInfo', payload=locals(), response_object=None)

	def GetIPv4LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4LearnedInfo operation on the server.

		Get IPv4 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4LearnedInfo', payload=locals(), response_object=None)

	def GetIPv4LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4LearnedInfo operation on the server.

		Get IPv4 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4LearnedInfo', payload=locals(), response_object=None)

	def GetIPv4LearnedInfo(self, Arg2):
		"""Executes the getIPv4LearnedInfo operation on the server.

		Fetches IPv4 routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv4LearnedInfo', payload=locals(), response_object=None)

	def GetIPv4MplsLearnedInfo(self, Arg2):
		"""Executes the getIPv4MplsLearnedInfo operation on the server.

		Fetches IPv4 MPLS routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv4MplsLearnedInfo', payload=locals(), response_object=None)

	def GetIpv4MvpnLearnedInfo(self, Arg2):
		"""Executes the getIpv4MvpnLearnedInfo operation on the server.

		Fetches MVPN MAC IP routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIpv4MvpnLearnedInfo', payload=locals(), response_object=None)

	def GetIpv4UmhRoutesLearnedInfo(self, Arg2):
		"""Executes the getIpv4UmhRoutesLearnedInfo operation on the server.

		Fetches Umh Routes learned by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIpv4UmhRoutesLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4VpnLearnedInfo(self, Arg1):
		"""Executes the getIPv4VpnLearnedInfo operation on the server.

		Get IPv4 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4VpnLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4VpnLearnedInfo operation on the server.

		Get IPv4 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4VpnLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4VpnLearnedInfo operation on the server.

		Get IPv4 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4VpnLearnedInfo(self, Arg2):
		"""Executes the getIPv4VpnLearnedInfo operation on the server.

		Fetches IPv4 VPN routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv4VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6LearnedInfo(self, Arg1):
		"""Executes the getIPv6LearnedInfo operation on the server.

		Get IPv6 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6LearnedInfo', payload=locals(), response_object=None)

	def GetIPv6LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6LearnedInfo operation on the server.

		Get IPv6 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6LearnedInfo', payload=locals(), response_object=None)

	def GetIPv6LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6LearnedInfo operation on the server.

		Get IPv6 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6LearnedInfo', payload=locals(), response_object=None)

	def GetIPv6LearnedInfo(self, Arg2):
		"""Executes the getIPv6LearnedInfo operation on the server.

		Gets IPv6 routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv6LearnedInfo', payload=locals(), response_object=None)

	def GetIPv6MplsLearnedInfo(self, Arg2):
		"""Executes the getIPv6MplsLearnedInfo operation on the server.

		Gets IPv6 Mpls routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv6MplsLearnedInfo', payload=locals(), response_object=None)

	def GetIpv6MvpnLearnedInfo(self, Arg2):
		"""Executes the getIpv6MvpnLearnedInfo operation on the server.

		Fetches MVPN MAC IP routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIpv6MvpnLearnedInfo', payload=locals(), response_object=None)

	def GetIpv6UmhRoutesLearnedInfo(self, Arg2):
		"""Executes the getIpv6UmhRoutesLearnedInfo operation on the server.

		Fetches Umh Route learned by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIpv6UmhRoutesLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6VpnLearnedInfo(self, Arg1):
		"""Executes the getIPv6VpnLearnedInfo operation on the server.

		Get IPv6 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6VpnLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6VpnLearnedInfo operation on the server.

		Get IPv6 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6VpnLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6VpnLearnedInfo operation on the server.

		Get IPv6 Vpn Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6VpnLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6VpnLearnedInfo(self, Arg2):
		"""Executes the getIPv6VpnLearnedInfo operation on the server.

		Gets IPv6 VPN routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv6VpnLearnedInfo', payload=locals(), response_object=None)

	def GetLinkStateLearnedInfo(self, Arg1):
		"""Executes the getLinkStateLearnedInfo operation on the server.

		Get Link State Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getLinkStateLearnedInfo', payload=locals(), response_object=None)

	def GetLinkStateLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getLinkStateLearnedInfo operation on the server.

		Get Link State Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getLinkStateLearnedInfo', payload=locals(), response_object=None)

	def GetLinkStateLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getLinkStateLearnedInfo operation on the server.

		Get Link State Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getLinkStateLearnedInfo', payload=locals(), response_object=None)

	def GetLinkStateLearnedInfo(self, Arg2):
		"""Executes the getLinkStateLearnedInfo operation on the server.

		Fetches Link State Information learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getLinkStateLearnedInfo', payload=locals(), response_object=None)

	def GetVPLSLearnedInfo(self, Arg1):
		"""Executes the getVPLSLearnedInfo operation on the server.

		Get VPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetVPLSLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getVPLSLearnedInfo operation on the server.

		Get VPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetVPLSLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getVPLSLearnedInfo operation on the server.

		Get VPLS Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getVPLSLearnedInfo', payload=locals(), response_object=None)

	def GetVPLSLearnedInfo(self, Arg2):
		"""Executes the getVPLSLearnedInfo operation on the server.

		Fetches VPLS routes learnt by this BGP peer.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getVPLSLearnedInfo', payload=locals(), response_object=None)

	def GracefulRestart(self, Arg1, Restart_time):
		"""Executes the gracefulRestart operation on the server.

		Graceful restart Peers on selected Peer Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Restart_time (number): This parameter requires a restart_time of type kInteger

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefulRestart', payload=locals(), response_object=None)

	def GracefulRestart(self, Arg1, Restart_time, SessionIndices):
		"""Executes the gracefulRestart operation on the server.

		Graceful restart Peers on selected Peer Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Restart_time (number): This parameter requires a restart_time of type kInteger
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefulRestart', payload=locals(), response_object=None)

	def GracefulRestart(self, Arg1, SessionIndices, Restart_time):
		"""Executes the gracefulRestart operation on the server.

		Graceful restart Peers on selected Peer Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a restart_time of type kInteger
			Restart_time (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefulRestart', payload=locals(), response_object=None)

	def Gracefulrestart(self, Arg2, Arg3):
		"""Executes the gracefulrestart operation on the server.

		Graceful restart Peers on selected Peer Ranges.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
			Arg3 (number): Restart After Time(in secs).

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('gracefulrestart', payload=locals(), response_object=None)

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1, SessionIndices):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1, SessionIndices):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def Resumekeepalive(self, Arg2):
		"""Executes the resumekeepalive operation on the server.

		Start Sending Keep Alive Messages.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('resumekeepalive', payload=locals(), response_object=None)

	def ResumeTCPSession(self, Arg1, Notification_code, Notification_sub_code):
		"""Executes the resumeTCPSession operation on the server.

		Resume TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Notification_code (number): This parameter requires a notification_code of type kInteger
			Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeTCPSession', payload=locals(), response_object=None)

	def ResumeTCPSession(self, Arg1, Notification_code, Notification_sub_code, SessionIndices):
		"""Executes the resumeTCPSession operation on the server.

		Resume TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			Notification_code (number): This parameter requires a notification_code of type kInteger
			Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeTCPSession', payload=locals(), response_object=None)

	def ResumeTCPSession(self, Arg1, SessionIndices, Notification_code, Notification_sub_code):
		"""Executes the resumeTCPSession operation on the server.

		Resume TCP Session

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a notification_code of type kInteger
			Notification_code (number): This parameter requires a notification_sub_code of type kInteger
			Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeTCPSession', payload=locals(), response_object=None)

	def Resumetcpsession(self, Arg2, Arg3, Arg4):
		"""Executes the resumetcpsession operation on the server.

		Resume BGP Peer Range TCP Session.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
			Arg3 (number): Notification Code
			Arg4 (number): Notification Sub Code

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('resumetcpsession', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop BGP Peer

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1, SessionIndices):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1, SessionIndices):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpIpv6Peer object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def Stopkeepalive(self, Arg2):
		"""Executes the stopkeepalive operation on the server.

		Stop Sending Keep Alive Messages.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopkeepalive', payload=locals(), response_object=None)
