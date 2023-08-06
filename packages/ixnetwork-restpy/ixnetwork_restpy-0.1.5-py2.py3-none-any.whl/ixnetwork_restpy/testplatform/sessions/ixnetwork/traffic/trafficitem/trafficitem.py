from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TrafficItem(Base):
	"""
	"""

	_SDM_NAME = 'trafficItem'

	def __init__(self, parent):
		super(TrafficItem, self).__init__(parent)

	def AppLibProfile(self, EnablePerIPStats=None, ObjectiveDistribution=None, ObjectiveType=None, ObjectiveValue=None, TrafficState=None):
		"""Gets child instances of AppLibProfile from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AppLibProfile will be returned.

		Args:
			EnablePerIPStats (bool): Enable Per IP Stats. When true then Per IP statistic drilldown is available.
			ObjectiveDistribution (str(applyFullObjectiveToEachPort|splitObjectiveEvenlyAmongPorts)): Objective distribution value.
			ObjectiveType (str(simulatedUsers|throughputGbps|throughputKbps|throughputMbps)): 
			ObjectiveValue (number): 
			TrafficState (str(Configured|Interim|Running|Unconfigured)): (Read only) A read-only field which indicates the current state of the traffic item.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile.AppLibProfile))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile import AppLibProfile
		return self._select(AppLibProfile(self), locals())

	def add_AppLibProfile(self, ConfiguredFlows=None, EnablePerIPStats=None, ObjectiveDistribution=None, ObjectiveType=None, ObjectiveValue=None):
		"""Adds a child instance of AppLibProfile on the server.

		Args:
			ConfiguredFlows (list(str[])): Configured application library flows within profile.
			EnablePerIPStats (bool): Enable Per IP Stats. When true then Per IP statistic drilldown is available.
			ObjectiveDistribution (str(applyFullObjectiveToEachPort|splitObjectiveEvenlyAmongPorts)): Objective distribution value.
			ObjectiveType (str(simulatedUsers|throughputGbps|throughputKbps|throughputMbps)): 
			ObjectiveValue (number): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile.AppLibProfile)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibprofile import AppLibProfile
		return self._create(AppLibProfile(self), locals())

	def ConfigElement(self, Crc=None, DestinationMacMode=None, EnableDisparityError=None, EncapsulationName=None, EndpointSetId=None, PreambleCustomSize=None, PreambleFrameSizeMode=None):
		"""Gets child instances of ConfigElement from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of ConfigElement will be returned.

		Args:
			Crc (str(badCrc|goodCrc)): 
			DestinationMacMode (str(arp|manual)): 
			EnableDisparityError (bool): 
			EncapsulationName (str): 
			EndpointSetId (number): 
			PreambleCustomSize (number): 
			PreambleFrameSizeMode (str(auto|custom)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.configelement.ConfigElement))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.configelement import ConfigElement
		return self._select(ConfigElement(self), locals())

	def DynamicUpdate(self):
		"""Gets child instances of DynamicUpdate from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DynamicUpdate will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.dynamicupdate.dynamicupdate.DynamicUpdate))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.dynamicupdate.dynamicupdate import DynamicUpdate
		return self._select(DynamicUpdate(self), locals())

	def EgressTracking(self, CustomOffsetBits=None, CustomWidthBits=None, Encapsulation=None, Offset=None):
		"""Gets child instances of EgressTracking from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EgressTracking will be returned.

		Args:
			CustomOffsetBits (number): 
			CustomWidthBits (number): 
			Encapsulation (str): 
			Offset (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking.EgressTracking))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking import EgressTracking
		return self._select(EgressTracking(self), locals())

	def add_EgressTracking(self, CustomOffsetBits=None, CustomWidthBits=None, Encapsulation="Ethernet", Offset="Outer VLAN Priority (3 bits)"):
		"""Adds a child instance of EgressTracking on the server.

		Args:
			CustomOffsetBits (number): 
			CustomWidthBits (number): 
			Encapsulation (str): 
			Offset (str): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking.EgressTracking)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.egresstracking.egresstracking import EgressTracking
		return self._create(EgressTracking(self), locals())

	def EndpointSet(self, AllowEmptyTopologySets=None, DestinationFilter=None, Name=None, SourceFilter=None):
		"""Gets child instances of EndpointSet from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EndpointSet will be returned.

		Args:
			AllowEmptyTopologySets (bool): Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
			DestinationFilter (str): 
			Name (str): 
			SourceFilter (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset.EndpointSet))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset import EndpointSet
		return self._select(EndpointSet(self), locals())

	def add_EndpointSet(self, AllowEmptyTopologySets="False", DestinationFilter=None, Destinations=None, MulticastDestinations=None, MulticastReceivers=None, Name=None, NgpfFilters=None, ScalableDestinations=None, ScalableSources=None, SourceFilter=None, Sources=None, TrafficGroups=None):
		"""Adds a child instance of EndpointSet on the server.

		Args:
			AllowEmptyTopologySets (bool): Enable this to allow the setting of sources and destinations without throwing an error even if the combination produces an empty topology set.
			DestinationFilter (str): 
			Destinations (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*|/api/v1/sessions/1/ixnetwork/topology?deepchild=*|/api/v1/sessions/1/ixnetwork/traffic?deepchild=*|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 
			MulticastDestinations (list(dict(arg1:bool,arg2:str[igmp|mld|none],arg3:str,arg4:str,arg5:number))): A compact representation of many virtual multicast destinations. Each list item consists of 5 values where the first two, a bool value and enum value, can be defaulted to false and none. The next two values are a starting address and step address which can be either an ipv4, ipv6 or streamId and the last value is a count of addresses.
			MulticastReceivers (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:number,arg3:number,arg4:number))): A list of virtual multicast receivers. Each list item consists of a multicast receiver object reference, port index, host index and group or join/prune index depending on the type of object reference.
			Name (str): 
			NgpfFilters (list(dict(arg1:str,arg2:list[number]))): 
			ScalableDestinations (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:number,arg3:number,arg4:number,arg5:number))): 
			ScalableSources (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:number,arg3:number,arg4:number,arg5:number))): 
			SourceFilter (str): 
			Sources (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*|/api/v1/sessions/1/ixnetwork/topology?deepchild=*|/api/v1/sessions/1/ixnetwork/traffic?deepchild=*|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 
			TrafficGroups (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=*])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset.EndpointSet)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.endpointset.endpointset import EndpointSet
		return self._create(EndpointSet(self), locals())

	def HighLevelStream(self, AppliedFrameSize=None, AppliedPacketCount=None, Crc=None, CurrentPacketCount=None, DestinationMacMode=None, Enabled=None, EncapsulationName=None, EndpointSetId=None, Name=None, OverSubscribed=None, Pause=None, PreambleCustomSize=None, PreambleFrameSizeMode=None, State=None, Suspend=None, TxPortId=None, TxPortName=None):
		"""Gets child instances of HighLevelStream from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of HighLevelStream will be returned.

		Args:
			AppliedFrameSize (str): 
			AppliedPacketCount (number): 
			Crc (str(badCrc|goodCrc)): 
			CurrentPacketCount (number): 
			DestinationMacMode (str(arp|manual)): 
			Enabled (bool): 
			EncapsulationName (str): 
			EndpointSetId (number): 
			Name (str): 
			OverSubscribed (bool): 
			Pause (bool): 
			PreambleCustomSize (number): 
			PreambleFrameSizeMode (str(auto|custom)): 
			State (str): 
			Suspend (bool): 
			TxPortId (str(None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport)): 
			TxPortName (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.highlevelstream.HighLevelStream))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.highlevelstream import HighLevelStream
		return self._select(HighLevelStream(self), locals())

	def Tracking(self, FieldWidth=None, Offset=None, OneToOneMesh=None, ProtocolOffset=None):
		"""Gets child instances of Tracking from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Tracking will be returned.

		Args:
			FieldWidth (str(eightBits|sixteenBits|thirtyTwoBits|twentyFourBits)): 
			Offset (number): 
			OneToOneMesh (bool): 
			ProtocolOffset (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.tracking.Tracking))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.tracking.tracking import Tracking
		return self._select(Tracking(self), locals())

	def TransmissionDistribution(self):
		"""Gets child instances of TransmissionDistribution from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TransmissionDistribution will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.transmissiondistribution.transmissiondistribution.TransmissionDistribution))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.transmissiondistribution.transmissiondistribution import TransmissionDistribution
		return self._select(TransmissionDistribution(self), locals())

	@property
	def AllowSelfDestined(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('allowSelfDestined')
	@AllowSelfDestined.setter
	def AllowSelfDestined(self, value):
		self._set_attribute('allowSelfDestined', value)

	@property
	def BiDirectional(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('biDirectional')
	@BiDirectional.setter
	def BiDirectional(self, value):
		self._set_attribute('biDirectional', value)

	@property
	def EgressEnabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('egressEnabled')
	@EgressEnabled.setter
	def EgressEnabled(self, value):
		self._set_attribute('egressEnabled', value)

	@property
	def EnableDynamicMplsLabelValues(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableDynamicMplsLabelValues')
	@EnableDynamicMplsLabelValues.setter
	def EnableDynamicMplsLabelValues(self, value):
		self._set_attribute('enableDynamicMplsLabelValues', value)

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Errors(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('errors')

	@property
	def FlowGroupCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('flowGroupCount')

	@property
	def HasOpenFlow(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('hasOpenFlow')
	@HasOpenFlow.setter
	def HasOpenFlow(self, value):
		self._set_attribute('hasOpenFlow', value)

	@property
	def HostsPerNetwork(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('hostsPerNetwork')
	@HostsPerNetwork.setter
	def HostsPerNetwork(self, value):
		self._set_attribute('hostsPerNetwork', value)

	@property
	def InterAsBgpPreference(self):
		"""

		Returns:
			str(one|two)
		"""
		return self._get_attribute('interAsBgpPreference')
	@InterAsBgpPreference.setter
	def InterAsBgpPreference(self, value):
		self._set_attribute('interAsBgpPreference', value)

	@property
	def InterAsLdpPreference(self):
		"""

		Returns:
			str(one|two)
		"""
		return self._get_attribute('interAsLdpPreference')
	@InterAsLdpPreference.setter
	def InterAsLdpPreference(self, value):
		self._set_attribute('interAsLdpPreference', value)

	@property
	def MaxNumberOfVpnLabelStack(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('maxNumberOfVpnLabelStack')
	@MaxNumberOfVpnLabelStack.setter
	def MaxNumberOfVpnLabelStack(self, value):
		self._set_attribute('maxNumberOfVpnLabelStack', value)

	@property
	def MergeDestinations(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('mergeDestinations')
	@MergeDestinations.setter
	def MergeDestinations(self, value):
		self._set_attribute('mergeDestinations', value)

	@property
	def MulticastForwardingMode(self):
		"""

		Returns:
			str(loadBalancing|replication)
		"""
		return self._get_attribute('multicastForwardingMode')
	@MulticastForwardingMode.setter
	def MulticastForwardingMode(self, value):
		self._set_attribute('multicastForwardingMode', value)

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NumVlansForMulticastReplication(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('numVlansForMulticastReplication')
	@NumVlansForMulticastReplication.setter
	def NumVlansForMulticastReplication(self, value):
		self._set_attribute('numVlansForMulticastReplication', value)

	@property
	def OrdinalNo(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ordinalNo')
	@OrdinalNo.setter
	def OrdinalNo(self, value):
		self._set_attribute('ordinalNo', value)

	@property
	def OriginatorType(self):
		"""

		Returns:
			str(endUser|quickTest)
		"""
		return self._get_attribute('originatorType')
	@OriginatorType.setter
	def OriginatorType(self, value):
		self._set_attribute('originatorType', value)

	@property
	def RoundRobinPacketOrdering(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('roundRobinPacketOrdering')
	@RoundRobinPacketOrdering.setter
	def RoundRobinPacketOrdering(self, value):
		self._set_attribute('roundRobinPacketOrdering', value)

	@property
	def RouteMesh(self):
		"""

		Returns:
			str(fullMesh|oneToOne)
		"""
		return self._get_attribute('routeMesh')
	@RouteMesh.setter
	def RouteMesh(self, value):
		self._set_attribute('routeMesh', value)

	@property
	def SrcDestMesh(self):
		"""

		Returns:
			str(fullMesh|manyToMany|none|oneToOne)
		"""
		return self._get_attribute('srcDestMesh')
	@SrcDestMesh.setter
	def SrcDestMesh(self, value):
		self._set_attribute('srcDestMesh', value)

	@property
	def State(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('state')

	@property
	def Suspend(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('suspend')
	@Suspend.setter
	def Suspend(self, value):
		self._set_attribute('suspend', value)

	@property
	def TrafficItemType(self):
		"""

		Returns:
			str(application|applicationLibrary|l2L3|quick)
		"""
		return self._get_attribute('trafficItemType')
	@TrafficItemType.setter
	def TrafficItemType(self, value):
		self._set_attribute('trafficItemType', value)

	@property
	def TrafficType(self):
		"""

		Returns:
			str(atm|avb1722|avbRaw|ethernetVlan|fc|fcoe|frameRelay|hdlc|ipv4|ipv4ApplicationTraffic|ipv6|ipv6ApplicationTraffic|ppp|raw)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TransmitMode(self):
		"""

		Returns:
			str(interleaved|sequential)
		"""
		return self._get_attribute('transmitMode')
	@TransmitMode.setter
	def TransmitMode(self, value):
		self._set_attribute('transmitMode', value)

	@property
	def TransportLdpPreference(self):
		"""

		Returns:
			str(one|two)
		"""
		return self._get_attribute('transportLdpPreference')
	@TransportLdpPreference.setter
	def TransportLdpPreference(self, value):
		self._set_attribute('transportLdpPreference', value)

	@property
	def TransportRsvpTePreference(self):
		"""

		Returns:
			str(one|two)
		"""
		return self._get_attribute('transportRsvpTePreference')
	@TransportRsvpTePreference.setter
	def TransportRsvpTePreference(self, value):
		self._set_attribute('transportRsvpTePreference', value)

	@property
	def UseControlPlaneFrameSize(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('useControlPlaneFrameSize')
	@UseControlPlaneFrameSize.setter
	def UseControlPlaneFrameSize(self, value):
		self._set_attribute('useControlPlaneFrameSize', value)

	@property
	def UseControlPlaneRate(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('useControlPlaneRate')
	@UseControlPlaneRate.setter
	def UseControlPlaneRate(self, value):
		self._set_attribute('useControlPlaneRate', value)

	@property
	def Warnings(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('warnings')

	def remove(self):
		"""Deletes a child instance of TrafficItem on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def ConvertToRaw(self):
		"""Executes the convertToRaw operation on the server.

		Converts a non-raw traffic item to a raw traffic item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('convertToRaw', payload=locals(), response_object=None)

	def Duplicate(self, Arg2):
		"""Executes the duplicate operation on the server.

		Duplicates a specific traffic item.

		Args:
			Arg2 (number): The number of times to duplicate the traffic item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('duplicate', payload=locals(), response_object=None)

	def DuplicateItems(self, Arg1):
		"""Executes the duplicateItems operation on the server.

		Duplicates a list of traffic items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('duplicateItems', payload=locals(), response_object=None)

	def Generate(self, Arg1):
		"""Executes the generate operation on the server.

		Generate traffic for specific traffic items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('generate', payload=locals(), response_object=None)

	def Generate(self):
		"""Executes the generate operation on the server.

		Generate traffic for a specific traffic item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('generate', payload=locals(), response_object=None)

	def ResolveAptixiaEndpoints(self, Arg1):
		"""Executes the resolveAptixiaEndpoints operation on the server.

		Resolves /vport/protocolStack/. endpoints being used by a specific traffic item.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.

		Returns:
			str: This exec returns a string containing the resolved endpoints.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resolveAptixiaEndpoints', payload=locals(), response_object=None)

	def StartDefaultLearning(self, Arg1):
		"""Executes the startDefaultLearning operation on the server.

		Starts default learning for a list of traffic items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startDefaultLearning', payload=locals(), response_object=None)

	def StartDefaultLearning(self):
		"""Executes the startDefaultLearning operation on the server.

		Starts default learning for a specific traffic item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('startDefaultLearning', payload=locals(), response_object=None)

	def StartLearning(self, Arg1, Arg2, Arg3, Arg4):
		"""Executes the startLearning operation on the server.

		Sends learning frames.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.
			Arg2 (number): The framesize of the learning frame.
			Arg3 (number): The framecount of the learning frames.
			Arg4 (number): The frames per second of the learning frames.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startLearning', payload=locals(), response_object=None)

	def StartLearning(self, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7):
		"""Executes the startLearning operation on the server.

		Sends learning frames.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.
			Arg2 (number): The framesize of the learning frame.
			Arg3 (number): The framecount of the learning frames.
			Arg4 (number): The frames per second of the learning frames.
			Arg5 (bool): Send gratuitous ARP frames.
			Arg6 (bool): Send MAC frames.
			Arg7 (bool): Send Fast Path frames.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startLearning', payload=locals(), response_object=None)

	def StartLearning(self, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8):
		"""Executes the startLearning operation on the server.

		Sends learning frames.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem])): An array of valid object references.
			Arg2 (number): The framesize of the learning frame.
			Arg3 (number): The framecount of the learning frames.
			Arg4 (number): The frames per second of the learning frames.
			Arg5 (bool): Send gratuitous ARP frames.
			Arg6 (bool): Send MAC frames.
			Arg7 (bool): Send Fast Path frames.
			Arg8 (bool): Send full mesh.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startLearning', payload=locals(), response_object=None)

	def StartStatelessTraffic(self, Arg1):
		"""Executes the startStatelessTraffic operation on the server.

		Start the traffic configuration for stateless traffic items only.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startStatelessTraffic', payload=locals(), response_object=None)

	def StartStatelessTrafficBlocking(self, Arg1):
		"""Executes the startStatelessTrafficBlocking operation on the server.

		Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startStatelessTrafficBlocking', payload=locals(), response_object=None)

	def StopStatelessTraffic(self, Arg1):
		"""Executes the stopStatelessTraffic operation on the server.

		Stop the stateless traffic items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopStatelessTraffic', payload=locals(), response_object=None)

	def StopStatelessTrafficBlocking(self, Arg1):
		"""Executes the stopStatelessTrafficBlocking operation on the server.

		Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopStatelessTrafficBlocking', payload=locals(), response_object=None)
