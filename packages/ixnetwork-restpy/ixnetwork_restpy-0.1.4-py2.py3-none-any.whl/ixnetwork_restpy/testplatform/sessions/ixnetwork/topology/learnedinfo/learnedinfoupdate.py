from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LearnedInfoUpdate(Base):
	"""The learned information trigger node that contains trigger tables of learned information.
	"""

	_SDM_NAME = 'learnedInfoUpdate'

	def __init__(self, parent):
		super(LearnedInfoUpdate, self).__init__(parent)

	def PceBasicRsvpSyncLspUpdateParams(self, Bandwidth=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, LocalProtection=None, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, OverrideSrpId=None, PceTriggersChoiceList=None, SetupPriority=None, SrpId=None):
		"""Gets child instances of PceBasicRsvpSyncLspUpdateParams from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceBasicRsvpSyncLspUpdateParams will be returned.

		Args:
			Bandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth (bps)
			ConfigureBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Bandwidth
			ConfigureEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure ERO
			ConfigureLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSP
			ConfigureLspa (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSPA
			ConfigureMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Metric
			ExcludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Exclude Any
			HoldingPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Holding Priority
			IncludeAll (obj(ixnetwork_restpy.multivalue.Multivalue)): Include All
			IncludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Any
			IncludeSrp (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			IncludeSymbolicPathName (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
			LocalProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Protection
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
			OverrideSrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			PceTriggersChoiceList (obj(ixnetwork_restpy.multivalue.Multivalue)): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
			SetupPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Setup Priority
			SrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams.PceBasicRsvpSyncLspUpdateParams))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicrsvpsynclspupdateparams import PceBasicRsvpSyncLspUpdateParams
		return self._select(PceBasicRsvpSyncLspUpdateParams(self), locals())

	def PceBasicSrSyncLspUpdateParams(self, Bandwidth=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, LocalProtection=None, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, OverrideSrpId=None, PceTriggersChoiceList=None, SetupPriority=None, SrpId=None):
		"""Gets child instances of PceBasicSrSyncLspUpdateParams from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceBasicSrSyncLspUpdateParams will be returned.

		Args:
			Bandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth (bps)
			ConfigureBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Bandwidth
			ConfigureEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure ERO
			ConfigureLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSP
			ConfigureLspa (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSPA
			ConfigureMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Metric
			ExcludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Exclude Any
			HoldingPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Holding Priority
			IncludeAll (obj(ixnetwork_restpy.multivalue.Multivalue)): Include All
			IncludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Any
			IncludeSrp (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			IncludeSymbolicPathName (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
			LocalProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Protection
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
			OverrideSrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			PceTriggersChoiceList (obj(ixnetwork_restpy.multivalue.Multivalue)): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
			SetupPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Setup Priority
			SrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams.PceBasicSrSyncLspUpdateParams))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcebasicsrsynclspupdateparams import PceBasicSrSyncLspUpdateParams
		return self._select(PceBasicSrSyncLspUpdateParams(self), locals())

	def PceDetailedRsvpSyncLspUpdateParams(self, Bandwidth=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, LocalProtection=None, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, OverrideSrpId=None, PceTriggersChoiceList=None, SetupPriority=None, SrpId=None):
		"""Gets child instances of PceDetailedRsvpSyncLspUpdateParams from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceDetailedRsvpSyncLspUpdateParams will be returned.

		Args:
			Bandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth (bps)
			ConfigureBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Bandwidth
			ConfigureEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure ERO
			ConfigureLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSP
			ConfigureLspa (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSPA
			ConfigureMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Metric
			ExcludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Exclude Any
			HoldingPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Holding Priority
			IncludeAll (obj(ixnetwork_restpy.multivalue.Multivalue)): Include All
			IncludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Any
			IncludeSrp (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			IncludeSymbolicPathName (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
			LocalProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Protection
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
			OverrideSrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			PceTriggersChoiceList (obj(ixnetwork_restpy.multivalue.Multivalue)): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
			SetupPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Setup Priority
			SrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams.PceDetailedRsvpSyncLspUpdateParams))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedrsvpsynclspupdateparams import PceDetailedRsvpSyncLspUpdateParams
		return self._select(PceDetailedRsvpSyncLspUpdateParams(self), locals())

	def PceDetailedSrSyncLspUpdateParams(self, Bandwidth=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, LocalProtection=None, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, OverrideSrpId=None, PceTriggersChoiceList=None, SetupPriority=None, SrpId=None):
		"""Gets child instances of PceDetailedSrSyncLspUpdateParams from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceDetailedSrSyncLspUpdateParams will be returned.

		Args:
			Bandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth (bps)
			ConfigureBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Bandwidth
			ConfigureEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure ERO
			ConfigureLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSP
			ConfigureLspa (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure LSPA
			ConfigureMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure Metric
			ExcludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Exclude Any
			HoldingPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Holding Priority
			IncludeAll (obj(ixnetwork_restpy.multivalue.Multivalue)): Include All
			IncludeAny (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Any
			IncludeSrp (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			IncludeSymbolicPathName (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
			LocalProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Protection
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
			OverrideSrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
			PceTriggersChoiceList (obj(ixnetwork_restpy.multivalue.Multivalue)): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
			SetupPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Setup Priority
			SrpId (obj(ixnetwork_restpy.multivalue.Multivalue)): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams.PceDetailedSrSyncLspUpdateParams))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pcedetailedsrsynclspupdateparams import PceDetailedSrSyncLspUpdateParams
		return self._select(PceDetailedSrSyncLspUpdateParams(self), locals())

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
