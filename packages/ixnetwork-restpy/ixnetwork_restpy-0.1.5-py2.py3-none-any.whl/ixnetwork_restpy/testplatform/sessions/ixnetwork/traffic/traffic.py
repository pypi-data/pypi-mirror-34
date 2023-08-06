from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Traffic(Base):
	"""
	"""

	_SDM_NAME = 'traffic'

	def __init__(self, parent):
		super(Traffic, self).__init__(parent)

	def DynamicFrameSize(self, FixedSize=None, HighLevelStreamName=None, RandomMax=None, RandomMin=None, TrafficItemName=None, Type=None):
		"""Gets child instances of DynamicFrameSize from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DynamicFrameSize will be returned.

		Args:
			FixedSize (number): 
			HighLevelStreamName (str): The name of the high level stream
			RandomMax (number): 
			RandomMin (number): 
			TrafficItemName (str): The name of the parent traffic item.
			Type (str(fixed|random)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize.DynamicFrameSize))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize import DynamicFrameSize
		return self._select(DynamicFrameSize(self), locals())

	def DynamicRate(self, BitRateUnitsType=None, EnforceMinimumInterPacketGap=None, HighLevelStreamName=None, InterPacketGapUnitsType=None, OverSubscribed=None, Rate=None, RateType=None, TrafficItemName=None, TxPort=None):
		"""Gets child instances of DynamicRate from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DynamicRate will be returned.

		Args:
			BitRateUnitsType (str(bitsPerSec|bytesPerSec|kbitsPerSec|kbytesPerSec|mbitsPerSec|mbytesPerSec)): 
			EnforceMinimumInterPacketGap (number): 
			HighLevelStreamName (str): The name of the high level stream
			InterPacketGapUnitsType (str(bytes|nanoseconds)): 
			OverSubscribed (bool): 
			Rate (number): 
			RateType (str(bitsPerSecond|framesPerSecond|interPacketGap|percentLineRate)): 
			TrafficItemName (str): The name of the parent traffic item.
			TxPort (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate.DynamicRate))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate import DynamicRate
		return self._select(DynamicRate(self), locals())

	def EgressOnlyTracking(self, Enabled=None, Port=None, SignatureOffset=None, SignatureValue=None):
		"""Gets child instances of EgressOnlyTracking from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EgressOnlyTracking will be returned.

		Args:
			Enabled (bool): Enables the egress only tracking for the given port.
			Port (str(None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport)): 
			SignatureOffset (number): Offset where the signature value will be placed in the packet.
			SignatureValue (str): Signature value to be placed inside the packet.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking.EgressOnlyTracking))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking import EgressOnlyTracking
		return self._select(EgressOnlyTracking(self), locals())

	def add_EgressOnlyTracking(self, Egress=None, Enabled=None, Port=None, SignatureOffset=None, SignatureValue=None):
		"""Adds a child instance of EgressOnlyTracking on the server.

		Args:
			Egress (list(dict(arg1:number,arg2:str))): Struct contains: egress offset and egress mask
			Enabled (bool): Enables the egress only tracking for the given port.
			Port (str(None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport)): 
			SignatureOffset (number): Offset where the signature value will be placed in the packet.
			SignatureValue (str): Signature value to be placed inside the packet.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking.EgressOnlyTracking)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking import EgressOnlyTracking
		return self._create(EgressOnlyTracking(self), locals())

	def ProtocolTemplate(self, DisplayName=None, StackTypeId=None, TemplateName=None):
		"""Gets child instances of ProtocolTemplate from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of ProtocolTemplate will be returned.

		Args:
			DisplayName (str): 
			StackTypeId (str): 
			TemplateName (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate.ProtocolTemplate))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate import ProtocolTemplate
		return self._select(ProtocolTemplate(self), locals())

	@property
	def Statistics(self):
		"""Returns the one and only one Statistics object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics.Statistics)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics import Statistics
		return self._read(Statistics(self), None)

	def TrafficItem(self, AllowSelfDestined=None, BiDirectional=None, EgressEnabled=None, EnableDynamicMplsLabelValues=None, Enabled=None, FlowGroupCount=None, HasOpenFlow=None, HostsPerNetwork=None, InterAsBgpPreference=None, InterAsLdpPreference=None, MaxNumberOfVpnLabelStack=None, MergeDestinations=None, MulticastForwardingMode=None, Name=None, NumVlansForMulticastReplication=None, OrdinalNo=None, OriginatorType=None, RoundRobinPacketOrdering=None, RouteMesh=None, SrcDestMesh=None, State=None, Suspend=None, TrafficItemType=None, TrafficType=None, TransmitMode=None, TransportLdpPreference=None, TransportRsvpTePreference=None, UseControlPlaneFrameSize=None, UseControlPlaneRate=None):
		"""Gets child instances of TrafficItem from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TrafficItem will be returned.

		Args:
			AllowSelfDestined (bool): 
			BiDirectional (bool): 
			EgressEnabled (bool): 
			EnableDynamicMplsLabelValues (bool): 
			Enabled (bool): 
			FlowGroupCount (number): 
			HasOpenFlow (bool): 
			HostsPerNetwork (number): 
			InterAsBgpPreference (str(one|two)): 
			InterAsLdpPreference (str(one|two)): 
			MaxNumberOfVpnLabelStack (number): 
			MergeDestinations (bool): 
			MulticastForwardingMode (str(loadBalancing|replication)): 
			Name (str): 
			NumVlansForMulticastReplication (number): 
			OrdinalNo (number): 
			OriginatorType (str(endUser|quickTest)): 
			RoundRobinPacketOrdering (bool): 
			RouteMesh (str(fullMesh|oneToOne)): 
			SrcDestMesh (str(fullMesh|manyToMany|none|oneToOne)): 
			State (str): 
			Suspend (bool): 
			TrafficItemType (str(application|applicationLibrary|l2L3|quick)): 
			TrafficType (str(atm|avb1722|avbRaw|ethernetVlan|fc|fcoe|frameRelay|hdlc|ipv4|ipv4ApplicationTraffic|ipv6|ipv6ApplicationTraffic|ppp|raw)): 
			TransmitMode (str(interleaved|sequential)): 
			TransportLdpPreference (str(one|two)): 
			TransportRsvpTePreference (str(one|two)): 
			UseControlPlaneFrameSize (bool): 
			UseControlPlaneRate (bool): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem.TrafficItem))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem import TrafficItem
		return self._select(TrafficItem(self), locals())

	def add_TrafficItem(self, AllowSelfDestined=None, BiDirectional=None, EgressEnabled=None, EnableDynamicMplsLabelValues=None, Enabled=None, HasOpenFlow="False", HostsPerNetwork=None, InterAsBgpPreference=None, InterAsLdpPreference=None, MaxNumberOfVpnLabelStack=None, MergeDestinations=None, MulticastForwardingMode=None, Name=None, NumVlansForMulticastReplication=None, OrdinalNo=None, OriginatorType="endUser", RoundRobinPacketOrdering=None, RouteMesh=None, SrcDestMesh=None, Suspend=None, TrafficItemType=None, TrafficType=None, TransmitMode=None, TransportLdpPreference=None, TransportRsvpTePreference=None, UseControlPlaneFrameSize=None, UseControlPlaneRate=None):
		"""Adds a child instance of TrafficItem on the server.

		Args:
			AllowSelfDestined (bool): 
			BiDirectional (bool): 
			EgressEnabled (bool): 
			EnableDynamicMplsLabelValues (bool): 
			Enabled (bool): 
			HasOpenFlow (bool): 
			HostsPerNetwork (number): 
			InterAsBgpPreference (str(one|two)): 
			InterAsLdpPreference (str(one|two)): 
			MaxNumberOfVpnLabelStack (number): 
			MergeDestinations (bool): 
			MulticastForwardingMode (str(loadBalancing|replication)): 
			Name (str): 
			NumVlansForMulticastReplication (number): 
			OrdinalNo (number): 
			OriginatorType (str(endUser|quickTest)): 
			RoundRobinPacketOrdering (bool): 
			RouteMesh (str(fullMesh|oneToOne)): 
			SrcDestMesh (str(fullMesh|manyToMany|none|oneToOne)): 
			Suspend (bool): 
			TrafficItemType (str(application|applicationLibrary|l2L3|quick)): 
			TrafficType (str(atm|avb1722|avbRaw|ethernetVlan|fc|fcoe|frameRelay|hdlc|ipv4|ipv4ApplicationTraffic|ipv6|ipv6ApplicationTraffic|ppp|raw)): 
			TransmitMode (str(interleaved|sequential)): 
			TransportLdpPreference (str(one|two)): 
			TransportRsvpTePreference (str(one|two)): 
			UseControlPlaneFrameSize (bool): 
			UseControlPlaneRate (bool): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem.TrafficItem)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem import TrafficItem
		return self._create(TrafficItem(self), locals())

	@property
	def AutoCorrectL4HeaderChecksums(self):
		"""This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.

		Returns:
			bool
		"""
		return self._get_attribute('autoCorrectL4HeaderChecksums')
	@AutoCorrectL4HeaderChecksums.setter
	def AutoCorrectL4HeaderChecksums(self, value):
		self._set_attribute('autoCorrectL4HeaderChecksums', value)

	@property
	def CycleOffsetForScheduledStart(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('cycleOffsetForScheduledStart')
	@CycleOffsetForScheduledStart.setter
	def CycleOffsetForScheduledStart(self, value):
		self._set_attribute('cycleOffsetForScheduledStart', value)

	@property
	def CycleOffsetUnitForScheduledStart(self):
		"""

		Returns:
			str(microseconds|milliseconds|nanoseconds|seconds)
		"""
		return self._get_attribute('cycleOffsetUnitForScheduledStart')
	@CycleOffsetUnitForScheduledStart.setter
	def CycleOffsetUnitForScheduledStart(self, value):
		self._set_attribute('cycleOffsetUnitForScheduledStart', value)

	@property
	def CycleTimeForScheduledStart(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('cycleTimeForScheduledStart')
	@CycleTimeForScheduledStart.setter
	def CycleTimeForScheduledStart(self, value):
		self._set_attribute('cycleTimeForScheduledStart', value)

	@property
	def CycleTimeUnitForScheduledStart(self):
		"""

		Returns:
			str(microseconds|milliseconds|nanoseconds|seconds)
		"""
		return self._get_attribute('cycleTimeUnitForScheduledStart')
	@CycleTimeUnitForScheduledStart.setter
	def CycleTimeUnitForScheduledStart(self, value):
		self._set_attribute('cycleTimeUnitForScheduledStart', value)

	@property
	def DataPlaneJitterWindow(self):
		"""

		Returns:
			str(0|10485760|1310720|167772160|20971520|2621440|335544320|41943040|5242880|671088640|83886080)
		"""
		return self._get_attribute('dataPlaneJitterWindow')
	@DataPlaneJitterWindow.setter
	def DataPlaneJitterWindow(self, value):
		self._set_attribute('dataPlaneJitterWindow', value)

	@property
	def DelayTimeForScheduledStart(self):
		"""Delay Time For Scheduled Start Transmit in seconds

		Returns:
			number
		"""
		return self._get_attribute('delayTimeForScheduledStart')
	@DelayTimeForScheduledStart.setter
	def DelayTimeForScheduledStart(self, value):
		self._set_attribute('delayTimeForScheduledStart', value)

	@property
	def DestMacRetryCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('destMacRetryCount')
	@DestMacRetryCount.setter
	def DestMacRetryCount(self, value):
		self._set_attribute('destMacRetryCount', value)

	@property
	def DestMacRetryDelay(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('destMacRetryDelay')
	@DestMacRetryDelay.setter
	def DestMacRetryDelay(self, value):
		self._set_attribute('destMacRetryDelay', value)

	@property
	def DetectMisdirectedOnAllPorts(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('detectMisdirectedOnAllPorts')
	@DetectMisdirectedOnAllPorts.setter
	def DetectMisdirectedOnAllPorts(self, value):
		self._set_attribute('detectMisdirectedOnAllPorts', value)

	@property
	def DisplayMplsCurrentLabelValue(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('displayMplsCurrentLabelValue')
	@DisplayMplsCurrentLabelValue.setter
	def DisplayMplsCurrentLabelValue(self, value):
		self._set_attribute('displayMplsCurrentLabelValue', value)

	@property
	def ElapsedTransmitTime(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('elapsedTransmitTime')

	@property
	def EnableDataIntegrityCheck(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrityCheck')
	@EnableDataIntegrityCheck.setter
	def EnableDataIntegrityCheck(self, value):
		self._set_attribute('enableDataIntegrityCheck', value)

	@property
	def EnableDestMacRetry(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableDestMacRetry')
	@EnableDestMacRetry.setter
	def EnableDestMacRetry(self, value):
		self._set_attribute('enableDestMacRetry', value)

	@property
	def EnableEgressOnlyTracking(self):
		"""This flags enables/disables egress only tracking on the quick flow group. In this mode only quick flow groups are supported, user will have only PGID stats and the packets will not contain any instrumentation block.

		Returns:
			bool
		"""
		return self._get_attribute('enableEgressOnlyTracking')
	@EnableEgressOnlyTracking.setter
	def EnableEgressOnlyTracking(self, value):
		self._set_attribute('enableEgressOnlyTracking', value)

	@property
	def EnableInstantaneousStatsSupport(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableInstantaneousStatsSupport')
	@EnableInstantaneousStatsSupport.setter
	def EnableInstantaneousStatsSupport(self, value):
		self._set_attribute('enableInstantaneousStatsSupport', value)

	@property
	def EnableLagFlowBalancing(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableLagFlowBalancing')
	@EnableLagFlowBalancing.setter
	def EnableLagFlowBalancing(self, value):
		self._set_attribute('enableLagFlowBalancing', value)

	@property
	def EnableMinFrameSize(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableMulticastScalingFactor(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastScalingFactor')
	@EnableMulticastScalingFactor.setter
	def EnableMulticastScalingFactor(self, value):
		self._set_attribute('enableMulticastScalingFactor', value)

	@property
	def EnableSequenceChecking(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableSequenceChecking')
	@EnableSequenceChecking.setter
	def EnableSequenceChecking(self, value):
		self._set_attribute('enableSequenceChecking', value)

	@property
	def EnableStaggeredStartDelay(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableStaggeredStartDelay')
	@EnableStaggeredStartDelay.setter
	def EnableStaggeredStartDelay(self, value):
		self._set_attribute('enableStaggeredStartDelay', value)

	@property
	def EnableStaggeredTransmit(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableStaggeredTransmit')
	@EnableStaggeredTransmit.setter
	def EnableStaggeredTransmit(self, value):
		self._set_attribute('enableStaggeredTransmit', value)

	@property
	def EnableStreamOrdering(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableStreamOrdering')
	@EnableStreamOrdering.setter
	def EnableStreamOrdering(self, value):
		self._set_attribute('enableStreamOrdering', value)

	@property
	def FrameOrderingMode(self):
		"""

		Returns:
			str(flowGroupSetup|none|peakLoading|RFC2889)
		"""
		return self._get_attribute('frameOrderingMode')
	@FrameOrderingMode.setter
	def FrameOrderingMode(self, value):
		self._set_attribute('frameOrderingMode', value)

	@property
	def GlobalStreamControl(self):
		"""

		Returns:
			str(continuous|iterations)
		"""
		return self._get_attribute('globalStreamControl')
	@GlobalStreamControl.setter
	def GlobalStreamControl(self, value):
		self._set_attribute('globalStreamControl', value)

	@property
	def GlobalStreamControlIterations(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('globalStreamControlIterations')
	@GlobalStreamControlIterations.setter
	def GlobalStreamControlIterations(self, value):
		self._set_attribute('globalStreamControlIterations', value)

	@property
	def IsApplicationTrafficRunning(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isApplicationTrafficRunning')

	@property
	def IsApplyOnTheFlyRequired(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isApplyOnTheFlyRequired')

	@property
	def IsTrafficRunning(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isTrafficRunning')

	@property
	def LargeErrorThreshhold(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('largeErrorThreshhold')
	@LargeErrorThreshhold.setter
	def LargeErrorThreshhold(self, value):
		self._set_attribute('largeErrorThreshhold', value)

	@property
	def LearningFrameSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('learningFrameSize')
	@LearningFrameSize.setter
	def LearningFrameSize(self, value):
		self._set_attribute('learningFrameSize', value)

	@property
	def LearningFramesCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('learningFramesCount')
	@LearningFramesCount.setter
	def LearningFramesCount(self, value):
		self._set_attribute('learningFramesCount', value)

	@property
	def LearningFramesRate(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('learningFramesRate')
	@LearningFramesRate.setter
	def LearningFramesRate(self, value):
		self._set_attribute('learningFramesRate', value)

	@property
	def MacChangeOnFly(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('macChangeOnFly')
	@MacChangeOnFly.setter
	def MacChangeOnFly(self, value):
		self._set_attribute('macChangeOnFly', value)

	@property
	def MaxTrafficGenerationQueries(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('maxTrafficGenerationQueries')
	@MaxTrafficGenerationQueries.setter
	def MaxTrafficGenerationQueries(self, value):
		self._set_attribute('maxTrafficGenerationQueries', value)

	@property
	def MplsLabelLearningTimeout(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('mplsLabelLearningTimeout')
	@MplsLabelLearningTimeout.setter
	def MplsLabelLearningTimeout(self, value):
		self._set_attribute('mplsLabelLearningTimeout', value)

	@property
	def PeakLoadingReplicationCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('peakLoadingReplicationCount')
	@PeakLoadingReplicationCount.setter
	def PeakLoadingReplicationCount(self, value):
		self._set_attribute('peakLoadingReplicationCount', value)

	@property
	def PreventDataPlaneToCpu(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('preventDataPlaneToCpu')
	@PreventDataPlaneToCpu.setter
	def PreventDataPlaneToCpu(self, value):
		self._set_attribute('preventDataPlaneToCpu', value)

	@property
	def RefreshLearnedInfoBeforeApply(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('refreshLearnedInfoBeforeApply')
	@RefreshLearnedInfoBeforeApply.setter
	def RefreshLearnedInfoBeforeApply(self, value):
		self._set_attribute('refreshLearnedInfoBeforeApply', value)

	@property
	def State(self):
		"""

		Returns:
			str(error|locked|started|startedWaitingForStats|startedWaitingForStreams|stopped|stoppedWaitingForStats|txStopWatchExpected|unapplied)
		"""
		return self._get_attribute('state')

	@property
	def UseRfc5952(self):
		"""Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)

		Returns:
			bool
		"""
		return self._get_attribute('useRfc5952')
	@UseRfc5952.setter
	def UseRfc5952(self, value):
		self._set_attribute('useRfc5952', value)

	@property
	def UseScheduledStartTransmit(self):
		"""Use Scheduled Start Transmit

		Returns:
			bool
		"""
		return self._get_attribute('useScheduledStartTransmit')
	@UseScheduledStartTransmit.setter
	def UseScheduledStartTransmit(self, value):
		self._set_attribute('useScheduledStartTransmit', value)

	@property
	def UseTxRxSync(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('useTxRxSync')
	@UseTxRxSync.setter
	def UseTxRxSync(self, value):
		self._set_attribute('useTxRxSync', value)

	@property
	def WaitTime(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('waitTime')
	@WaitTime.setter
	def WaitTime(self, value):
		self._set_attribute('waitTime', value)

	def Apply(self):
		"""Executes the apply operation on the server.

		Apply the traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('apply', payload=locals(), response_object=None)

	def ApplyApplicationTraffic(self):
		"""Executes the applyApplicationTraffic operation on the server.

		Apply the stateful traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('applyApplicationTraffic', payload=locals(), response_object=None)

	def ApplyOnTheFlyTrafficChanges(self):
		"""Executes the applyOnTheFlyTrafficChanges operation on the server.

		Apply on the fly traffic changes.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('applyOnTheFlyTrafficChanges', payload=locals(), response_object=None)

	def ApplyStatefulTraffic(self):
		"""Executes the applyStatefulTraffic operation on the server.

		Apply the traffic configuration for stateful traffic items only.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('applyStatefulTraffic', payload=locals(), response_object=None)

	def GenerateIfRequired(self):
		"""Executes the generateIfRequired operation on the server.

		causes regeneration of dirty traffic items

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('generateIfRequired', payload=locals(), response_object=None)

	def GetFrameCountForDuration(self, Arg2):
		"""Executes the getFrameCountForDuration operation on the server.

		Get the frame count for a specific duration.

		Args:
			Arg2 (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream],arg2:number))): An array of structures. Each structure is one valid highLevelStream object reference and the duration to get the frame count for.

		Returns:
			list(number): An array of frame counts.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getFrameCountForDuration', payload=locals(), response_object=None)

	def MakeStatelessTrafficUnapplied(self):
		"""Executes the makeStatelessTrafficUnapplied operation on the server.

		Move stateless traffic to unapplied state.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('makeStatelessTrafficUnapplied', payload=locals(), response_object=None)

	def SendL2L3Learning(self):
		"""Executes the sendL2L3Learning operation on the server.

		Send L2 and L3 learning frames.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendL2L3Learning', payload=locals(), response_object=None)

	def Start(self):
		"""Executes the start operation on the server.

		Start the traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('start', payload=locals(), response_object=None)

	def StartApplicationTraffic(self):
		"""Executes the startApplicationTraffic operation on the server.

		Start the stateful traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('startApplicationTraffic', payload=locals(), response_object=None)

	def StartStatefulTraffic(self):
		"""Executes the startStatefulTraffic operation on the server.

		Start stateful traffic items only.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('startStatefulTraffic', payload=locals(), response_object=None)

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

	def Stop(self):
		"""Executes the stop operation on the server.

		Stop the traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stop', payload=locals(), response_object=None)

	def StopApplicationTraffic(self):
		"""Executes the stopApplicationTraffic operation on the server.

		Stop the stateful traffic configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopApplicationTraffic', payload=locals(), response_object=None)

	def StopStatefulTraffic(self):
		"""Executes the stopStatefulTraffic operation on the server.

		Stop stateful traffic items only.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopStatefulTraffic', payload=locals(), response_object=None)

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
