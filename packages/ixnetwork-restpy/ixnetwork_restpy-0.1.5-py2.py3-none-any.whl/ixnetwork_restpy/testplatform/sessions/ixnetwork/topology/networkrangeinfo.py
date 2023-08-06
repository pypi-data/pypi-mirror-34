from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NetworkRangeInfo(Base):
	"""RBRangeInfo help : TODO.
	"""

	_SDM_NAME = 'networkRangeInfo'

	def __init__(self, parent):
		super(NetworkRangeInfo, self).__init__(parent)

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
	def NetworkRangeIPByMask(self):
		"""Use mask to generate range of addresses

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeIPByMask')

	@property
	def NetworkRangeInterfaceIp(self):
		"""Interface IP address for a non-connected interface

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeInterfaceIp')

	@property
	def NetworkRangeInterfaceIpMask(self):
		"""Interface IP mask for a non-connected interface

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeInterfaceIpMask')

	@property
	def NetworkRangeIp(self):
		"""Network Range IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeIp')

	@property
	def NetworkRangeIpIncrementBy(self):
		"""Network Range IP Increment By

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeIpIncrementBy')

	@property
	def NetworkRangeIpMask(self):
		"""Network Range IP Mask

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeIpMask')

	@property
	def NetworkRangeLinkType(self):
		"""Link Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeLinkType')

	@property
	def NetworkRangeRID(self):
		"""Network Range RID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeRID')

	@property
	def NetworkRangeRIDIncrement(self):
		"""Network Range RID Increment

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkRangeRIDIncrement')

	@property
	def NumColumns(self):
		"""4 Byte Integer.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numColumns')

	@property
	def NumRows(self):
		"""4 Byte Integer.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numRows')

	def remove(self):
		"""Deletes a child instance of NetworkRangeInfo on the server.

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
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./networkRangeInfo object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./networkRangeInfo object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
