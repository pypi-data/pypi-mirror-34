from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6PrefixPools(Base):
	"""Represents an IPv6 address
	"""

	_SDM_NAME = 'ipv6PrefixPools'

	def __init__(self, parent):
		super(Ipv6PrefixPools, self).__init__(parent)

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
	def AddrStepSupported(self):
		"""Indicates whether the Route Range provider allows address increment step of more than one

		Returns:
			bool
		"""
		return self._get_attribute('addrStepSupported')
	@AddrStepSupported.setter
	def AddrStepSupported(self, value):
		self._set_attribute('addrStepSupported', value)

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
	def LastNetworkAddress(self):
		"""Last Address of host/network address pool in the simulated IPv6 host/network range

		Returns:
			list(str)
		"""
		return self._get_attribute('lastNetworkAddress')

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
	def NetworkAddress(self):
		"""First address of host/network address pool in the simulated IPv6 host/network range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkAddress')

	@property
	def NumberOfAddresses(self):
		"""Number of host/network addresses in the simulated IPv6 host/network range

		Returns:
			number
		"""
		return self._get_attribute('numberOfAddresses')
	@NumberOfAddresses.setter
	def NumberOfAddresses(self, value):
		self._set_attribute('numberOfAddresses', value)

	@property
	def PrefixAddrStep(self):
		"""The difference between each address, and its next, in the IPv6 host/network range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixAddrStep')

	@property
	def PrefixLength(self):
		"""The length (in bits) of the mask to be used in conjunction with all the addresses created in the range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixLength')

	def remove(self):
		"""Deletes a child instance of Ipv6PrefixPools on the server.

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
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6PrefixPools object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ipv6PrefixPools object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
