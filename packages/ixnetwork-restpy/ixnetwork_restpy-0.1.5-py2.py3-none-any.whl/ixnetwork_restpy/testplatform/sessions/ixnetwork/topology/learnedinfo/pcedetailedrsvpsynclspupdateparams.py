from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PceDetailedRsvpSyncLspUpdateParams(Base):
	"""PCE Learned LSPs Information Database
	"""

	_SDM_NAME = 'pceDetailedRsvpSyncLspUpdateParams'

	def __init__(self, parent):
		super(PceDetailedRsvpSyncLspUpdateParams, self).__init__(parent)

	def PceUpdateRsvpEroSubObjectList(self, ActiveThisEro=None, AsNumber=None, Ipv4Prefix=None, Ipv6Prefix=None, LooseHop=None, PrefixLength=None, SubObjectType=None):
		"""Gets child instances of PceUpdateRsvpEroSubObjectList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceUpdateRsvpEroSubObjectList will be returned.

		Args:
			ActiveThisEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls whether the ERO sub-object will be sent in the PCInitiate message.
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS Number
			Ipv4Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Prefix is specified as an IPv4 address.
			Ipv6Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Prefix is specified as an IPv6 address.
			LooseHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if user wants to represent a loose-hop sub object in the LSP
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			SubObjectType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: Not Applicable IPv4 Prefix IPv6 Prefix AS Number.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist.PceUpdateRsvpEroSubObjectList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist import PceUpdateRsvpEroSubObjectList
		return self._select(PceUpdateRsvpEroSubObjectList(self), locals())

	def PceUpdateRsvpMetricSubObjectList(self, ActiveThisMetric=None, BFlag=None, MetricType=None, MetricValue=None):
		"""Gets child instances of PceUpdateRsvpMetricSubObjectList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceUpdateRsvpMetricSubObjectList will be returned.

		Args:
			ActiveThisMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies whether the corresponding metric object is active or not.
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): B (bound) flag MUST be set in the METRIC object, which specifies that the SID depth for the computed path MUST NOT exceed the metric-value.
			MetricType (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a drop down which has 4 choices: IGP/ TE/ Hop count/ MSD.
			MetricValue (obj(ixnetwork_restpy.multivalue.Multivalue)): User can specify the metric value corresponding to the metric type selected.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist.PceUpdateRsvpMetricSubObjectList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist import PceUpdateRsvpMetricSubObjectList
		return self._select(PceUpdateRsvpMetricSubObjectList(self), locals())

	@property
	def Bandwidth(self):
		"""Bandwidth (bps)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def ConfigureBandwidth(self):
		"""Configure Bandwidth

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureBandwidth')

	@property
	def ConfigureEro(self):
		"""Configure ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureEro')

	@property
	def ConfigureLsp(self):
		"""Configure LSP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureLsp')

	@property
	def ConfigureLspa(self):
		"""Configure LSPA

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureLspa')

	@property
	def ConfigureMetric(self):
		"""Configure Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureMetric')

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def HoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def IncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeSrp(self):
		"""Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSrp')

	@property
	def IncludeSymbolicPathName(self):
		"""Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathName')

	@property
	def LocalProtection(self):
		"""Local Protection

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtection')

	@property
	def NumberOfEroSubObjects(self):
		"""Value that indicates the number of ERO Sub Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfEroSubObjects')
	@NumberOfEroSubObjects.setter
	def NumberOfEroSubObjects(self, value):
		self._set_attribute('numberOfEroSubObjects', value)

	@property
	def NumberOfMetricSubObjects(self):
		"""Value that indicates the number of Metric Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfMetricSubObjects')
	@NumberOfMetricSubObjects.setter
	def NumberOfMetricSubObjects(self, value):
		self._set_attribute('numberOfMetricSubObjects', value)

	@property
	def OverrideSrpId(self):
		"""Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('overrideSrpId')

	@property
	def PceTriggersChoiceList(self):
		"""Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pceTriggersChoiceList')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SrpId(self):
		"""The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srpId')

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

	def SendPcUpdate(self, Arg2):
		"""Executes the sendPcUpdate operation on the server.

		Counts property changes created by the user.

		Args:
			Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendPcUpdate', payload=locals(), response_object=None)
