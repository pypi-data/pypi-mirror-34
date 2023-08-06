from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PceDetailedSrSyncLspUpdateParams(Base):
	"""PCE Learned LSPs Information Database
	"""

	_SDM_NAME = 'pceDetailedSrSyncLspUpdateParams'

	def __init__(self, parent):
		super(PceDetailedSrSyncLspUpdateParams, self).__init__(parent)

	def PceUpdateSrEroSubObjectList(self, ActiveThisEro=None, Bos=None, FBit=None, Ipv4NodeId=None, Ipv6NodeId=None, LocalInterfaceId=None, LocalIpv4Address=None, LocalIpv6Address=None, LocalNodeId=None, LooseHop=None, MplsLabel=None, MplsLabel32=None, NaiType=None, RemoteInterfaceId=None, RemoteIpv4Address=None, RemoteIpv6Address=None, RemoteNodeId=None, Sid=None, SidType=None, Tc=None, Ttl=None):
		"""Gets child instances of PceUpdateSrEroSubObjectList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceUpdateSrEroSubObjectList will be returned.

		Args:
			ActiveThisEro (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls whether the ERO sub-object will be sent in the PCInitiate message.
			Bos (obj(ixnetwork_restpy.multivalue.Multivalue)): This bit is set to true for the last entry in the label stack i.e., for the bottom of the stack, and false for all other label stack entries. This control will be editable only if SID Type is MPLS Label 32bit.
			FBit (obj(ixnetwork_restpy.multivalue.Multivalue)): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
			Ipv4NodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Node ID is specified as an IPv4 address. This control can be configured if NAI Type is set to IPv4 Node ID and F bit is disabled.
			Ipv6NodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.
			LocalInterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Local Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			LocalIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
			LocalIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
			LocalNodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Local Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			LooseHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if user wants to represent a loose-hop sub object in the LSP
			MplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): This control will be editable if the SID Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
			MplsLabel32 (obj(ixnetwork_restpy.multivalue.Multivalue)): MPLS Label 32 Bit
			NaiType (obj(ixnetwork_restpy.multivalue.Multivalue)): NAI (Node or Adjacency Identifier) contains the NAI associated with the SID. Depending on the value of SID Type, the NAI can have different formats such as, Not Applicable IPv4 Node ID IPv6 Node ID IPv4 Adjacency IPv6 Adjacency Unnumbered Adjacency with IPv4 NodeIDs
			RemoteInterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Remote Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			RemoteIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
			RemoteIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
			RemoteNodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Remote Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			Sid (obj(ixnetwork_restpy.multivalue.Multivalue)): SID is the Segment Identifier
			SidType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Segment Identifier Type control user can configure whether to include SID or not and if included what is its type. Types are as follows: Null SID 20bit MPLS Label 32bit MPLS Label. If it is Null then S bit is set in the packet. Default value is 20bit MPLS Label.
			Tc (obj(ixnetwork_restpy.multivalue.Multivalue)): This field is used to carry traffic class information. This control will be editable only if SID Type is MPLS Label 32bit.
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): This field is used to encode a time-to-live value. This control will be editable only if SID Type is MPLS Label 32bit.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrerosubobjectlist.PceUpdateSrEroSubObjectList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrerosubobjectlist import PceUpdateSrEroSubObjectList
		return self._select(PceUpdateSrEroSubObjectList(self), locals())

	def PceUpdateSrMetricSubObjectList(self, ActiveThisMetric=None, BFlag=None, MetricType=None, MetricValue=None):
		"""Gets child instances of PceUpdateSrMetricSubObjectList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceUpdateSrMetricSubObjectList will be returned.

		Args:
			ActiveThisMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies whether the corresponding metric object is active or not.
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): B (bound) flag MUST be set in the METRIC object, which specifies that the SID depth for the computed path MUST NOT exceed the metric-value.
			MetricType (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a drop down which has 4 choices: IGP/ TE/ Hop count/ MSD.
			MetricValue (obj(ixnetwork_restpy.multivalue.Multivalue)): User can specify the metric value corresponding to the metric type selected.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrmetricsubobjectlist.PceUpdateSrMetricSubObjectList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatesrmetricsubobjectlist import PceUpdateSrMetricSubObjectList
		return self._select(PceUpdateSrMetricSubObjectList(self), locals())

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
