from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NetworkGroup(Base):
	"""Describes a set of network clouds with similar configuration and the same multiplicity for devices behind.
	"""

	_SDM_NAME = 'networkGroup'

	def __init__(self, parent):
		super(NetworkGroup, self).__init__(parent)

	def BgpIPRouteProperty(self, OverridePeerAsSetMode=None, Active=None, AddPathId=None, AdvertiseAsBGPLSPrefix=None, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Count=None, Delay=None, DescriptiveName=None, Downtime=None, EnableAddPath=None, EnableAggregatorId=None, EnableAigp=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSRGB=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncrementMode=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, Name=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfTlvs=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, RouteOrigin=None, SegmentId=None, SendMulticastWithProperSAFI=None, SkipMulticast=None, SpecialLabel=None, Uptime=None, UseTraditionalNlri=None, Weight=None):
		"""Gets child instances of BgpIPRouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpIPRouteProperty will be returned.

		Args:
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AddPathId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP ADD Path Id
			AdvertiseAsBGPLSPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise as BGP-LS Prefix
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			AdvertiseNexthopAsV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise Nexthop as V4
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AggregatorIdMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID Mode
			AsNumSuffixRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
			AsPathPerRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
			AsRandomSeed (obj(ixnetwork_restpy.multivalue.Multivalue)): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
			AsSegDist (obj(ixnetwork_restpy.multivalue.Multivalue)): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Delay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Downtime (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime In Seconds
			EnableAddPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Path ID when ADD Path Capability is enabled in BGP Peer
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAigp (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AIGP
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Non-Random AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableFlapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Flapping
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EnableRandomAsPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables generation/advertisement of Random AS Path Segments.
			EnableSRGB (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable SRGB TLV
			EnableWeight (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Weight
			FlapFromRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap From Route Index
			FlapToRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap To Route Index
			IncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Either Fixed or Increment
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label End
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MaxASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Numbers generated per Segment
			MaxNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Path Segments Per Route Range.
			MinASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Numbers generated per Segments.
			MinNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Path Segments Per Route Range.
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NextHopIPType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			NextHopIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Next Hop Increment Mode
			NextHopType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfTlvs (number): Number of TLVs
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			PackingFrom (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing From
			PackingTo (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing To
			PartialFlap (obj(ixnetwork_restpy.multivalue.Multivalue)): Partial Flap
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			SegmentId (obj(ixnetwork_restpy.multivalue.Multivalue)): SID or Segment ID, converts to label value by adding offset into SRGB Start Label Value.
			SendMulticastWithProperSAFI (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Routes with SAFI as Multicast (2)
			SkipMulticast (obj(ixnetwork_restpy.multivalue.Multivalue)): Skip the Multicast routes for this route range
			SpecialLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): If we are emulating Egress then Label field may not hold Label value calculated based on SRGB and Offset but Implicit IPv4 NULL or Explicit NULL
			Uptime (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime In Seconds
			UseTraditionalNlri (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Traditional NLRI
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty.BgpIPRouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty import BgpIPRouteProperty
		return self._select(BgpIPRouteProperty(self), locals())

	def add_BgpIPRouteProperty(self, AdvertiseAsBgp3107="False", AdvertiseAsBgp3107Sr="False", AdvertiseAsRfc8277="False", Name=None, NoOfASPathSegmentsPerRouteRange="1", NoOfClusters="1", NoOfCommunities="1", NoOfExternalCommunities="1", NoOfLabels="1", NoOfTlvs="1"):
		"""Adds a child instance of BgpIPRouteProperty on the server.

		Args:
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfTlvs (number): Number of TLVs

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty.BgpIPRouteProperty)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty import BgpIPRouteProperty
		return self._create(BgpIPRouteProperty(self), locals())

	def BgpL3VpnRouteProperty(self, OverridePeerAsSetMode=None, Active=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Count=None, Delay=None, DescriptiveName=None, DistinguisherAsNumber=None, DistinguisherAssignedNumber=None, DistinguisherIpAddress=None, DistinguisherType=None, Downtime=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableIpv4Receiver=None, EnableIpv4Sender=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncludeRdInNextHopLength=None, IncludeSourceAsExtComm=None, IncludeVrfRouteImportExtComm=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelMode=None, LabelSpaceId=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, Name=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, Uptime=None, UseAsIpv4UmhRoutes=None, UseAsUmhRoutes=None, UseTraditionalNlri=None, Weight=None):
		"""Gets child instances of BgpL3VpnRouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpL3VpnRouteProperty will be returned.

		Args:
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseNexthopAsV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise Nexthop as V4
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AggregatorIdMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID Mode
			AsNumSuffixRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
			AsPathPerRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
			AsRandomSeed (obj(ixnetwork_restpy.multivalue.Multivalue)): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
			AsSegDist (obj(ixnetwork_restpy.multivalue.Multivalue)): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Delay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistinguisherAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher AS Number (2-byte or 4-Byte)
			DistinguisherAssignedNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher Assigned Number
			DistinguisherIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher IP Address
			DistinguisherType (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher Type
			Downtime (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime In Seconds
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Non-Random AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableFlapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Flapping
			EnableIpv4Receiver (bool): Enable IPv4 Receiver
			EnableIpv4Sender (bool): Enable IPv4 Sender
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EnableRandomAsPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables generation/advertisement of Random AS Path Segments.
			EnableWeight (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Weight
			FlapFromRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap From Route Index
			FlapToRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap To Route Index
			IncludeRdInNextHopLength (obj(ixnetwork_restpy.multivalue.Multivalue)): If RD is included in NH Len then NH Len is NH size + RD size else NH len is NH size.
			IncludeSourceAsExtComm (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Source AS ExtComm
			IncludeVrfRouteImportExtComm (obj(ixnetwork_restpy.multivalue.Multivalue)): Include VRF Route Import ExtComm
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label End
			LabelMode (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Mode
			LabelSpaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Space ID
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MaxASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Numbers generated per Segment
			MaxNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Path Segments Per Route Range.
			MinASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Numbers generated per Segments.
			MinNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Path Segments Per Route Range.
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NextHopIPType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			NextHopIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Next Hop Increment Mode
			NextHopType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			PackingFrom (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing From
			PackingTo (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing To
			PartialFlap (obj(ixnetwork_restpy.multivalue.Multivalue)): Partial Flap
			Uptime (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime In Seconds
			UseAsIpv4UmhRoutes (bool): Use As IPv4 UMH Routes
			UseAsUmhRoutes (obj(ixnetwork_restpy.multivalue.Multivalue)): Use As UMH Routes
			UseTraditionalNlri (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Traditional NLRI
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty.BgpL3VpnRouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty import BgpL3VpnRouteProperty
		return self._select(BgpL3VpnRouteProperty(self), locals())

	def add_BgpL3VpnRouteProperty(self, EnableIpv4Receiver="False", EnableIpv4Sender="True", Name=None, NoOfASPathSegmentsPerRouteRange="1", NoOfClusters="1", NoOfCommunities="1", NoOfExternalCommunities="1", UseAsIpv4UmhRoutes="False"):
		"""Adds a child instance of BgpL3VpnRouteProperty on the server.

		Args:
			EnableIpv4Receiver (bool): Enable IPv4 Receiver
			EnableIpv4Sender (bool): Enable IPv4 Sender
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			UseAsIpv4UmhRoutes (bool): Use As IPv4 UMH Routes

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty.BgpL3VpnRouteProperty)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty import BgpL3VpnRouteProperty
		return self._create(BgpL3VpnRouteProperty(self), locals())

	def BgpMVpnReceiverSitesIpv4(self, BFRId=None, BFRIpv4Prefix=None, BFRIpv6Prefix=None, BFRPrefixType=None, SubDomainId=None, UseAutoSubDomainId=None, Active=None, CMulticastRouteType=None, Count=None, DescriptiveName=None, DownstreamLabel=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeBierPtainLeafAd=None, Name=None, SendTriggeredMulticastRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddressIpv4=None, StartSourceAddressIpv4=None, StartSourceOrCrpAddressIpv4=None, SupportLeafADRoutesSending=None, WildCardLeafAdForBierPta=None):
		"""Gets child instances of BgpMVpnReceiverSitesIpv4 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpMVpnReceiverSitesIpv4 will be returned.

		Args:
			BFRId (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR-Id
			BFRIpv4Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR IPv4 Prefix
			BFRIpv6Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR IPv6 Prefix
			BFRPrefixType (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Prefix Type
			SubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Sub-Domain Id
			UseAutoSubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Auto Sub-Domain Id
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			CMulticastRouteType (obj(ixnetwork_restpy.multivalue.Multivalue)): C-Multicast Route Type
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DownstreamLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Downstream Assigned Label in Leaf A-D route when tunnel type is Ingress Replication
			GroupAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Address Count
			GroupMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Mask Width
			IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SendTriggeredMulticastRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Triggered Multicast Route
			SourceAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Address Count
			SourceGroupMapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Group Mapping
			SourceMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Mask Width
			StartGroupAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Group Address
			StartSourceAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Source Address IPv4
			StartSourceOrCrpAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): C-RP Address IPv4
			SupportLeafADRoutesSending (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Leaf A-D Routes Sending
			WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4.BgpMVpnReceiverSitesIpv4))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4 import BgpMVpnReceiverSitesIpv4
		return self._select(BgpMVpnReceiverSitesIpv4(self), locals())

	def add_BgpMVpnReceiverSitesIpv4(self, IncludeBierPtainLeafAd="True", Name=None, WildCardLeafAdForBierPta="False"):
		"""Adds a child instance of BgpMVpnReceiverSitesIpv4 on the server.

		Args:
			IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4.BgpMVpnReceiverSitesIpv4)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4 import BgpMVpnReceiverSitesIpv4
		return self._create(BgpMVpnReceiverSitesIpv4(self), locals())

	def BgpMVpnReceiverSitesIpv6(self, BFRId=None, BFRIpv4Prefix=None, BFRIpv6Prefix=None, BFRPrefixType=None, SubDomainId=None, UseAutoSubDomainId=None, Active=None, CMulticastRouteType=None, Count=None, DescriptiveName=None, DownstreamLabel=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeBierPtainLeafAd=None, Name=None, SendTriggeredMulticastRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddressIpv6=None, StartSourceAddressIpv6=None, StartSourceOrCrpAddressIpv6=None, SupportLeafADRoutesSending=None, WildCardLeafAdForBierPta=None):
		"""Gets child instances of BgpMVpnReceiverSitesIpv6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpMVpnReceiverSitesIpv6 will be returned.

		Args:
			BFRId (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR-Id
			BFRIpv4Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR IPv4 Prefix
			BFRIpv6Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR IPv6 Prefix
			BFRPrefixType (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Prefix Type
			SubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Sub-Domain Id
			UseAutoSubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Auto Sub-Domain Id
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			CMulticastRouteType (obj(ixnetwork_restpy.multivalue.Multivalue)): C-Multicast Route Type
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DownstreamLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Downstream Assigned Label in Leaf A-D route when tunnel type is Ingress Replication
			GroupAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Address Count
			GroupMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Mask Width
			IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SendTriggeredMulticastRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Triggered Multicast Route
			SourceAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Address Count
			SourceGroupMapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Group Mapping
			SourceMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Mask Width
			StartGroupAddressIpv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Group Address
			StartSourceAddressIpv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Source Address IPv6
			StartSourceOrCrpAddressIpv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): C-RP Address IPv6
			SupportLeafADRoutesSending (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Leaf A-D Routes Sending
			WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6.BgpMVpnReceiverSitesIpv6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6 import BgpMVpnReceiverSitesIpv6
		return self._select(BgpMVpnReceiverSitesIpv6(self), locals())

	def add_BgpMVpnReceiverSitesIpv6(self, IncludeBierPtainLeafAd="True", Name=None, WildCardLeafAdForBierPta="False"):
		"""Adds a child instance of BgpMVpnReceiverSitesIpv6 on the server.

		Args:
			IncludeBierPtainLeafAd (bool): Include Bier PTA in Leaf A-D
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			WildCardLeafAdForBierPta (bool): Wildcard Leaf A-D For Bier PTA

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6.BgpMVpnReceiverSitesIpv6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6 import BgpMVpnReceiverSitesIpv6
		return self._create(BgpMVpnReceiverSitesIpv6(self), locals())

	def BgpMVpnSenderSitesIpv4(self, Active=None, Count=None, DescriptiveName=None, GroupAddressCount=None, GroupMaskWidth=None, Name=None, SendTriggeredSourceActiveADRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddressIpv4=None, StartSourceAddressIpv4=None):
		"""Gets child instances of BgpMVpnSenderSitesIpv4 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpMVpnSenderSitesIpv4 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			GroupAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Address Count
			GroupMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Mask Width
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SendTriggeredSourceActiveADRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Triggered Source Active A-D Route
			SourceAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Address Count
			SourceGroupMapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Group Mapping
			SourceMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Mask Width
			StartGroupAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Group Address
			StartSourceAddressIpv4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Source Address IPv4

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4.BgpMVpnSenderSitesIpv4))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4 import BgpMVpnSenderSitesIpv4
		return self._select(BgpMVpnSenderSitesIpv4(self), locals())

	def add_BgpMVpnSenderSitesIpv4(self, Name=None):
		"""Adds a child instance of BgpMVpnSenderSitesIpv4 on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4.BgpMVpnSenderSitesIpv4)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4 import BgpMVpnSenderSitesIpv4
		return self._create(BgpMVpnSenderSitesIpv4(self), locals())

	def BgpMVpnSenderSitesIpv6(self, Active=None, Count=None, DescriptiveName=None, GroupAddressCount=None, GroupMaskWidth=None, IncludeIpv6ExplicitNullLabel=None, Name=None, SendTriggeredSourceActiveADRoute=None, SourceAddressCount=None, SourceGroupMapping=None, SourceMaskWidth=None, StartGroupAddressIpv6=None, StartSourceAddressIpv6=None):
		"""Gets child instances of BgpMVpnSenderSitesIpv6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpMVpnSenderSitesIpv6 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			GroupAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Address Count
			GroupMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Group Mask Width
			IncludeIpv6ExplicitNullLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Include IPv6 Explicit NULL Label
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SendTriggeredSourceActiveADRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Triggered Source Active A-D Route
			SourceAddressCount (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Address Count
			SourceGroupMapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Group Mapping
			SourceMaskWidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Source Mask Width
			StartGroupAddressIpv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Group Address
			StartSourceAddressIpv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Source Address IPv6

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6.BgpMVpnSenderSitesIpv6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6 import BgpMVpnSenderSitesIpv6
		return self._select(BgpMVpnSenderSitesIpv6(self), locals())

	def add_BgpMVpnSenderSitesIpv6(self, Name=None):
		"""Adds a child instance of BgpMVpnSenderSitesIpv6 on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6.BgpMVpnSenderSitesIpv6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6 import BgpMVpnSenderSitesIpv6
		return self._create(BgpMVpnSenderSitesIpv6(self), locals())

	def BgpV6IPRouteProperty(self, OverridePeerAsSetMode=None, Active=None, AddPathId=None, AdvertiseAsBGPLSPrefix=None, AdvertiseAsBgp3107=None, AdvertiseAsBgp3107Sr=None, AdvertiseAsRfc8277=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Count=None, Delay=None, DescriptiveName=None, Downtime=None, EnableAddPath=None, EnableAggregatorId=None, EnableAigp=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSRGB=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncrementMode=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, Name=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLabels=None, NoOfTlvs=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, RouteOrigin=None, SegmentId=None, SendMulticastWithProperSAFI=None, SkipMulticast=None, SpecialLabel=None, Uptime=None, UseTraditionalNlri=None, Weight=None):
		"""Gets child instances of BgpV6IPRouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpV6IPRouteProperty will be returned.

		Args:
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AddPathId (obj(ixnetwork_restpy.multivalue.Multivalue)): BGP ADD Path Id
			AdvertiseAsBGPLSPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise as BGP-LS Prefix
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			AdvertiseNexthopAsV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise Nexthop as V4
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AggregatorIdMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID Mode
			AsNumSuffixRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
			AsPathPerRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
			AsRandomSeed (obj(ixnetwork_restpy.multivalue.Multivalue)): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
			AsSegDist (obj(ixnetwork_restpy.multivalue.Multivalue)): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Delay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Downtime (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime In Seconds
			EnableAddPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Path ID when ADD Path Capability is enabled in BGP Peer
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAigp (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AIGP
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Non-Random AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableFlapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Flapping
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EnableRandomAsPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables generation/advertisement of Random AS Path Segments.
			EnableSRGB (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable SRGB TLV
			EnableWeight (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Weight
			FlapFromRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap From Route Index
			FlapToRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap To Route Index
			IncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Either Fixed or Increment
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label End
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MaxASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Numbers generated per Segment
			MaxNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Path Segments Per Route Range.
			MinASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Numbers generated per Segments.
			MinNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Path Segments Per Route Range.
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NextHopIPType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			NextHopIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Next Hop Increment Mode
			NextHopType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfTlvs (number): Number of TLVs
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			PackingFrom (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing From
			PackingTo (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing To
			PartialFlap (obj(ixnetwork_restpy.multivalue.Multivalue)): Partial Flap
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			SegmentId (obj(ixnetwork_restpy.multivalue.Multivalue)): SID or Segment ID, converts to label value by adding offset into SRGB Start Label Value.
			SendMulticastWithProperSAFI (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Routes with SAFI as Multicast (2)
			SkipMulticast (obj(ixnetwork_restpy.multivalue.Multivalue)): Skip the Multicast routes for this route range
			SpecialLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): If we are emulating Egress then Label field may not hold Label value calculated based on SRGB and Offset but Implicit IPv4 NULL or Explicit NULL
			Uptime (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime In Seconds
			UseTraditionalNlri (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Traditional NLRI
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty.BgpV6IPRouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty import BgpV6IPRouteProperty
		return self._select(BgpV6IPRouteProperty(self), locals())

	def add_BgpV6IPRouteProperty(self, AdvertiseAsBgp3107="False", AdvertiseAsBgp3107Sr="False", AdvertiseAsRfc8277="False", Name=None, NoOfASPathSegmentsPerRouteRange="1", NoOfClusters="1", NoOfCommunities="1", NoOfExternalCommunities="1", NoOfLabels="1", NoOfTlvs="1"):
		"""Adds a child instance of BgpV6IPRouteProperty on the server.

		Args:
			AdvertiseAsBgp3107 (bool): Will cause this route to be sent as BGP 3107 MPLS SAFI route
			AdvertiseAsBgp3107Sr (bool): Will cause this route to be sent as BGP 3107 SR MPLS SAFI route
			AdvertiseAsRfc8277 (bool): Will cause this route to be sent as RFC 8277 MPLS SAFI route
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLabels (number): Number of Labels
			NoOfTlvs (number): Number of TLVs

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty.BgpV6IPRouteProperty)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty import BgpV6IPRouteProperty
		return self._create(BgpV6IPRouteProperty(self), locals())

	def BgpV6L3VpnRouteProperty(self, OverridePeerAsSetMode=None, Active=None, AdvSrv6SidInIgp=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Count=None, Delay=None, DescriptiveName=None, DistinguisherAsNumber=None, DistinguisherAssignedNumber=None, DistinguisherIpAddress=None, DistinguisherType=None, Downtime=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableIpv6Receiver=None, EnableIpv6Sender=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSrv6Sid=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncludeRdInNextHopLength=None, IncludeSourceAsExtComm=None, IncludeVrfRouteImportExtComm=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelMode=None, LabelSpaceId=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, Name=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, Srv6SidFuncAllocType=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, Srv6SidStep=None, Uptime=None, UseAsIpv6UmhRoutes=None, UseAsUmhRoutes=None, UseTraditionalNlri=None, Weight=None):
		"""Gets child instances of BgpV6L3VpnRouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpV6L3VpnRouteProperty will be returned.

		Args:
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvSrv6SidInIgp (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise SRv6 SID in IGP (ISIS)
			AdvertiseNexthopAsV4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise Nexthop as V4
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AggregatorIdMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID Mode
			AsNumSuffixRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)
			AsPathPerRoute (obj(ixnetwork_restpy.multivalue.Multivalue)): When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.
			AsRandomSeed (obj(ixnetwork_restpy.multivalue.Multivalue)): Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.
			AsSegDist (obj(ixnetwork_restpy.multivalue.Multivalue)): Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Delay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistinguisherAsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher AS Number (2-byte or 4-Byte)
			DistinguisherAssignedNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher Assigned Number
			DistinguisherIpAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher IP Address
			DistinguisherType (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Distinguisher Type
			Downtime (obj(ixnetwork_restpy.multivalue.Multivalue)): Downtime In Seconds
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Non-Random AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableFlapping (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Flapping
			EnableIpv6Receiver (bool): Enable IPv6 Receiver
			EnableIpv6Sender (bool): Enable IPv6 Sender
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EnableRandomAsPath (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables generation/advertisement of Random AS Path Segments.
			EnableSrv6Sid (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable SRv6 SID With VPN Route
			EnableWeight (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Weight
			FlapFromRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap From Route Index
			FlapToRouteIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): Flap To Route Index
			IncludeRdInNextHopLength (obj(ixnetwork_restpy.multivalue.Multivalue)): If RD is included in NH Len then NH Len is NH size + RD size else NH len is NH size.
			IncludeSourceAsExtComm (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Source AS ExtComm
			IncludeVrfRouteImportExtComm (obj(ixnetwork_restpy.multivalue.Multivalue)): Include VRF Route Import ExtComm
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelEnd (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label End
			LabelMode (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Mode
			LabelSpaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Space ID
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): L3VPN RR Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MaxASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Numbers generated per Segment
			MaxNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Number Of AS Path Segments Per Route Range.
			MinASNumPerSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Numbers generated per Segments.
			MinNoOfASPathSegmentsPerRouteRange (obj(ixnetwork_restpy.multivalue.Multivalue)): Minimum Number Of AS Path Segments Per Route Range.
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NextHopIPType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			NextHopIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Next Hop Increment Mode
			NextHopType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			PackingFrom (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing From
			PackingTo (obj(ixnetwork_restpy.multivalue.Multivalue)): Packing To
			PartialFlap (obj(ixnetwork_restpy.multivalue.Multivalue)): Partial Flap
			Srv6SidFuncAllocType (obj(ixnetwork_restpy.multivalue.Multivalue)): SRv6 Func Allocation Type
			Srv6SidLoc (obj(ixnetwork_restpy.multivalue.Multivalue)): SRv6 SID. It consists of Locator, Func and Args
			Srv6SidLocLen (obj(ixnetwork_restpy.multivalue.Multivalue)): SRv6 SID Locator Length
			Srv6SidLocMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): SRv6 SID Locator Metric
			Srv6SidReserved (obj(ixnetwork_restpy.multivalue.Multivalue)): SRv6 SID Reserved Value
			Srv6SidStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Range SRv6 SID Step
			Uptime (obj(ixnetwork_restpy.multivalue.Multivalue)): Uptime In Seconds
			UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes
			UseAsUmhRoutes (obj(ixnetwork_restpy.multivalue.Multivalue)): Use As UMH Routes
			UseTraditionalNlri (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Traditional NLRI
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty.BgpV6L3VpnRouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty import BgpV6L3VpnRouteProperty
		return self._select(BgpV6L3VpnRouteProperty(self), locals())

	def add_BgpV6L3VpnRouteProperty(self, EnableIpv6Receiver="False", EnableIpv6Sender="True", Name=None, NoOfASPathSegmentsPerRouteRange="1", NoOfClusters="1", NoOfCommunities="1", NoOfExternalCommunities="1", UseAsIpv6UmhRoutes="False"):
		"""Adds a child instance of BgpV6L3VpnRouteProperty on the server.

		Args:
			EnableIpv6Receiver (bool): Enable IPv6 Receiver
			EnableIpv6Sender (bool): Enable IPv6 Sender
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty.BgpV6L3VpnRouteProperty)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty import BgpV6L3VpnRouteProperty
		return self._create(BgpV6L3VpnRouteProperty(self), locals())

	def CMacProperties(self, Active=None, ActiveTs=None, AdvertiseIpv4Address=None, AdvertiseIpv6Address=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableSecondLabel=None, EnableStickyStaticFlag=None, EnableUserDefinedSequenceNumber=None, EviId=None, FirstLabelStart=None, IncludeDefaultGatewayExtendedCommunity=None, Ipv4AddressPrefixLength=None, Ipv4NextHop=None, Ipv6AddressPrefixLength=None, Ipv6NextHop=None, LabelMode=None, LabelStep=None, LocalPreference=None, MultiExitDiscriminator=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PeerAddress=None, SecondLabelStart=None, SequenceNumber=None, SetNextHop=None, SetNextHopIpType=None, UseSameSequenceNumber=None):
		"""Gets child instances of CMacProperties from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of CMacProperties will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ActiveTs (obj(ixnetwork_restpy.multivalue.Multivalue)): Active TS
			AdvertiseIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise IPv4 Address
			AdvertiseIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise IPv6 Address
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			EnableSecondLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Second Label (L3)
			EnableStickyStaticFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Sticky/Static Flag
			EnableUserDefinedSequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable User Defined Sequence Number
			EviId (obj(ixnetwork_restpy.multivalue.Multivalue)): EVI ID
			FirstLabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): First Label (L2) Start
			IncludeDefaultGatewayExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Default Gateway Extended Community
			Ipv4AddressPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Address Prefix Length which is used to determine the intersubnetting between local and remote host
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6AddressPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Address Prefix Length which is used to determine the intersubnetting between local and remote host
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Mode
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			PeerAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Peer IP Address
			SecondLabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Second Label (L3) Start
			SequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Sequence Number
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type
			UseSameSequenceNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Use Same Sequence Number

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties.CMacProperties))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties import CMacProperties
		return self._select(CMacProperties(self), locals())

	def add_CMacProperties(self, Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1"):
		"""Adds a child instance of CMacProperties on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties.CMacProperties)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties import CMacProperties
		return self._create(CMacProperties(self), locals())

	def DeviceGroup(self, Count=None, DescriptiveName=None, Enabled=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of DeviceGroup from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DeviceGroup will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enabled (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables/disables device.
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup.DeviceGroup))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup import DeviceGroup
		return self._select(DeviceGroup(self), locals())

	def add_DeviceGroup(self, Multiplier="10", Name=None):
		"""Adds a child instance of DeviceGroup on the server.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup.DeviceGroup)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup import DeviceGroup
		return self._create(DeviceGroup(self), locals())

	def DslPools(self, ActualNetDataRateDownstream=None, ActualNetDataRateDownstreamTolerance=None, ActualNetDataRateUpstream=None, ActualNetDataRateUpstreamTolerance=None, CircuitId=None, Count=None, DescriptiveName=None, DslType=None, EnableActualNetDataRateDownstream=None, EnableActualNetDataRateUpstream=None, EnableDslType=None, EnablePonType=None, EnableRemoteId=None, FlappingMode=None, InnerVlanId=None, LineDownInterval=None, LineUpInterval=None, Name=None, OuterVlanId=None, PonType=None, RemoteId=None, TechType=None, VlanAllocationModel=None):
		"""Gets child instances of DslPools from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DslPools will be returned.

		Args:
			ActualNetDataRateDownstream (obj(ixnetwork_restpy.multivalue.Multivalue)): Actual downstream net data rate on a DSL access line. Rate in kbits/s as a 32-bit unsigned integer
			ActualNetDataRateDownstreamTolerance (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage for variation of Actual Net Data Rate Downstream TLV value when sending port-up messages in flapping behavior
			ActualNetDataRateUpstream (obj(ixnetwork_restpy.multivalue.Multivalue)): Actual upstream net data rate on a DSL access line. Rate in kbits/s as a 32-bit unsigned integer
			ActualNetDataRateUpstreamTolerance (obj(ixnetwork_restpy.multivalue.Multivalue)): Percentage for variation of Actual Net Data Rate Upstream TLV value when sending port-up messages in flapping behavior
			CircuitId (obj(ixnetwork_restpy.multivalue.Multivalue)): A locally administered human-readable string generated by or configured on the Access Node, identifying the corresponding access loop logical port on the user side of the Access Node
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DslType (obj(ixnetwork_restpy.multivalue.Multivalue)): DSL Type value for DSL Type TLV
			EnableActualNetDataRateDownstream (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Actual-Net-Data-Rate-Downstream TLV
			EnableActualNetDataRateUpstream (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Actual-Net-Data-Rate-Upstream TLV
			EnableDslType (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable DSL Type TLV
			EnablePonType (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable PON Type TLV
			EnableRemoteId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Access-Loop-Remote-ID TLV
			FlappingMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable a flapping profile. Resync will send Port-Up messages, one message every 'Flap Interval' seconds. Reset will send Port-Up followed by Port-Down messages, one message every 'Flap Interval' seconds. Stop will stop the flapping profile, and send one Port-Up message if the line is silent at the time of stopping the flapping profile.
			InnerVlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): Inner VLAN ID for N:1 and 1:1 VLAN mapping in Access-Aggregation-Circuit-ID-Binary TLV
			LineDownInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Interval in milliseconds to wait after sending port-down message when flapping is enabled
			LineUpInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Interval in milliseconds to wait after sending port-up message when flapping is enabled
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OuterVlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): Outer VLAN ID for 1:1 VLAN mapping in Access-Aggregation-Circuit-ID-Binary TLV
			PonType (obj(ixnetwork_restpy.multivalue.Multivalue)): PON Type value for PON Type TLV
			RemoteId (obj(ixnetwork_restpy.multivalue.Multivalue)): An operator-configured string that uniquely identifies the user on the associated access line
			TechType (obj(ixnetwork_restpy.multivalue.Multivalue)): Type of Access Loop Technology
			VlanAllocationModel (obj(ixnetwork_restpy.multivalue.Multivalue)): Access-Aggregation-Circuit-ID-Binary TLV disable, enable N:1 vlan allocation model or 1:1 vlan allocation model

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools.DslPools))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools import DslPools
		return self._select(DslPools(self), locals())

	def add_DslPools(self, Name=None):
		"""Adds a child instance of DslPools on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools.DslPools)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dslpools import DslPools
		return self._create(DslPools(self), locals())

	def EvpnIPv4PrefixRange(self, Active=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelMode=None, LabelStart=None, LabelStep=None, LocalPreference=None, MultiExitDiscriminator=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, SetNextHop=None, SetNextHopIpType=None):
		"""Gets child instances of EvpnIPv4PrefixRange from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EvpnIPv4PrefixRange will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Mode
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange.EvpnIPv4PrefixRange))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange import EvpnIPv4PrefixRange
		return self._select(EvpnIPv4PrefixRange(self), locals())

	def add_EvpnIPv4PrefixRange(self, Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1"):
		"""Adds a child instance of EvpnIPv4PrefixRange on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange.EvpnIPv4PrefixRange)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange import EvpnIPv4PrefixRange
		return self._create(EvpnIPv4PrefixRange(self), locals())

	def EvpnIPv6PrefixRange(self, Active=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, Count=None, DescriptiveName=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelMode=None, LabelStart=None, LabelStep=None, LocalPreference=None, MultiExitDiscriminator=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, SetNextHop=None, SetNextHopIpType=None):
		"""Gets child instances of EvpnIPv6PrefixRange from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EvpnIPv6PrefixRange will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AggregatorAs (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator AS
			AggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregator ID
			AsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): AS# Set Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAggregatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Aggregator ID
			EnableAsPathSegments (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segments
			EnableAtomicAggregate (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Atomic Aggregate
			EnableCluster (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Cluster
			EnableCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Community
			EnableExtendedCommunity (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Extended Community
			EnableLocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Local Preference
			EnableMultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Multi Exit
			EnableNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Next Hop
			EnableOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Origin
			EnableOriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Originator ID
			Ipv4NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Next Hop
			Ipv6NextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Next Hop
			LabelMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Mode
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Start
			LabelStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Step
			LocalPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Preference
			MultiExitDiscriminator (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi Exit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities
			Origin (obj(ixnetwork_restpy.multivalue.Multivalue)): Origin
			OriginatorId (obj(ixnetwork_restpy.multivalue.Multivalue)): Originator ID
			OverridePeerAsSetMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Override Peer AS# Set Mode
			SetNextHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop
			SetNextHopIpType (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Next Hop IP Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange.EvpnIPv6PrefixRange))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange import EvpnIPv6PrefixRange
		return self._select(EvpnIPv6PrefixRange(self), locals())

	def add_EvpnIPv6PrefixRange(self, Name=None, NoOfASPathSegmentsPerRouteRange="0", NoOfClusters="1", NoOfCommunities="1", NoOfExtendedCommunity="1"):
		"""Adds a child instance of EvpnIPv6PrefixRange on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExtendedCommunity (number): Number of Extended Communities

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange.EvpnIPv6PrefixRange)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange import EvpnIPv6PrefixRange
		return self._create(EvpnIPv6PrefixRange(self), locals())

	def Ipv4PrefixPools(self, AddrStepSupported=None, Count=None, DescriptiveName=None, Name=None, NetworkAddress=None, NumberOfAddresses=None, PrefixAddrStep=None, PrefixLength=None):
		"""Gets child instances of Ipv4PrefixPools from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv4PrefixPools will be returned.

		Args:
			AddrStepSupported (bool): Indicates whether the Route Range provider allows route range address increment step of more than one
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): First address of host/network address pool in the simulated IPv4 host/network range
			NumberOfAddresses (number): Number of host/network addresses in the simulated IPv4 host/network range
			PrefixAddrStep (obj(ixnetwork_restpy.multivalue.Multivalue)): The difference between each address, and its next, in the IPv4 host/network range.
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools.Ipv4PrefixPools))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools import Ipv4PrefixPools
		return self._select(Ipv4PrefixPools(self), locals())

	def add_Ipv4PrefixPools(self, AddrStepSupported="False", Name=None, NumberOfAddresses="1"):
		"""Adds a child instance of Ipv4PrefixPools on the server.

		Args:
			AddrStepSupported (bool): Indicates whether the Route Range provider allows route range address increment step of more than one
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAddresses (number): Number of host/network addresses in the simulated IPv4 host/network range

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools.Ipv4PrefixPools)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools import Ipv4PrefixPools
		return self._create(Ipv4PrefixPools(self), locals())

	def Ipv6PrefixPools(self, AddrStepSupported=None, Count=None, DescriptiveName=None, Name=None, NetworkAddress=None, NumberOfAddresses=None, PrefixAddrStep=None, PrefixLength=None):
		"""Gets child instances of Ipv6PrefixPools from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv6PrefixPools will be returned.

		Args:
			AddrStepSupported (bool): Indicates whether the Route Range provider allows address increment step of more than one
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): First address of host/network address pool in the simulated IPv6 host/network range
			NumberOfAddresses (number): Number of host/network addresses in the simulated IPv6 host/network range
			PrefixAddrStep (obj(ixnetwork_restpy.multivalue.Multivalue)): The difference between each address, and its next, in the IPv6 host/network range.
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools.Ipv6PrefixPools))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools import Ipv6PrefixPools
		return self._select(Ipv6PrefixPools(self), locals())

	def add_Ipv6PrefixPools(self, AddrStepSupported="False", Name=None, NumberOfAddresses="1"):
		"""Adds a child instance of Ipv6PrefixPools on the server.

		Args:
			AddrStepSupported (bool): Indicates whether the Route Range provider allows address increment step of more than one
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAddresses (number): Number of host/network addresses in the simulated IPv6 host/network range

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools.Ipv6PrefixPools)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools import Ipv6PrefixPools
		return self._create(Ipv6PrefixPools(self), locals())

	def IsisL3RouteProperty(self, BAR=None, BFRId=None, BFRIdStep=None, BIERBitStringLength=None, IPA=None, Active=None, AdvIPv6Prefix=None, Algorithm=None, ConfigureSIDIndexLabel=None, Count=None, DBitInsideSRv6SidTLV=None, DescriptiveName=None, EFlag=None, Funcflags=None, Function=None, IncludeBSLObject=None, Ipv6SID=None, Ipv6Srh=None, LFlag=None, LabelRangeSize=None, LabelStart=None, Metric=None, NFlag=None, Name=None, PFlag=None, RFlag=None, Redistribution=None, ReservedInsideFlagsOfSRv6SidTLV=None, RouteOrigin=None, SIDIndexLabel=None, SubDomainId=None, VFlag=None):
		"""Gets child instances of IsisL3RouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3RouteProperty will be returned.

		Args:
			BAR (obj(ixnetwork_restpy.multivalue.Multivalue)): BIER Algorithm
			BFRId (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Id
			BFRIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Id Step
			BIERBitStringLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Bit String Length
			IPA (obj(ixnetwork_restpy.multivalue.Multivalue)): IGP Algorithm
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvIPv6Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise IPv6 Prefix
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DBitInsideSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit NULL flag
			Funcflags (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the function flags
			Function (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies endpoint function codes
			IncludeBSLObject (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, MPLS encapsulation sub-sub-Tlv will be advertised under Bier Info Sub-Tlv
			Ipv6SID (obj(ixnetwork_restpy.multivalue.Multivalue)): This refers to the IPv6 SID that is being used to reach the advertised IPv6 Prefix
			Ipv6Srh (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise IPv6 SID
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Flag
			LabelRangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Set Identifier
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Start
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Metric
			NFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Nodal prefix flag
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
			RFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution flag
			Redistribution (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution
			ReservedInsideFlagsOfSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the reserved field (part of Flags field of SRv6 SID TLV)
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			SIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Sub Domain Id
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty.IsisL3RouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty import IsisL3RouteProperty
		return self._select(IsisL3RouteProperty(self), locals())

	def IsisSpbMacCloudConfig(self, Active=None, Count=None, DescriptiveName=None, Isid=None, Name=None):
		"""Gets child instances of IsisSpbMacCloudConfig from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbMacCloudConfig will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Isid (obj(ixnetwork_restpy.multivalue.Multivalue)): ISID
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig.IsisSpbMacCloudConfig))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig import IsisSpbMacCloudConfig
		return self._select(IsisSpbMacCloudConfig(self), locals())

	def add_IsisSpbMacCloudConfig(self, Name=None):
		"""Adds a child instance of IsisSpbMacCloudConfig on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig.IsisSpbMacCloudConfig)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig import IsisSpbMacCloudConfig
		return self._create(IsisSpbMacCloudConfig(self), locals())

	def IsisTrillUCastMacConfig(self, Active=None, Count=None, DescriptiveName=None, Name=None):
		"""Gets child instances of IsisTrillUCastMacConfig from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrillUCastMacConfig will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig.IsisTrillUCastMacConfig))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig import IsisTrillUCastMacConfig
		return self._select(IsisTrillUCastMacConfig(self), locals())

	def LdpFECProperty(self, Active=None, Count=None, DescriptiveName=None, EnablePacking=None, EnableReplyingLspPing=None, LabelIncrementMode=None, LabelValue=None, Name=None):
		"""Gets child instances of LdpFECProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpFECProperty will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnablePacking (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC ranges are aggregated within a single LDP PDU to conserve bandwidth and processing.
			EnableReplyingLspPing (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping reply is enabled.
			LabelIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Increment Mode
			LabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): The first label in the range of labels
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty.LdpFECProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty import LdpFECProperty
		return self._select(LdpFECProperty(self), locals())

	def LdpIpv6FECProperty(self, Active=None, Count=None, DescriptiveName=None, EnablePacking=None, EnableReplyingLspPing=None, LabelIncrementMode=None, LabelValue=None, Name=None):
		"""Gets child instances of LdpIpv6FECProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpIpv6FECProperty will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnablePacking (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC ranges are aggregated within a single LDP PDU to conserve bandwidth and processing.
			EnableReplyingLspPing (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping reply is enabled.
			LabelIncrementMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Increment Mode
			LabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): The first label in the range of labels
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty.LdpIpv6FECProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty import LdpIpv6FECProperty
		return self._select(LdpIpv6FECProperty(self), locals())

	def MacPools(self, Count=None, DescriptiveName=None, EnableVlans=None, Mac=None, Name=None, NumberOfAddresses=None, PrefixLength=None, UseVlans=None, VlanCount=None):
		"""Gets child instances of MacPools from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MacPools will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableVlans (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables VLANs for the sessions
			Mac (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC addresses of the devices
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAddresses (number): Number of MAC addresses in the simulated MAC range
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools.MacPools))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools import MacPools
		return self._select(MacPools(self), locals())

	def add_MacPools(self, Name=None, NumberOfAddresses="1", UseVlans="False", VlanCount="1"):
		"""Adds a child instance of MacPools on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAddresses (number): Number of MAC addresses in the simulated MAC range
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools.MacPools)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.macpools import MacPools
		return self._create(MacPools(self), locals())

	def NetworkGroup(self, Count=None, DescriptiveName=None, Enabled=None, Multiplier=None, Name=None):
		"""Gets child instances of NetworkGroup from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetworkGroup will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enabled (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables/disables device.
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup.NetworkGroup))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup import NetworkGroup
		return self._select(NetworkGroup(self), locals())

	def add_NetworkGroup(self, Multiplier="1", Name=None):
		"""Adds a child instance of NetworkGroup on the server.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup.NetworkGroup)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup import NetworkGroup
		return self._create(NetworkGroup(self), locals())

	def NetworkRangeInfo(self, Count=None, DescriptiveName=None, Name=None, NetworkRangeIPByMask=None, NetworkRangeInterfaceIp=None, NetworkRangeInterfaceIpMask=None, NetworkRangeIp=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRID=None, NetworkRangeRIDIncrement=None, NumColumns=None, NumRows=None):
		"""Gets child instances of NetworkRangeInfo from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetworkRangeInfo will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkRangeIPByMask (obj(ixnetwork_restpy.multivalue.Multivalue)): Use mask to generate range of addresses
			NetworkRangeInterfaceIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface IP address for a non-connected interface
			NetworkRangeInterfaceIpMask (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface IP mask for a non-connected interface
			NetworkRangeIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Range IP
			NetworkRangeIpIncrementBy (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Range IP Increment By
			NetworkRangeIpMask (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Range IP Mask
			NetworkRangeLinkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Type
			NetworkRangeRID (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Range RID
			NetworkRangeRIDIncrement (obj(ixnetwork_restpy.multivalue.Multivalue)): Network Range RID Increment
			NumColumns (obj(ixnetwork_restpy.multivalue.Multivalue)): 4 Byte Integer.
			NumRows (obj(ixnetwork_restpy.multivalue.Multivalue)): 4 Byte Integer.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo.NetworkRangeInfo))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo import NetworkRangeInfo
		return self._select(NetworkRangeInfo(self), locals())

	def add_NetworkRangeInfo(self, Name=None):
		"""Adds a child instance of NetworkRangeInfo on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo.NetworkRangeInfo)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo import NetworkRangeInfo
		return self._create(NetworkRangeInfo(self), locals())

	def NetworkTopology(self, Count=None, LinksPerNetwork=None, NodesPerNetwork=None):
		"""Gets child instances of NetworkTopology from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetworkTopology will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			LinksPerNetwork (number): linksPerNetwork is controled by assigned topology
			NodesPerNetwork (number): Number of nodes in the Network Topology, including the root node defined in the parent Device Group

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology.NetworkTopology))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology import NetworkTopology
		return self._select(NetworkTopology(self), locals())

	def add_NetworkTopology(self):
		"""Adds a child instance of NetworkTopology on the server.

		Args:

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology.NetworkTopology)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology import NetworkTopology
		return self._create(NetworkTopology(self), locals())

	def OspfRouteProperty(self, BAR=None, BFRId=None, BFRIdStep=None, BIERBitStringLength=None, Active=None, Algorithm=None, AllowPropagate=None, BierAFlag=None, BierNFlag=None, ConfigureSIDIndexLabel=None, Count=None, DescriptiveName=None, EFlag=None, IncludeBSLObject=None, Ipa=None, LFlag=None, LabelStart=None, MFlag=None, MaxSI=None, Metric=None, MtId=None, Name=None, NpFlag=None, RouteOrigin=None, SidIndexLabel=None, SubDomainId=None, VFlag=None):
		"""Gets child instances of OspfRouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OspfRouteProperty will be returned.

		Args:
			BAR (obj(ixnetwork_restpy.multivalue.Multivalue)): BIER Algorithm
			BFRId (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Id
			BFRIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): BFR Id Step
			BIERBitStringLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Bit String Length
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm
			AllowPropagate (obj(ixnetwork_restpy.multivalue.Multivalue)): Allow Propagate
			BierAFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Attach Flag
			BierNFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Flag
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit-Null Flag
			IncludeBSLObject (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, MPLS encapsulation sub-sub-Tlv will be advertised under Bier Info Sub-Tlv
			Ipa (obj(ixnetwork_restpy.multivalue.Multivalue)): IPA
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local or Global Flag
			LabelStart (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Start
			MFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Mapping Server Flag
			MaxSI (obj(ixnetwork_restpy.multivalue.Multivalue)): Max SI
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Metric
			MtId (obj(ixnetwork_restpy.multivalue.Multivalue)): Multi-Topology ID
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NpFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP Flag
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			SidIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SubDomainId (obj(ixnetwork_restpy.multivalue.Multivalue)): Sub Domain Id
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value or Index Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty.OspfRouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty import OspfRouteProperty
		return self._select(OspfRouteProperty(self), locals())

	def Ospfv3RouteProperty(self, Active=None, AllowPropagate=None, AutoSelectForwardingAddress=None, Count=None, DescriptiveName=None, ForwardingAddress=None, Metric=None, Name=None, RouteOrigin=None):
		"""Gets child instances of Ospfv3RouteProperty from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv3RouteProperty will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AllowPropagate (obj(ixnetwork_restpy.multivalue.Multivalue)): Allow Propagate
			AutoSelectForwardingAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto Select Forwarding Address
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ForwardingAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Forwarding addresses of the Type-7 LSA
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty.Ospfv3RouteProperty))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty import Ospfv3RouteProperty
		return self._select(Ospfv3RouteProperty(self), locals())

	def add_Ospfv3RouteProperty(self, Name=None):
		"""Adds a child instance of Ospfv3RouteProperty on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty.Ospfv3RouteProperty)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty import Ospfv3RouteProperty
		return self._create(Ospfv3RouteProperty(self), locals())

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
	def Enabled(self):
		"""Enables/disables device.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enabled')

	@property
	def Multiplier(self):
		"""Number of device instances per parent device instance (multiplier)

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

	def remove(self):
		"""Deletes a child instance of NetworkGroup on the server.

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

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./networkGroup object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./networkGroup object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
