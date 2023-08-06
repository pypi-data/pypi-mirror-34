from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PceInitiateLSPParameters(Base):
	"""This tab configures the Initiated LSP Parameters.
	"""

	_SDM_NAME = 'pceInitiateLSPParameters'

	def __init__(self, parent):
		super(PceInitiateLSPParameters, self).__init__(parent)

	def PceInitiateXROobject(self, Active=None, AsNumber=None, Attribute=None, Count=None, DescriptiveName=None, Exclude_bit=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, Name=None, PceId128=None, PceId32=None, PrefixLength=None, RouterId=None, SrlgId=None, SubObjectType=None):
		"""Gets child instances of PceInitiateXROobject from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PceInitiateXROobject will be returned.

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
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject.PceInitiateXROobject))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject import PceInitiateXROobject
		return self._select(PceInitiateXROobject(self), locals())

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
	def AssociationId(self):
		"""The Association ID of this LSP.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('associationId')

	@property
	def Bandwidth(self):
		"""Bandwidth (bits/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

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
	def DestEndPointIpv4(self):
		"""Dest IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv6.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destEndPointIpv4')

	@property
	def DestEndPointIpv6(self):
		"""Dest IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv4.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destEndPointIpv6')

	@property
	def EnableXro(self):
		"""Include XRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableXro')

	@property
	def ExcludeAny(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link only if the link carries all of the attributes in the set.

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
		"""The priority of the LSP with respect to holding resources. The value 0 is the highest priority. Holding Priority is used in deciding whether this session can be preempted by another session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def IncludeAll(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control excludes a link from consideration if the link carries any of the attributes in the set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link if the link carries any of the attributes in the set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeAssociation(self):
		"""Indicates whether PPAG will be included in a PCInitiate message. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAssociation')

	@property
	def IncludeBandwidth(self):
		"""Indicates whether Bandwidth will be included in a PCInitiate message. All other attributes in sub-tab-Bandwidth would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeBandwidth')

	@property
	def IncludeEndPoints(self):
		"""Indicates whether END-POINTS object will be included in a PCInitiate message. All other attributes in sub-tab-End Points would be editable only if this checkbox is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeEndPoints')

	@property
	def IncludeEro(self):
		"""Specifies whether ERO is active or inactive. All subsequent attributes of the sub-tab-ERO would be editable only if this is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeEro')

	@property
	def IncludeLsp(self):
		"""Indicates whether LSP will be included in a PCInitiate message. All other attributes in sub-tab-LSP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLsp')

	@property
	def IncludeLspa(self):
		"""Indicates whether LSPA will be included in a PCInitiate message. All other attributes in sub-tab-LSPA would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLspa')

	@property
	def IncludeMetric(self):
		"""Indicates whether the PCInitiate message will have the metric list that is configured. All subsequent attributes of the sub-tab-Metric would be editable only if this is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeMetric')

	@property
	def IncludeSrp(self):
		"""Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSrp')

	@property
	def IncludeSymbolicPathNameTlv(self):
		"""Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathNameTlv')

	@property
	def IpVersion(self):
		"""Drop down to select the IP Version with 2 choices : IPv4 / IPv6

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipVersion')

	@property
	def LocalProtection(self):
		"""When set, this means that the path must include links protected with Fast Reroute

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
	def NumberOfMetricSubObject(self):
		"""Value that indicates the number of Metric Objects to be configured.

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
	def OverridePlspId(self):
		"""Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.

		Returns:
			bool
		"""
		return self._get_attribute('overridePlspId')
	@OverridePlspId.setter
	def OverridePlspId(self, value):
		self._set_attribute('overridePlspId', value)

	@property
	def OverrideSrpIdNumber(self):
		"""Indicates whether SRP ID Number is overridable.

		Returns:
			bool
		"""
		return self._get_attribute('overrideSrpIdNumber')
	@OverrideSrpIdNumber.setter
	def OverrideSrpIdNumber(self, value):
		self._set_attribute('overrideSrpIdNumber', value)

	@property
	def PathSetupType(self):
		"""Indicates which type of LSP will be requested in the PCInitiated Request.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pathSetupType')

	@property
	def PlspId(self):
		"""An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('plspId')

	@property
	def ProtectionLsp(self):
		"""Indicates whether Protection LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('protectionLsp')

	@property
	def SessionInfo(self):
		"""Logs additional information about the LSP state

		Returns:
			list(str[advertised|delegatedActive|delegatedDown|delegatedGoingUp|delegatedUp|init|none|notDelegatedActive|notDelegatedDown|notDelegatedGoingUp|notDelegatedUp|pcErrorReceived|removedByPCC|removedByPCE|returnDelegation])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SetupPriority(self):
		"""The priority of the LSP with respect to taking resources.The value 0 is the highest priority.The Setup Priority is used in deciding whether this session can preempt another session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SrcEndPointIpv4(self):
		"""Source IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is set to IPv6.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srcEndPointIpv4')

	@property
	def SrcEndPointIpv6(self):
		"""Source IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP version is set to IPv4.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srcEndPointIpv6')

	@property
	def SrpIdNumber(self):
		"""The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srpIdNumber')

	@property
	def StandbyMode(self):
		"""Indicates whether Standby LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('standbyMode')

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

		Return Delegation of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('returnDelegation', payload=locals(), response_object=None)

	def ReturnDelegation(self, Arg1, SessionIndices):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('returnDelegation', payload=locals(), response_object=None)

	def ReturnDelegation(self, Arg1, SessionIndices):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references
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

	def TakeControl(self, Arg1):
		"""Executes the takeControl operation on the server.

		Take Control of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('takeControl', payload=locals(), response_object=None)

	def TakeControl(self, Arg1, SessionIndices):
		"""Executes the takeControl operation on the server.

		Take Control of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('takeControl', payload=locals(), response_object=None)

	def TakeControl(self, Arg1, SessionIndices):
		"""Executes the takeControl operation on the server.

		Take Control of PCE-Initiated LSPs

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pceInitiateLSPParameters object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('takeControl', payload=locals(), response_object=None)

	def TakeControl(self, Arg2):
		"""Executes the takeControl operation on the server.

		Take Control helps PCE to take control of Orphan LSP/LSPs.

		Args:
			Arg2 (list(number)): Take Control.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('takeControl', payload=locals(), response_object=None)
