from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PcReplyLspParameters(Base):
	"""PCReply LSP Parameters
	"""

	_SDM_NAME = 'pcReplyLspParameters'

	def __init__(self, parent):
		super(PcReplyLspParameters, self).__init__(parent)

	def PceXroSubObjectsList(self, Active=None, AsNumber=None, Attribute=None, Count=None, DescriptiveName=None, Exclude_bit=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, Name=None, PceId128=None, PceId32=None, PrefixLength=None, RouterId=None, SrlgId=None, SubObjectType=None):
		"""Gets child instances of PceXroSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceXroSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls whether the XRO sub-object will be sent in the PCRequest message.
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS Number
			Attribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates how the exclusion subobject is to be indicated
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Exclude_bit (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether the exclusion is mandatory or desired.
			InterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface ID
			Ipv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Address
			Ipv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Address
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PceId128 (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 bit PKS ID
			PceId32 (obj(ixnetwork_restpy.multivalue.Multivalue)): 32 bit PKS ID
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Router ID
			SrlgId (obj(ixnetwork_restpy.multivalue.Multivalue)): SRLG ID
			SubObjectType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: IPv4 Prefix IPv6 Prefix Unnumbered Interface ID AS Number. SRLG

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist.PceXroSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcexrosubobjectslist import PceXroSubObjectsList
		return self._select(PceXroSubObjectsList(self), locals())

	def PcepEroSubObjectsList(self, Active=None, AsNumber=None, Bos=None, Count=None, DescriptiveName=None, FBit=None, Ipv4NodeId=None, Ipv4Prefix=None, Ipv6NodeId=None, Ipv6Prefix=None, LocalInterfaceId=None, LocalIpv4Address=None, LocalIpv6Address=None, LocalNodeId=None, LooseHop=None, MplsLabel=None, NaiType=None, Name=None, PrefixLength=None, RemoteInterfaceId=None, RemoteIpv4Address=None, RemoteIpv6Address=None, RemoteNodeId=None, Sid=None, SidType=None, SubObjectType=None, Tc=None, Ttl=None):
		"""Gets child instances of PcepEroSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PcepEroSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls whether the ERO sub-object will be sent in the PCInitiate message.
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS Number
			Bos (obj(ixnetwork_restpy.multivalue.Multivalue)): This bit is set to true for the last entry in the label stack i.e., for the bottom of the stack, and false for all other label stack entries. This control will be editable only if SID Type is MPLS Label 32bit.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			FBit (obj(ixnetwork_restpy.multivalue.Multivalue)): A Flag which is used to carry additional information pertaining to SID. When this bit is set, the NAI value in the subobject body is null.
			Ipv4NodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Node ID is specified as an IPv4 address. This control can be configured if NAI Type is set to IPv4 Node ID and F bit is disabled.
			Ipv4Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Prefix is specified as an IPv4 address.
			Ipv6NodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Node ID is specified as an IPv6 address. This control can be configured if NAI Type is set to IPv6 Node ID and F bit is disabled.
			Ipv6Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Prefix is specified as an IPv6 address.
			LocalInterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Local Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			LocalIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
			LocalIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
			LocalNodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Local Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			LooseHop (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates if user wants to represent a loose-hop sub object in the LSP
			MplsLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): This control will be editable if the SID Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
			NaiType (obj(ixnetwork_restpy.multivalue.Multivalue)): NAI (Node or Adjacency Identifier) contains the NAI associated with the SID. Depending on the value of SID Type, the NAI can have different formats such as, Not Applicable IPv4 Node ID IPv6 Node ID IPv4 Adjacency IPv6 Adjacency Unnumbered Adjacency with IPv4 NodeIDs
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RemoteInterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Remote Interface ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			RemoteIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv4 Adjacency and F bit is disabled.
			RemoteIpv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): This Control can be configured if NAI Type is set to IPv6 Adjacency and F bit is disabled.
			RemoteNodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the Remote Node ID of the Unnumbered Adjacency with IPv4 NodeIDs which is specified as a pair of Node ID / Interface ID tuples. This Control can be configured if NAI Type is set to Unnumbered Adjacency with IPv4 NodeIDs and F bit is disabled.
			Sid (obj(ixnetwork_restpy.multivalue.Multivalue)): SID is the Segment Identifier
			SidType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Segment Identifier Type control user can configure whether to include SID or not and if included what is its type. Types are as follows: Null SID 20bit MPLS Label 32bit MPLS Label. If it is Null then S bit is set in the packet. Default value is 20bit MPLS Label.
			SubObjectType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: Not Applicable IPv4 Prefix IPv6 Prefix AS Number.
			Tc (obj(ixnetwork_restpy.multivalue.Multivalue)): This field is used to carry traffic class information. This control will be editable only if SID Type is MPLS Label 32bit.
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): This field is used to encode a time-to-live value. This control will be editable only if SID Type is MPLS Label 32bit.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist.PcepEroSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist import PcepEroSubObjectsList
		return self._select(PcepEroSubObjectsList(self), locals())

	def PcepMetricSubObjectsList(self, Active=None, BFlag=None, Count=None, DescriptiveName=None, MetricType=None, MetricValue=None, Name=None):
		"""Gets child instances of PcepMetricSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PcepMetricSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies whether the corresponding metric object is active or not.
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): B (bound) flag MUST be set in the METRIC object, which specifies that the SID depth for the computed path MUST NOT exceed the metric-value.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			MetricType (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a drop down which has 4 choices: IGP/ TE/ Hop count/ MSD.
			MetricValue (obj(ixnetwork_restpy.multivalue.Multivalue)): User can specify the metric value corresponding to the metric type selected.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist.PcepMetricSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist import PcepMetricSubObjectsList
		return self._select(PcepMetricSubObjectsList(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Bandwidth(self):
		"""Bandwidth (bits/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def BiDirectional(self):
		"""Bi-directional

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('biDirectional')

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
	def EnableCFlag(self):
		"""C Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCFlag')

	@property
	def EnableEro(self):
		"""Include ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableEro')

	@property
	def EnableLoose(self):
		"""Loose

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLoose')

	@property
	def EnableXro(self):
		"""Include XRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableXro')

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def FailBit(self):
		"""Fail Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('failBit')

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
	def IncludeBandwidth(self):
		"""Include Bandwidth

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeBandwidth')

	@property
	def IncludeLsp(self):
		"""Include LSP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLsp')

	@property
	def IncludeLspa(self):
		"""Include LSPA

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLspa')

	@property
	def IncludeMetric(self):
		"""Include Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeMetric')

	@property
	def IncludeRp(self):
		"""Include RP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeRp')

	@property
	def IncludeSymbolicPathNameTlv(self):
		"""Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathNameTlv')

	@property
	def LocalProtection(self):
		"""Local Protection

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtection')

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
	def NatureOfIssue(self):
		"""Nature Of Issue

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('natureOfIssue')

	@property
	def NumberOfEroSubObjects(self):
		"""Number of ERO Sub Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfEroSubObjects')
	@NumberOfEroSubObjects.setter
	def NumberOfEroSubObjects(self, value):
		self._set_attribute('numberOfEroSubObjects', value)

	@property
	def NumberOfMetricSubObject(self):
		"""Number of Metric

		Returns:
			number
		"""
		return self._get_attribute('numberOfMetricSubObject')
	@NumberOfMetricSubObject.setter
	def NumberOfMetricSubObject(self, value):
		self._set_attribute('numberOfMetricSubObject', value)

	@property
	def NumberOfXroSubObjects(self):
		"""Number of XRO Sub Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfXroSubObjects')
	@NumberOfXroSubObjects.setter
	def NumberOfXroSubObjects(self, value):
		self._set_attribute('numberOfXroSubObjects', value)

	@property
	def PlspId(self):
		"""An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('plspId')

	@property
	def PriorityValue(self):
		"""Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('priorityValue')

	@property
	def ProcessType(self):
		"""Indicates how the XRO is responded in the Path Request Response.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('processType')

	@property
	def ReceivedPLSPID(self):
		"""Received PLSP-ID in PcRequest

		Returns:
			list(number)
		"""
		return self._get_attribute('receivedPLSPID')

	@property
	def ReceivedSymbolicPath(self):
		"""Received Symbolic Path Name in PcRequest

		Returns:
			list(str)
		"""
		return self._get_attribute('receivedSymbolicPath')

	@property
	def ReflectLSP(self):
		"""Reflect LSP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reflectLSP')

	@property
	def ReflectRP(self):
		"""Reflect RP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reflectRP')

	@property
	def ReflectedObjectNoPath(self):
		"""Reflected Object

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reflectedObjectNoPath')

	@property
	def RequestId(self):
		"""Request ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('requestId')

	@property
	def ResponseOptions(self):
		"""Reply Options

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('responseOptions')

	@property
	def ResponsePathType(self):
		"""Indicates which type of LSP will be responsed in the Path Request Response.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('responsePathType')

	@property
	def SessionInfo(self):
		"""Logs additional information about the LSP state

		Returns:
			list(str[delegatedActive|delegatedDown|delegatedGoingUp|delegatedUp|noLSPObjectInPCRequest|none|notDelegatedActive|notDelegatedDown|notDelegatedGoingUp|notDelegatedUp|pcErrorReceived|removedByPCC|replySentReportNotReceived])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SymbolicPathName(self):
		"""Each LSP (path) must have a symbolic name that is unique in the PCC. It must remain constant throughout a path's lifetime, which may span across multiple consecutive PCEP sessions and/or PCC restarts.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('symbolicPathName')

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

	def ReturnDelegation(self, Arg1):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Replied LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pcReplyLspParameters object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('returnDelegation', payload=locals(), response_object=None)

	def ReturnDelegation(self, Arg1, SessionIndices):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Replied LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pcReplyLspParameters object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('returnDelegation', payload=locals(), response_object=None)

	def ReturnDelegation(self, Arg1, SessionIndices):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Replied LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pcReplyLspParameters object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('returnDelegation', payload=locals(), response_object=None)

	def ReturnDelegation(self, Arg2):
		"""Executes the returnDelegation operation on the server.

		Return Delegation helps PCE to return a delegation of LSP/LSPs.

		Args:
			Arg2 (list(number)): Return Delegation.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('returnDelegation', payload=locals(), response_object=None)
