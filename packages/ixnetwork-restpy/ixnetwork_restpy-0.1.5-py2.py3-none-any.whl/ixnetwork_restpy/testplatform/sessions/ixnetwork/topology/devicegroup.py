from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DeviceGroup(Base):
	"""Describes a set of network devices with similar configuration and the same multiplicity for devices behind.
	"""

	_SDM_NAME = 'deviceGroup'

	def __init__(self, parent):
		super(DeviceGroup, self).__init__(parent)

	def BfdRouter(self, Active=None, Count=None, DescriptiveName=None, Name=None, Status=None):
		"""Gets child instances of BfdRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BfdRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter.BfdRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter import BfdRouter
		return self._select(BfdRouter(self), locals())

	def add_BfdRouter(self, Name=None):
		"""Adds a child instance of BfdRouter on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter.BfdRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter import BfdRouter
		return self._create(BfdRouter(self), locals())

	def BridgeData(self, Count=None, DescriptiveName=None, Name=None, SystemId=None):
		"""Gets child instances of BridgeData from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BridgeData will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): 6 Byte System Id in Hex format.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata.BridgeData))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata import BridgeData
		return self._select(BridgeData(self), locals())

	def CfmMp(self, Active=None, AutoLbIteration=None, AutoLbTimeoutInSec=None, AutoLbTimerInSec=None, AutoLtIteration=None, AutoLtTimeoutInSec=None, AutoLtTimerInSec=None, CVlanId=None, CVlanPriority=None, CcmPriority=None, ChassisId=None, ChassisIdLength=None, ChassisIdSubType=None, Count=None, DataTlvLength=None, DataTlvValue=None, DescriptiveName=None, EnableAutoLb=None, EnableAutoLt=None, EnableDataTlv=None, EnableInterfaceStatusTlv=None, EnableOrganizationSpecificTlv=None, EnablePortStatusTlv=None, EnableSenderIdTlv=None, EnableVlan=None, IncludeTLVinCCM=None, IncludeTLVinLBM=None, IncludeTLVinLBR=None, IncludeTLVinLTM=None, IncludeTLVinLTR=None, LbAllRemoteMeps=None, LbDestinationMacAddress=None, LbmPriority=None, LtAllRemoteMeps=None, LtDestinationMacAddress=None, LtmPriority=None, MacAddress=None, ManagementAddress=None, ManagementAddressDomain=None, ManagementAddressDomainLength=None, ManagementAddressLength=None, MdMegLevel=None, MdMegLevelIndex=None, MdNameFormat=None, MepId=None, MipId=None, Multiplier=None, Name=None, OrganizationSpecificTlvLength=None, OverrideVlanPriority=None, Rdi=None, SVlanId=None, SVlanPriority=None, SVlanTpid=None, ShortMaName=None, ShortMaNameFormat=None, Status=None, Type=None, VlanStacking=None):
		"""Gets child instances of CfmMp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of CfmMp will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AutoLbIteration (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LB Iteration
			AutoLbTimeoutInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LB Timeout (sec)
			AutoLbTimerInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LB Timer (sec)
			AutoLtIteration (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LT Iteration
			AutoLtTimeoutInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LT Timeout (sec)
			AutoLtTimerInSec (obj(ixnetwork_restpy.multivalue.Multivalue)): Auto LT Timer (sec)
			CVlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): C-VLAN ID
			CVlanPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): C-VLAN Priority
			CcmPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): CCM Priority
			ChassisId (obj(ixnetwork_restpy.multivalue.Multivalue)): Chassis ID
			ChassisIdLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Chassis ID Length
			ChassisIdSubType (obj(ixnetwork_restpy.multivalue.Multivalue)): Chassis ID SubType
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DataTlvLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Data TLV Length
			DataTlvValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Data TLV Value
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAutoLb (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Auto LB
			EnableAutoLt (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Auto LT
			EnableDataTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Data TLV
			EnableInterfaceStatusTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Interface Status TLV
			EnableOrganizationSpecificTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Organization Specific TLV
			EnablePortStatusTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Port Status TLV
			EnableSenderIdTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Sender ID TLV
			EnableVlan (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable VLAN
			IncludeTLVinCCM (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Custom TLV in CCM
			IncludeTLVinLBM (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Custom TLV in LBM
			IncludeTLVinLBR (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Custom TLV in LBR
			IncludeTLVinLTM (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Custom TLV in LTM
			IncludeTLVinLTR (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Custom TLV in LTR
			LbAllRemoteMeps (obj(ixnetwork_restpy.multivalue.Multivalue)): LB All Remote MEPS
			LbDestinationMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): LB Destination MAC Address
			LbmPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): LBM Priority
			LtAllRemoteMeps (obj(ixnetwork_restpy.multivalue.Multivalue)): LT All Remote MEPS
			LtDestinationMacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): LT Destination MAC Address
			LtmPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): LTM Priority
			MacAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC Address
			ManagementAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Management Address
			ManagementAddressDomain (obj(ixnetwork_restpy.multivalue.Multivalue)): Management Address Domain
			ManagementAddressDomainLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Management Address Domain Length
			ManagementAddressLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Management Address Length
			MdMegLevel (obj(ixnetwork_restpy.multivalue.Multivalue)): MD/MEG Level
			MdMegLevelIndex (obj(ixnetwork_restpy.multivalue.Multivalue)): MD/MEG Level Index
			MdNameFormat (obj(ixnetwork_restpy.multivalue.Multivalue)): CCI Interval
			MepId (obj(ixnetwork_restpy.multivalue.Multivalue)): MEP ID
			MipId (obj(ixnetwork_restpy.multivalue.Multivalue)): MIP ID
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OrganizationSpecificTlvLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Organization Specific TLV Length
			OverrideVlanPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Override V-LAN Priority
			Rdi (obj(ixnetwork_restpy.multivalue.Multivalue)): RDI (Auto Update)
			SVlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): S-VLAN ID
			SVlanPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): S-VLAN Priority
			SVlanTpid (obj(ixnetwork_restpy.multivalue.Multivalue)): S-VLAN TPID
			ShortMaName (obj(ixnetwork_restpy.multivalue.Multivalue)): Short MA Name
			ShortMaNameFormat (obj(ixnetwork_restpy.multivalue.Multivalue)): Short MA Name Format
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type
			VlanStacking (obj(ixnetwork_restpy.multivalue.Multivalue)): VLAN Stacking

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmmp.CfmMp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmmp import CfmMp
		return self._select(CfmMp(self), locals())

	def add_CfmMp(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of CfmMp on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmmp.CfmMp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cfmmp import CfmMp
		return self._create(CfmMp(self), locals())

	def DeviceGroup(self, Count=None, DescriptiveName=None, Enabled=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of DeviceGroup from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DeviceGroup will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enabled (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables/disables device.
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup.DeviceGroup))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup import DeviceGroup
		return self._select(DeviceGroup(self), locals())

	def add_DeviceGroup(self, Multiplier="10", Name=None):
		"""Adds a child instance of DeviceGroup on the server.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup.DeviceGroup)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup import DeviceGroup
		return self._create(DeviceGroup(self), locals())

	def Ethernet(self, Count=None, DescriptiveName=None, EnableVlans=None, Mac=None, Mtu=None, Multiplier=None, Name=None, NotifyMACMove=None, Status=None, UseVlans=None, VlanCount=None):
		"""Gets child instances of Ethernet from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ethernet will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableVlans (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables VLANs for the sessions.
			Mac (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC addresses of the devices
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum transmission unit
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NotifyMACMove (bool): Flag to determine if MAC move notification to be sent
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
		return self._select(Ethernet(self), locals())

	def add_Ethernet(self, ConnectedVia=None, Multiplier="1", Name=None, NotifyMACMove="False", StackedLayers=None, UseVlans="False", VlanCount="1"):
		"""Adds a child instance of Ethernet on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NotifyMACMove (bool): Flag to determine if MAC move notification to be sent
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			UseVlans (bool): Flag to determine whether VLANs are enabled
			VlanCount (number): Number of active VLANs

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
		return self._create(Ethernet(self), locals())

	def Ipv4Loopback(self, Address=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Prefix=None, Status=None):
		"""Gets child instances of Ipv4Loopback from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv4Loopback will be returned.

		Args:
			Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 addresses of the devices
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback.Ipv4Loopback))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback import Ipv4Loopback
		return self._select(Ipv4Loopback(self), locals())

	def add_Ipv4Loopback(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ipv4Loopback on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback.Ipv4Loopback)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback import Ipv4Loopback
		return self._create(Ipv4Loopback(self), locals())

	def Ipv6Loopback(self, Address=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, Prefix=None, Status=None):
		"""Gets child instances of Ipv6Loopback from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv6Loopback will be returned.

		Args:
			Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 addresses of the devices
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback.Ipv6Loopback))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback import Ipv6Loopback
		return self._select(Ipv6Loopback(self), locals())

	def add_Ipv6Loopback(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ipv6Loopback on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback.Ipv6Loopback)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback import Ipv6Loopback
		return self._create(Ipv6Loopback(self), locals())

	def IsisFabricPathRouter(self, Active=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, CSNPInterval=None, CapabilityRouterId=None, Count=None, DceMCastIpv4GroupCount=None, DceMCastIpv6GroupCount=None, DceMCastMacGroupCount=None, DceTopologyCount=None, DescriptiveName=None, DiscardLSPs=None, EnableHelloPadding=None, EnableHostName=None, EnableWideMetric=None, HostName=None, IgnoreReceiveMD5=None, InterLSPsOrMGroupPDUBurstGap=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, MaxAreaAddresses=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, Name=None, Overloaded=None, PSNPInterval=None, PartitionRepair=None, Status=None):
		"""Gets child instances of IsisFabricPathRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisFabricPathRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Addresses
			AreaAuthenticationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Authentication Type
			AreaTransmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Transmit Password / MD5-Key
			Attached (obj(ixnetwork_restpy.multivalue.Multivalue)): Attached
			CSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): CSNP Interval (ms)
			CapabilityRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Capability Router Id
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DceMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			DceMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			DceMCastMacGroupCount (number): MAC Group Count(multiplier)
			DceTopologyCount (number): Topology Count(multiplier)
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLSPs (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard LSPs
			EnableHelloPadding (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Padding
			EnableHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Host Name
			EnableWideMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Wide Metric
			HostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Host Name
			IgnoreReceiveMD5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore Receive MD5
			InterLSPsOrMGroupPDUBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
			LSPLifetime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Rifetime (sec)
			LSPRefreshRate (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Refresh Rate (sec)
			LSPorMGroupPDUMinTransmissionInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP/MGROUP-PDU Min Transmission Interval (ms)
			MaxAreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Area Addresses
			MaxLSPSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSP Size
			MaxLSPsOrMGroupPDUsPerBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSPs/MGROUP-PDUs Per Burst
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overloaded (obj(ixnetwork_restpy.multivalue.Multivalue)): Overloaded
			PSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): PSNP Interval (ms)
			PartitionRepair (obj(ixnetwork_restpy.multivalue.Multivalue)): Partition Repair
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter.IsisFabricPathRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter import IsisFabricPathRouter
		return self._select(IsisFabricPathRouter(self), locals())

	def IsisL3Router(self, BIERNodePrefix=None, Active=None, AdvertiseSRLB=None, AdvertiseSRMSPreference=None, AdvertiseSidAsLocator=None, Algorithm=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, BIERIPv6NodePrefix=None, BierNFlag=None, BierRFlag=None, CSNPInterval=None, ConfigureSIDIndexLabel=None, Count=None, DBit=None, DBitForSRv6Cap=None, DBitInsideSRv6SidTLV=None, DescriptiveName=None, DiscardLSPs=None, Distribution=None, DomainAuthenticationType=None, DomainTransmitPasswordOrMD5Key=None, EFlag=None, EFlagOfSRv6CapTlv=None, EnableBIER=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableMTIPv6=None, EnableMappingServer=None, EnableSR=None, EnableTE=None, EnableWMforTE=None, EnableWideMetric=None, Funcflags=None, Function=None, HitlessRestartMode=None, HitlessRestartTime=None, HitlessRestartVersion=None, HostName=None, IgnoreReceiveMD5=None, IncludeMaximumEndDSrhTLV=None, IncludeMaximumEndPopSrhTLV=None, IncludeMaximumSLTLV=None, IncludeMaximumTEncapSrhTLV=None, IncludeMaximumTInsertSrhTLV=None, IncludePrefixAttrFlags=None, InterLSPsOrMGroupPDUBurstGap=None, Ipv4Flag=None, Ipv6Flag=None, Ipv6NodePrefix=None, Ipv6Srh=None, LFlag=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, LocatorPrefixLength=None, Mask=None, MaxAreaAddresses=None, MaxEndD=None, MaxEndPopSrh=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, MaxSL=None, MaxTEncap=None, MaxTInsert=None, NFlag=None, Name=None, NoOfBIERSubDomains=None, NoOfSRTunnels=None, NodePrefix=None, NumberOfMappingIPV4Ranges=None, NumberOfMappingIPV6Ranges=None, OFlagOfSRv6CapTlv=None, Overloaded=None, PFlag=None, PSNPInterval=None, PartitionRepair=None, PrefixAdvertisementType=None, PrefixLength=None, RFlag=None, Redistribution=None, RedistributionForSRv6=None, ReservedInsideFlagsOfSRv6SidTLV=None, ReservedInsideSRv6CapFlag=None, RouteMetric=None, RouteOrigin=None, RtrcapId=None, RtrcapIdForSrv6=None, SBit=None, SBitForSRv6Cap=None, SIDIndexLabel=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None, SrlbFlags=None, SrmsPreference=None, Status=None, TERouterId=None, VFlag=None):
		"""Gets child instances of IsisL3Router from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3Router will be returned.

		Args:
			BIERNodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Prefix
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseSRLB (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables advertisement of Segment Routing Local Block (SRLB) Sub-Tlv in Router Capability Tlv
			AdvertiseSRMSPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise SRMS Preference sub-TLV in Router capability TLV
			AdvertiseSidAsLocator (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, then the configured IPv6 Node SID gets advertised as a reachable IPv6 prefix
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm
			AreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Addresses
			AreaAuthenticationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Authentication Type
			AreaTransmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Transmit Password / MD5-Key
			Attached (obj(ixnetwork_restpy.multivalue.Multivalue)): Attached
			BIERIPv6NodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Node Prefix
			BierNFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Nodal prefix flag
			BierRFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution flag
			CSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): CSNP Interval (ms)
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DBit (obj(ixnetwork_restpy.multivalue.Multivalue)): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
			DBitForSRv6Cap (obj(ixnetwork_restpy.multivalue.Multivalue)): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
			DBitInsideSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLSPs (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard LSPs
			Distribution (obj(ixnetwork_restpy.multivalue.Multivalue)): Distribution
			DomainAuthenticationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Domain Authentication Type
			DomainTransmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Domain Transmit Password / MD5-Key
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit NULL flag
			EFlagOfSRv6CapTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then router is able to apply T.Encap operation
			EnableBIER (bool): Enable BIER
			EnableHelloPadding (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Padding
			EnableHitlessRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hitless Restart
			EnableHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Host Name
			EnableMTIPv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MT for IPv6
			EnableMappingServer (obj(ixnetwork_restpy.multivalue.Multivalue)): This ensures whether the ISIS router will behave as a Segment Routing Mapping Server (SRMS) or not.
			EnableSR (bool): Enable Segment Routing
			EnableTE (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable TE
			EnableWMforTE (obj(ixnetwork_restpy.multivalue.Multivalue)): Hidden field is to disable wide Metric, when user disable TE Router conditionally
			EnableWideMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Wide Metric
			Funcflags (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the function flags
			Function (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies endpoint function codes
			HitlessRestartMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Mode
			HitlessRestartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Time
			HitlessRestartVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Version
			HostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Host Name
			IgnoreReceiveMD5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore Receive MD5
			IncludeMaximumEndDSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum End D SRH TLV in SRv6 capability
			IncludeMaximumEndPopSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Max-End-Pop-SRH TLV in SRv6 capability
			IncludeMaximumSLTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum SL TLV in SRv6 capability
			IncludeMaximumTEncapSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum T.Encap SRH TLV in SRv6 capability
			IncludeMaximumTInsertSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum T.Insert SRH TLV in SRv6 capability
			IncludePrefixAttrFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Prefix Attributes Flags
			InterLSPsOrMGroupPDUBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
			Ipv4Flag (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then the router is capable of processing SR MPLS encapsulated IPv4 packets on all interfaces.
			Ipv6Flag (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then the router is capable of processing SR MPLS encapsulated IPv6 packets on all interfaces.
			Ipv6NodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Node SID
			Ipv6Srh (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the SR-IPv6 flag. If set to true, then this enables the SRv6 capability on the router If set to false, then this enables the MPLS SR capability on the router
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Flag
			LSPLifetime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Rifetime (sec)
			LSPRefreshRate (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Refresh Rate (sec)
			LSPorMGroupPDUMinTransmissionInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP/MGROUP-PDU Min Transmission Interval (ms)
			LocatorPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Locator Prefix Length
			Mask (obj(ixnetwork_restpy.multivalue.Multivalue)): Mask
			MaxAreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Area Addresses
			MaxEndD (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions if the extension header right underneath the outer IPv6 header is an SRH.
			MaxEndPopSrh (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs in the top SRH in an SRH stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
			MaxLSPSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSP Size
			MaxLSPsOrMGroupPDUsPerBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSPs/MGROUP-PDUs Per Burst
			MaxSL (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum value of the Segments Left (SL) field in the SRH of a received packet before applying the function associated with a SID.
			MaxTEncap (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
			MaxTInsert (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
			NFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Nodal prefix flag
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfBIERSubDomains (number): Number of BIER Sub Domains
			NoOfSRTunnels (number): Number of MPLS SR Tunnels
			NodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Prefix
			NumberOfMappingIPV4Ranges (number): Specifies the number of IPv4 mappings or range TLVs that each router in a DG can advertise.
			NumberOfMappingIPV6Ranges (number): Specifies the number of IPv6 mappings or range TLVs that each router in a DG can advertise.
			OFlagOfSRv6CapTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, it indicates that this packet is an operations and management (OAM) packet.
			Overloaded (obj(ixnetwork_restpy.multivalue.Multivalue)): Overloaded
			PFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
			PSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): PSNP Interval (ms)
			PartitionRepair (obj(ixnetwork_restpy.multivalue.Multivalue)): Partition Repair
			PrefixAdvertisementType (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Advertisement Type
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution flag
			Redistribution (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution
			RedistributionForSRv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution
			ReservedInsideFlagsOfSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the reserved field (part of flags field of SRv6 SID TLV)
			ReservedInsideSRv6CapFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the reserved field (as part of Flags field of SRv6 Capability TLV)
			RouteMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Metric
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			RtrcapId (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Capability Id
			RtrcapIdForSrv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Capability Id
			SBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
			SBitForSRv6Cap (obj(ixnetwork_restpy.multivalue.Multivalue)): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
			SIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SRAlgorithmCount (number): SR Algorithm Count
			SRGBRangeCount (number): SRGB Range Count
			SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}
			SrlbFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies the value of the SRLB flags field
			SrmsPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): This is used to associate a preference with SRMS advertisements and is being advertised as a sub-TLV in Router Capability TLV
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TERouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): TE Router ID
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router.IsisL3Router))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router import IsisL3Router
		return self._select(IsisL3Router(self), locals())

	def IsisSpbRouter(self, Active=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, CSNPInterval=None, Count=None, DescriptiveName=None, DiscardLSPs=None, EnableHelloPadding=None, EnableHitlessRestart=None, EnableHostName=None, EnableWideMetric=None, HitlessRestartMode=None, HitlessRestartTime=None, HitlessRestartVersion=None, HostName=None, IgnoreMTPortCapability=None, IgnoreReceiveMD5=None, InterLSPsOrMGroupPDUBurstGap=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, MaxAreaAddresses=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, Name=None, Overloaded=None, PSNPInterval=None, PartitionRepair=None, SpbTopologyCount=None, Status=None):
		"""Gets child instances of IsisSpbRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Addresses
			AreaAuthenticationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Authentication Type
			AreaTransmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Transmit Password / MD5-Key
			Attached (obj(ixnetwork_restpy.multivalue.Multivalue)): Attached
			CSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): CSNP Interval (ms)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLSPs (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard LSPs
			EnableHelloPadding (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Padding
			EnableHitlessRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hitless Restart
			EnableHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Host Name
			EnableWideMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Wide Metric
			HitlessRestartMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Mode
			HitlessRestartTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Time
			HitlessRestartVersion (obj(ixnetwork_restpy.multivalue.Multivalue)): Restart Version
			HostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Host Name
			IgnoreMTPortCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore MT Port Capability
			IgnoreReceiveMD5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore Receive MD5
			InterLSPsOrMGroupPDUBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
			LSPLifetime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Rifetime (sec)
			LSPRefreshRate (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Refresh Rate (sec)
			LSPorMGroupPDUMinTransmissionInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP/MGROUP-PDU Min Transmission Interval (ms)
			MaxAreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Area Addresses
			MaxLSPSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSP Size
			MaxLSPsOrMGroupPDUsPerBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSPs/MGROUP-PDUs Per Burst
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overloaded (obj(ixnetwork_restpy.multivalue.Multivalue)): Overloaded
			PSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): PSNP Interval (ms)
			PartitionRepair (obj(ixnetwork_restpy.multivalue.Multivalue)): Partition Repair
			SpbTopologyCount (number): Topology Count(multiplier)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter.IsisSpbRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter import IsisSpbRouter
		return self._select(IsisSpbRouter(self), locals())

	def add_IsisSpbRouter(self, Name=None, SpbTopologyCount="1"):
		"""Adds a child instance of IsisSpbRouter on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SpbTopologyCount (number): Topology Count(multiplier)

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter.IsisSpbRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter import IsisSpbRouter
		return self._create(IsisSpbRouter(self), locals())

	def IsisTrillRouter(self, Active=None, AreaAddresses=None, AreaAuthenticationType=None, AreaTransmitPasswordOrMD5Key=None, Attached=None, CSNPInterval=None, CapabilityRouterId=None, Count=None, DescriptiveName=None, DiscardLSPs=None, EnableHelloPadding=None, EnableHostName=None, EnableMtuProbe=None, EnableWideMetric=None, HostName=None, IgnoreReceiveMD5=None, InterLSPsOrMGroupPDUBurstGap=None, LSPLifetime=None, LSPRefreshRate=None, LSPorMGroupPDUMinTransmissionInterval=None, MaxAreaAddresses=None, MaxLSPSize=None, MaxLSPsOrMGroupPDUsPerBurst=None, Name=None, NoOfMtuProbes=None, OrigLspBufSize=None, Overloaded=None, PSNPInterval=None, PartitionRepair=None, Status=None, TrillMCastIpv4GroupCount=None, TrillMCastIpv6GroupCount=None, TrillMCastMacGroupCount=None):
		"""Gets child instances of IsisTrillRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrillRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Addresses
			AreaAuthenticationType (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Authentication Type
			AreaTransmitPasswordOrMD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): Area Transmit Password / MD5-Key
			Attached (obj(ixnetwork_restpy.multivalue.Multivalue)): Attached
			CSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): CSNP Interval (ms)
			CapabilityRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Capability Router Id
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLSPs (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard LSPs
			EnableHelloPadding (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Hello Padding
			EnableHostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Host Name
			EnableMtuProbe (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MTU Probe
			EnableWideMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Wide Metric
			HostName (obj(ixnetwork_restpy.multivalue.Multivalue)): Host Name
			IgnoreReceiveMD5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Ignore Receive MD5
			InterLSPsOrMGroupPDUBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter LSPs/MGROUP-PDUs Burst Gap (ms)
			LSPLifetime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Rifetime (sec)
			LSPRefreshRate (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Refresh Rate (sec)
			LSPorMGroupPDUMinTransmissionInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP/MGROUP-PDU Min Transmission Interval (ms)
			MaxAreaAddresses (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Area Addresses
			MaxLSPSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSP Size
			MaxLSPsOrMGroupPDUsPerBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Max LSPs/MGROUP-PDUs Per Burst
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfMtuProbes (obj(ixnetwork_restpy.multivalue.Multivalue)): No. of MTU Probes
			OrigLspBufSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Originating LSP Buf Size(Sz)
			Overloaded (obj(ixnetwork_restpy.multivalue.Multivalue)): Overloaded
			PSNPInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): PSNP Interval (ms)
			PartitionRepair (obj(ixnetwork_restpy.multivalue.Multivalue)): Partition Repair
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TrillMCastIpv4GroupCount (number): # Multicast IPv4 Groups(multiplier)
			TrillMCastIpv6GroupCount (number): # Multicast IPv6 Groups(multiplier)
			TrillMCastMacGroupCount (number): MAC Group Count(multiplier)

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter.IsisTrillRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter import IsisTrillRouter
		return self._select(IsisTrillRouter(self), locals())

	def LdpBasicRouter(self, Active=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LdpVersion=None, LeafRangesCountV4=None, Multiplier=None, Name=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV4=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpBasicRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpBasicRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
		return self._select(LdpBasicRouter(self), locals())

	def add_LdpBasicRouter(self, ConnectedVia=None, LdpVersion="version1", LeafRangesCountV4="0", Multiplier="1", Name=None, RootRangesCountV4="0", StackedLayers=None):
		"""Adds a child instance of LdpBasicRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
		return self._create(LdpBasicRouter(self), locals())

	def LdpBasicRouterV6(self, Active=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV6=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpBasicRouterV6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpBasicRouterV6 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
		return self._select(LdpBasicRouterV6(self), locals())

	def add_LdpBasicRouterV6(self, ConnectedVia=None, LdpVersion="version1", LeafRangesCountV6="0", Multiplier="1", Name=None, RootRangesCountV6="0", StackedLayers=None):
		"""Adds a child instance of LdpBasicRouterV6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
		return self._create(LdpBasicRouterV6(self), locals())

	def LdpLpbInterface(self, Active=None, Count=None, DescriptiveName=None, Name=None, Status=None):
		"""Gets child instances of LdpLpbInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpLpbInterface will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface.LdpLpbInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface import LdpLpbInterface
		return self._select(LdpLpbInterface(self), locals())

	def LdpTargetedRouter(self, Active=None, BfdOpeMode=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableBfdRegistration=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, Ipv6peerCount=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LabelSpaceID=None, LdpVersion=None, LeafRangesCountV4=None, Multiplier=None, Name=None, OperationMode=None, PeerCount=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV4=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpTargetedRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpTargetedRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BfdOpeMode (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD Operation Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LabelSpaceID (obj(ixnetwork_restpy.multivalue.Multivalue)): Identifies the set of labels that will be used. Part of the LDP Identifier
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of LDP Label Advertisement
			PeerCount (number): The number of Target Peers configured for this LDP router
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
		return self._select(LdpTargetedRouter(self), locals())

	def add_LdpTargetedRouter(self, ConnectedVia=None, Ipv6peerCount="0", LdpVersion="version1", LeafRangesCountV4="0", Multiplier="1", Name=None, PeerCount="0", RootRangesCountV4="0", StackedLayers=None):
		"""Adds a child instance of LdpTargetedRouter on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV4 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeerCount (number): The number of Target Peers configured for this LDP router
			RootRangesCountV4 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
		return self._create(LdpTargetedRouter(self), locals())

	def LdpTargetedRouterV6(self, Active=None, BfdOpeMode=None, Count=None, DescriptiveName=None, EnableBfdMplsLearnedLsp=None, EnableBfdRegistration=None, EnableFec128Advertisement=None, EnableFec129Advertisement=None, EnableGracefulRestart=None, EnableIpv4Advertisement=None, EnableIpv6Advertisement=None, EnableLspPingLearnedLsp=None, EnableP2MPCapability=None, IgnoreStateAdvertisementControlCapability=None, IncludeSac=None, Ipv6peerCount=None, KeepAliveHoldTime=None, KeepAliveInterval=None, LabelSpaceID=None, LdpVersion=None, LeafRangesCountV6=None, Multiplier=None, Name=None, OperationMode=None, PeerCount=None, ReconnectTime=None, RecoveryTime=None, RootRangesCountV6=None, SessionPreference=None, Status=None):
		"""Gets child instances of LdpTargetedRouterV6 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpTargetedRouterV6 will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BfdOpeMode (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD Operation Mode
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBfdMplsLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, BFD MPLS is enabled.
			EnableBfdRegistration (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable BFD Registration
			EnableFec128Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC128 P2P-PW app type is enabled in SAC TLV.
			EnableFec129Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, FEC129 P2P-PW app type is enabled in SAC TLV.
			EnableGracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.
			EnableIpv4Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.
			EnableIpv6Advertisement (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.
			EnableLspPingLearnedLsp (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LSP Ping is enabled for learned LSPs.
			EnableP2MPCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router is P2MP capable.
			IgnoreStateAdvertisementControlCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Router ignores SAC TLV it receives.
			IncludeSac (obj(ixnetwork_restpy.multivalue.Multivalue)): Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			KeepAliveHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.
			KeepAliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.
			LabelSpaceID (obj(ixnetwork_restpy.multivalue.Multivalue)): Identifies the set of labels that will be used. Part of the LDP Identifier
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OperationMode (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of LDP Label Advertisement
			PeerCount (number): The number of Target Peers configured for this LDP router
			ReconnectTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Reconnect Time ms
			RecoveryTime (obj(ixnetwork_restpy.multivalue.Multivalue)): The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			SessionPreference (obj(ixnetwork_restpy.multivalue.Multivalue)): The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
		return self._select(LdpTargetedRouterV6(self), locals())

	def add_LdpTargetedRouterV6(self, ConnectedVia=None, Ipv6peerCount="0", LdpVersion="version1", LeafRangesCountV6="0", Multiplier="1", Name=None, PeerCount="0", RootRangesCountV6="0", StackedLayers=None):
		"""Adds a child instance of LdpTargetedRouterV6 on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Ipv6peerCount (number): The number of ipv6 Target Peers configured for this LDP router
			LdpVersion (str(version1|version2)): Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2
			LeafRangesCountV6 (number): The number of Leaf Ranges configured for this LDP router
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeerCount (number): The number of Target Peers configured for this LDP router
			RootRangesCountV6 (number): The number of Root Ranges configured for this LDP router
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
		return self._create(LdpTargetedRouterV6(self), locals())

	def Ldpv6LoopbackInterface(self, Active=None, Count=None, DescriptiveName=None, Name=None, Status=None):
		"""Gets child instances of Ldpv6LoopbackInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ldpv6LoopbackInterface will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface.Ldpv6LoopbackInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface import Ldpv6LoopbackInterface
		return self._select(Ldpv6LoopbackInterface(self), locals())

	def add_Ldpv6LoopbackInterface(self, Name=None):
		"""Adds a child instance of Ldpv6LoopbackInterface on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface.Ldpv6LoopbackInterface)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface import Ldpv6LoopbackInterface
		return self._create(Ldpv6LoopbackInterface(self), locals())

	def MplsoamRouter(self, Active=None, Count=None, DescriptiveName=None, Name=None, Status=None):
		"""Gets child instances of MplsoamRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of MplsoamRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter.MplsoamRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter import MplsoamRouter
		return self._select(MplsoamRouter(self), locals())

	def add_MplsoamRouter(self, Name=None):
		"""Adds a child instance of MplsoamRouter on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter.MplsoamRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter import MplsoamRouter
		return self._create(MplsoamRouter(self), locals())

	def NetworkGroup(self, Count=None, DescriptiveName=None, Enabled=None, Multiplier=None, Name=None):
		"""Gets child instances of NetworkGroup from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetworkGroup will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enabled (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables/disables device.
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup.NetworkGroup))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup import NetworkGroup
		return self._select(NetworkGroup(self), locals())

	def add_NetworkGroup(self, Multiplier="1", Name=None):
		"""Adds a child instance of NetworkGroup on the server.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup.NetworkGroup)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup import NetworkGroup
		return self._create(NetworkGroup(self), locals())

	def NetworkTopology(self, Count=None, LinksPerNetwork=None, NodesPerNetwork=None):
		"""Gets child instances of NetworkTopology from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NetworkTopology will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			LinksPerNetwork (number): linksPerNetwork is controled by assigned topology
			NodesPerNetwork (number): Number of nodes in the Network Topology, including the root node defined in the parent Device Group

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology.NetworkTopology))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology import NetworkTopology
		return self._select(NetworkTopology(self), locals())

	def add_NetworkTopology(self):
		"""Adds a child instance of NetworkTopology on the server.

		Args:

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology.NetworkTopology)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology import NetworkTopology
		return self._create(NetworkTopology(self), locals())

	def OfHostData(self, Count=None, DescriptiveName=None, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None, ParentSwitchPortName=None):
		"""Gets child instances of OfHostData from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OfHostData will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfHostPorts (number): number of Host Ports per OF Switch.
			NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab
			ParentSwitchPortName (obj(ixnetwork_restpy.multivalue.Multivalue)): Description of the parent Switch Port.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata.OfHostData))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata import OfHostData
		return self._select(OfHostData(self), locals())

	def add_OfHostData(self, Name=None, NumberOfHostPorts="1", NumberOfHostsPerPort="1"):
		"""Adds a child instance of OfHostData on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfHostPorts (number): number of Host Ports per OF Switch.
			NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata.OfHostData)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata import OfHostData
		return self._create(OfHostData(self), locals())

	def Ospfv2Router(self, BIERPrefix=None, Active=None, Algorithm=None, BBit=None, BierAFlag=None, BierNFlag=None, ConfigureSIDIndexLabel=None, Count=None, DescriptiveName=None, DiscardLearnedLsa=None, DoNotGenerateRouterLsa=None, EBit=None, EFlag=None, EnableBIER=None, EnableMappingServer=None, EnableSegmentRouting=None, GracefulRestart=None, InterFloodLsUpdateBurstGap=None, LFlag=None, LsaRefreshTime=None, LsaRetransmitTime=None, MFlag=None, MaxLsUpdatesPerBurst=None, Name=None, NoOfAddressPrefix=None, NoOfBIERSubDomains=None, NpFlag=None, OobResyncBreakout=None, SRAlgorithmCount=None, SidIndexLabel=None, SrgbRangeCount=None, Status=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwitchRedundantCntrlProcessor=None, SupportReasonUnknown=None, VFlag=None):
		"""Gets child instances of Ospfv2Router from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv2Router will be returned.

		Args:
			BIERPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm for the Node SID/Label
			BBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA B-Bit
			BierAFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Attach Flag
			BierNFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Flag
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DiscardLearnedLsa (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard Learned LSAs
			DoNotGenerateRouterLsa (obj(ixnetwork_restpy.multivalue.Multivalue)): Generate Router LSA.
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA E-Bit
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit-Null Flag
			EnableBIER (bool): Enable BIER
			EnableMappingServer (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Mapping Server of Segment Routing
			EnableSegmentRouting (bool): Enable Segment Routing
			GracefulRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Graceful Restart,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
			InterFloodLsUpdateBurstGap (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Flood LSUpdate burst gap (ms)
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local or Global Flag
			LsaRefreshTime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSA Refresh time (s)
			LsaRetransmitTime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSA Retransmit time(s)
			MFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Mapping Server Flag
			MaxLsUpdatesPerBurst (obj(ixnetwork_restpy.multivalue.Multivalue)): Max Flood LSUpdates Per Burst
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfAddressPrefix (number): Number Of Address Prefix Range
			NoOfBIERSubDomains (number): Number of BIER Sub Domains
			NpFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP Flag
			OobResyncBreakout (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable out-of-band resynchronization breakout
			SRAlgorithmCount (number): SR Algorithm Count
			SidIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SrgbRangeCount (number): SRGB Range Count
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			StrictLsaChecking (obj(ixnetwork_restpy.multivalue.Multivalue)): Terminate graceful restart when an LSA has changed
			SupportForRfc3623 (obj(ixnetwork_restpy.multivalue.Multivalue)): Support RFC 3623 features,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
			SupportReasonSoftReloadUpgrade (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is Software Reload or Upgrade.
			SupportReasonSoftRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is OSPFv2 software restart.
			SupportReasonSwitchRedundantCntrlProcessor (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unplanned switchover.
			SupportReasonUnknown (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unknown and unplanned.
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value or Index Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router.Ospfv2Router))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router import Ospfv2Router
		return self._select(Ospfv2Router(self), locals())

	def Ospfv3Router(self, Active=None, BBit=None, Count=None, DescriptiveName=None, DisableAutoGenerateLinkLsa=None, DisableAutoGenerateRouterLsa=None, DiscardLearnedLsa=None, EBit=None, EnableGracefulRestartHelperMode=None, EnableStrictLsaChecking=None, EnableSupportReasonSwReloadUpgrade=None, EnableSupportReasonSwRestart=None, EnableSupportReasonSwitchToRedundantControlProcessor=None, EnableSupportReasonUnknown=None, LsaRefreshTime=None, LsaRetransmitTime=None, MaxNumLsaPerSecond=None, Name=None, Status=None):
		"""Gets child instances of Ospfv3Router from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv3Router will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA B-Bit
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DisableAutoGenerateLinkLsa (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unknown and unplanned.
			DisableAutoGenerateRouterLsa (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unknown and unplanned.
			DiscardLearnedLsa (obj(ixnetwork_restpy.multivalue.Multivalue)): Discard Learned LSAs
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA E-Bit
			EnableGracefulRestartHelperMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Graceful Restart helper Mode,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs
			EnableStrictLsaChecking (obj(ixnetwork_restpy.multivalue.Multivalue)): Terminate graceful restart when an LSA has changed
			EnableSupportReasonSwReloadUpgrade (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is Software Reload or Upgrade.
			EnableSupportReasonSwRestart (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is Ospfv3 software restart.
			EnableSupportReasonSwitchToRedundantControlProcessor (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unplanned switchover.
			EnableSupportReasonUnknown (obj(ixnetwork_restpy.multivalue.Multivalue)): Support graceful restart helper mode when restart reason is unknown and unplanned.
			LsaRefreshTime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSA Refresh time (s)
			LsaRetransmitTime (obj(ixnetwork_restpy.multivalue.Multivalue)): LSA Retransmit time(s)
			MaxNumLsaPerSecond (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Flood LSUpdate burst gap (ms)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router.Ospfv3Router))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router import Ospfv3Router
		return self._select(Ospfv3Router(self), locals())

	def add_Ospfv3Router(self, Name=None):
		"""Adds a child instance of Ospfv3Router on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router.Ospfv3Router)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router import Ospfv3Router
		return self._create(Ospfv3Router(self), locals())

	def PimRouter(self, Active=None, Count=None, DescriptiveName=None, DrPriority=None, JoinPruneHoldTime=None, JoinPruneInterval=None, Name=None, Status=None):
		"""Gets child instances of PimRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PimRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DrPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): The Designated Router (DR) priority assigned to this emulated PIM-SM router. This value is used in the election of the DR, and is included in the Hello Messages. The larger the DR value, the higher the priority. The default is 0.
			JoinPruneHoldTime (obj(ixnetwork_restpy.multivalue.Multivalue)): (in seconds) The period during which a router receiving a Join/Prune message must keep the Join/State alive. The default is 3 times the Join/Prune Interval (= 180 seconds).
			JoinPruneInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): (in seconds) The Join/Prune interval specifies the length of time between transmissions of Join/Prune messages. The default is 60 seconds.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter.PimRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter import PimRouter
		return self._select(PimRouter(self), locals())

	def add_PimRouter(self, Name=None):
		"""Adds a child instance of PimRouter on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter.PimRouter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter import PimRouter
		return self._create(PimRouter(self), locals())

	def RouterData(self, Count=None, DescriptiveName=None, Name=None, RouterId=None):
		"""Gets child instances of RouterData from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RouterData will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): 4 Byte Router Id in dotted decimal format.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata.RouterData))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata import RouterData
		return self._select(RouterData(self), locals())

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
	def Enabled(self):
		"""Enables/disables device.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enabled')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def Multiplier(self):
		"""Number of device instances per parent device instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

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
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	def remove(self):
		"""Deletes a child instance of DeviceGroup on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def CopyPaste(self, Arg2):
		"""Executes the copyPaste operation on the server.

		Copy this node, paste it behind the destination node and return the newly copied node.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/?deepchild=*)): The destination node below which the copied node will be pasted

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*]): The newly copied node.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('copyPaste', payload=locals(), response_object=None)

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

	def RestartDown(self, Targets):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions in Device Group that are in 'Down' state.

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected Device Groups.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./deviceGroup object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
