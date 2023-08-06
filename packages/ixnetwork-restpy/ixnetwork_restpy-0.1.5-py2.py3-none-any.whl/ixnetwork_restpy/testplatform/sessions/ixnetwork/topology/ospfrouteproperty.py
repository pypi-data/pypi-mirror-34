from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OspfRouteProperty(Base):
	"""OSPF route range table
	"""

	_SDM_NAME = 'ospfRouteProperty'

	def __init__(self, parent):
		super(OspfRouteProperty, self).__init__(parent)

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

	@property
	def BAR(self):
		"""BIER Algorithm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('BAR')

	@property
	def BFRId(self):
		"""BFR Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('BFRId')

	@property
	def BFRIdStep(self):
		"""BFR Id Step

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('BFRIdStep')

	@property
	def BIERBitStringLength(self):
		"""Bit String Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('BIERBitStringLength')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Algorithm(self):
		"""Algorithm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('algorithm')

	@property
	def AllowPropagate(self):
		"""Allow Propagate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('allowPropagate')

	@property
	def BierAFlag(self):
		"""Attach Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bierAFlag')

	@property
	def BierNFlag(self):
		"""Node Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bierNFlag')

	@property
	def ConfigureSIDIndexLabel(self):
		"""Configure SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureSIDIndexLabel')

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
	def EFlag(self):
		"""Explicit-Null Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eFlag')

	@property
	def IncludeBSLObject(self):
		"""If set, MPLS encapsulation sub-sub-Tlv will be advertised under Bier Info Sub-Tlv

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeBSLObject')

	@property
	def Ipa(self):
		"""IPA

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipa')

	@property
	def LFlag(self):
		"""Local or Global Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lFlag')

	@property
	def LabelStart(self):
		"""Label Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelStart')

	@property
	def MFlag(self):
		"""Mapping Server Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mFlag')

	@property
	def MaxSI(self):
		"""Max SI

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxSI')

	@property
	def Metric(self):
		"""Route Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('metric')

	@property
	def MtId(self):
		"""Multi-Topology ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mtId')

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
	def NpFlag(self):
		"""No-PHP Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('npFlag')

	@property
	def RouteOrigin(self):
		"""Route Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routeOrigin')

	@property
	def SidIndexLabel(self):
		"""SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sidIndexLabel')

	@property
	def SubDomainId(self):
		"""Sub Domain Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('subDomainId')

	@property
	def VFlag(self):
		"""Value or Index Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vFlag')

	def AgeOutRoutes(self, Arg1, Percentage):
		"""Executes the ageOutRoutes operation on the server.

		Age out percentage of OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			Percentage (number): This parameter requires a percentage of type kInteger

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('ageOutRoutes', payload=locals(), response_object=None)

	def AgeOutRoutes(self, Arg1, Percentage, SessionIndices):
		"""Executes the ageOutRoutes operation on the server.

		Age out percentage of OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			Percentage (number): This parameter requires a percentage of type kInteger
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('ageOutRoutes', payload=locals(), response_object=None)

	def AgeOutRoutes(self, Arg1, SessionIndices, Percentage):
		"""Executes the ageOutRoutes operation on the server.

		Age out percentage of OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (str): This parameter requires a percentage of type kInteger
			Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('ageOutRoutes', payload=locals(), response_object=None)

	def Ageoutroutes(self, Arg2, Arg3):
		"""Executes the ageoutroutes operation on the server.

		Completely/Partially age out routes contained in this route range.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
			Arg3 (number): What percentage of routes to age out. 100% means all routes.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('ageoutroutes', payload=locals(), response_object=None)

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

	def ReadvertiseRoutes(self, Arg1):
		"""Executes the readvertiseRoutes operation on the server.

		Re-advertise Aged out OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('readvertiseRoutes', payload=locals(), response_object=None)

	def ReadvertiseRoutes(self, Arg1, SessionIndices):
		"""Executes the readvertiseRoutes operation on the server.

		Re-advertise Aged out OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('readvertiseRoutes', payload=locals(), response_object=None)

	def ReadvertiseRoutes(self, Arg1, SessionIndices):
		"""Executes the readvertiseRoutes operation on the server.

		Re-advertise Aged out OSPF Routes in a Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('readvertiseRoutes', payload=locals(), response_object=None)

	def Readvertiseroutes(self, Arg2):
		"""Executes the readvertiseroutes operation on the server.

		Readvertise only the aged-out routes contained in this route range.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('readvertiseroutes', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop OSPF Route Range

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfRouteProperty object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
