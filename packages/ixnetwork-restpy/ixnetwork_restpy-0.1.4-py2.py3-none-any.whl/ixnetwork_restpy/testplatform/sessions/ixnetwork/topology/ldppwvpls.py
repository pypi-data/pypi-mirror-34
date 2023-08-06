from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ldppwvpls(Base):
	"""LDP FEC128 Configuration
	"""

	_SDM_NAME = 'ldppwvpls'

	def __init__(self, parent):
		super(Ldppwvpls, self).__init__(parent)

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

	def Connector(self, ConnectedTo=None, Count=None, PropagateMultiplier=None):
		"""Gets child instances of Connector from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Connector will be returned.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			PropagateMultiplier (bool): The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._select(Connector(self), locals())

	def add_Connector(self, ConnectedTo=None):
		"""Adds a child instance of Connector on the server.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._create(Connector(self), locals())

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

	def Mpls(self, Bos=None, Cos=None, Count=None, DescriptiveName=None, DestMac=None, Enablecw=None, Multiplier=None, Name=None, Overridecos=None, RxLabelValue=None, Status=None, TransportType=None, Ttl=None, TxLabelValue=None, UpperLayer=None):
		"""Gets child instances of Mpls from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Mpls will be returned.

		Args:
			Bos (obj(ixnetwork_restpy.multivalue.Multivalue)): bos
			Cos (obj(ixnetwork_restpy.multivalue.Multivalue)): EXP
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination Mac.
			Enablecw (bool): Enable Control Word
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overridecos (bool): Override Cos
			RxLabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Rx Label
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TransportType (str(overMac|overTunnel)): TransportType
			Ttl (obj(ixnetwork_restpy.multivalue.Multivalue)): TTL
			TxLabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Tx Label
			UpperLayer (str(nhEthernet|nhIp)): Value to Determine who is upper Layer.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls.Mpls))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls import Mpls
		return self._select(Mpls(self), locals())

	def add_Mpls(self, ConnectedVia=None, Enablecw="False", Multiplier="1", Name=None, Overridecos="False", StackedLayers=None, TransportType="overMac", UpperLayer="nhEthernet"):
		"""Adds a child instance of Mpls on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Enablecw (bool): Enable Control Word
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Overridecos (bool): Override Cos
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			TransportType (str(overMac|overTunnel)): TransportType
			UpperLayer (str(nhEthernet|nhIp)): Value to Determine who is upper Layer.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls.Mpls)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mpls import Mpls
		return self._create(Mpls(self), locals())

	def Tag(self, __id__=None, Count=None, Enabled=None, Name=None):
		"""Gets child instances of Tag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Tag will be returned.

		Args:
			__id__ (obj(ixnetwork_restpy.multivalue.Multivalue)): the tag ids that this entity will use/publish
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._select(Tag(self), locals())

	def add_Tag(self, Enabled="False", Name=None):
		"""Adds a child instance of Tag on the server.

		Args:
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._create(Tag(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AutoPeerID(self):
		"""If selected, LDP Peer IP would be taken from LDP router's peer configuration.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autoPeerID')

	@property
	def AutoPeerId(self):
		"""If selected, LDP Peer IP would be taken from LDP router's peer configuration.

		Returns:
			bool
		"""
		return self._get_attribute('autoPeerId')
	@AutoPeerId.setter
	def AutoPeerId(self, value):
		self._set_attribute('autoPeerId', value)

	@property
	def BfdPwCV(self):
		"""BFD PW-ACH CV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bfdPwCV')

	@property
	def BfdUdpCV(self):
		"""BFD IP/UDP CV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bfdUdpCV')

	@property
	def CBitEnabled(self):
		"""If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('cBitEnabled')

	@property
	def ConnectedVia(self):
		"""List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescEnabled(self):
		"""If selected, indicates that an optional Interface Description is present

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('descEnabled')

	@property
	def Description(self):
		"""An optional user-defined Interface Description. It may be used with ALL VC types. Valid length is 0 to 80 octets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('description')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DownInterval(self):
		"""Time interval for which the PW status will remain down

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downInterval')

	@property
	def DownStart(self):
		"""The duration in time after session becomes up and a notification message being sent to make the session down

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downStart')

	@property
	def EnableCCCVNegotiation(self):
		"""If selected, indicates that CCCV Negotiation is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCCCVNegotiation')

	@property
	def EnablePWStatus(self):
		"""If selected, this enables the use of PW Status TLV in notification messages to notify the PW status

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePWStatus')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def GroupId(self):
		"""A user-defined 32-bit value used to identify a group of VCs

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('groupId')

	@property
	def InterfaceType(self):
		"""The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interfaceType')

	@property
	def Ipv6PeerId(self):
		"""The 128-bit IPv6 address of the LDP Peer.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6PeerId')

	@property
	def LSPPingCV(self):
		"""LSP Ping CV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lSPPingCV')

	@property
	def Label(self):
		"""Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('label')

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

	@property
	def Mtu(self):
		"""The 2-octet value for the maximum Transmission Unit (MTU).

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mtu')

	@property
	def Multiplier(self):
		"""Number of layer instances per parent instance (multiplier)

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
	def PWACHCC(self):
		"""PW-ACH CC

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pWACHCC')

	@property
	def PWStatusCode(self):
		"""PW Status Code to be sent when to transition to down state if PW Status Send Notification is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pWStatusCode')

	@property
	def PeerId(self):
		"""The 32-bit IPv4 address of the LDP Peer.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('peerId')

	@property
	def PwStatusSendNotification(self):
		"""If selected, it signifies whether to send a notification message with a PW status for the corresponding PW

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pwStatusSendNotification')

	@property
	def RepeatCount(self):
		"""The number of times to repeat the Up/Down status of the PW. '0' means keep toggling the Up/Down state indefinitely.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('repeatCount')

	@property
	def RouterAlertCC(self):
		"""Router Alert CC

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routerAlertCC')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def StackedLayers(self):
		"""List of secondary (many to one) child layer protocols

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('stackedLayers')
	@StackedLayers.setter
	def StackedLayers(self, value):
		self._set_attribute('stackedLayers', value)

	@property
	def StateCounts(self):
		"""A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

		Returns:
			dict(total:number,notStarted:number,down:number,up:number)
		"""
		return self._get_attribute('stateCounts')

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	@property
	def UpInterval(self):
		"""Time Interval for which the PW status will remain in Up state before transitioning again to Down state.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('upInterval')

	@property
	def VCIDStart(self):
		"""The value of the VC ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vCIDStart')

	def remove(self):
		"""Deletes a child instance of Ldppwvpls on the server.

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

	def PurgeVCRanges(self, Arg1):
		"""Executes the purgeVCRanges operation on the server.

		Purge VC Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVCRanges', payload=locals(), response_object=None)

	def PurgeVCRanges(self, Arg1, SessionIndices):
		"""Executes the purgeVCRanges operation on the server.

		Purge VC Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVCRanges', payload=locals(), response_object=None)

	def PurgeVCRanges(self, Arg1, SessionIndices):
		"""Executes the purgeVCRanges operation on the server.

		Purge VC Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVCRanges', payload=locals(), response_object=None)

	def Purgevcranges(self, Arg2):
		"""Executes the purgevcranges operation on the server.

		Purge Ethernet VC. Sends Address Withdraw message to purge all MACs learnt for this VC. Applicable for Ethernet Type VC only ( not VLAN).

		Args:
			Arg2 (list(number)): Purge VC Ranges.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('purgevcranges', payload=locals(), response_object=None)

	def PurgeVPLSMac(self, Arg1, Mac_count, Mac):
		"""Executes the purgeVPLSMac operation on the server.

		Purge VPLS MAC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			Mac_count (number): This parameter requires a mac_count of type kInteger
			Mac (str): This parameter requires a mac of type kString

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVPLSMac', payload=locals(), response_object=None)

	def PurgeVPLSMac(self, Arg1, Mac_count, Mac, SessionIndices):
		"""Executes the purgeVPLSMac operation on the server.

		Purge VPLS MAC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			Mac_count (number): This parameter requires a mac_count of type kInteger
			Mac (str): This parameter requires a mac of type kString
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVPLSMac', payload=locals(), response_object=None)

	def PurgeVPLSMac(self, Arg1, SessionIndices, Mac_count, Mac):
		"""Executes the purgeVPLSMac operation on the server.

		Purge VPLS MAC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (str): This parameter requires a mac_count of type kInteger
			Mac_count (number): This parameter requires a mac of type kString
			Mac (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('purgeVPLSMac', payload=locals(), response_object=None)

	def PurgeVPLSMac(self, Arg2, Arg3, Arg4):
		"""Executes the purgeVPLSMac operation on the server.

		Purge Ethernet MAC. Sends Address Withdraw message with specified MACs. Applicable for Ethernet Type VC only ( not VLAN).

		Args:
			Arg2 (list(number)): Purge Ethernet MAC.
			Arg3 (number): Number of Mac addresses to purge
			Arg4 (str): Mac addresses start

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('purgeVPLSMac', payload=locals(), response_object=None)

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Activate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Activate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Activate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Deactivate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Deactivate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Deactivate VC

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldppwvpls object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
