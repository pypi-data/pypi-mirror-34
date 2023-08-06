from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LdpBasicRouterV6(Base):
	"""Ldpv6 Device level Configuration
	"""

	_SDM_NAME = 'ldpBasicRouterV6'

	def __init__(self, parent):
		super(LdpBasicRouterV6, self).__init__(parent)

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

	@property
	def LdpLeafRangeV6(self):
		"""Returns the one and only one LdpLeafRangeV6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpleafrangev6.LdpLeafRangeV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpleafrangev6 import LdpLeafRangeV6
		return self._read(LdpLeafRangeV6(self), None)

	@property
	def LdpRootRangeV6(self):
		"""Returns the one and only one LdpRootRangeV6 object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldprootrangev6.LdpRootRangeV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldprootrangev6 import LdpRootRangeV6
		return self._read(LdpRootRangeV6(self), None)

	def Ldpotherpws(self, ATMPresent=None, Active=None, AutoPeerID=None, AutoPeerId=None, BfdPwCV=None, BfdUdpCV=None, CAS=None, CBitEnabled=None, CEMOption=None, CEMOptionPresent=None, CEMPayLoadEnable=None, CEMPayload=None, Count=None, DescEnabled=None, Description=None, DescriptiveName=None, DownInterval=None, DownStart=None, EnableCCCVNegotiation=None, EnablePWStatus=None, Frequency=None, GroupId=None, IfaceType=None, IncludeRTPHeader=None, IncludeSSRC=None, IncludeTDMBitrate=None, IncludeTDMOption=None, IncludeTDMPayload=None, Ipv6PeerId=None, LSPPingCV=None, Label=None, MaxATMCells=None, Mtu=None, Multiplier=None, Name=None, PWACHCC=None, PWStatusCode=None, PayloadType=None, PeerId=None, PwStatusSendNotification=None, RepeatCount=None, RouterAlertCC=None, SP=None, SSRC=None, Status=None, TDMBitrate=None, TDMDataSize=None, TimestampMode=None, UpInterval=None, VCIDStart=None):
		"""Gets child instances of Ldpotherpws from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ldpotherpws will be returned.

		Args:
			ATMPresent (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that ATM Transparent Cell Transport mode is being used
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AutoPeerID (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			BfdPwCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD PW-ACH CV
			BfdUdpCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD IP/UDP CV
			CAS (obj(ixnetwork_restpy.multivalue.Multivalue)): CAS Value
			CBitEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
			CEMOption (obj(ixnetwork_restpy.multivalue.Multivalue)): The value of the CEM option
			CEMOptionPresent (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that a CEM option is present
			CEMPayLoadEnable (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that there is a Circuit Emulation Service over MPLS (CEM) payload
			CEMPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): The length of the CEM payload (in bytes)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that an optional Interface Description is present
			Description (obj(ixnetwork_restpy.multivalue.Multivalue)): An optional user-defined Interface Description. It may be used with ALL VC types. Valid length is 0 to 80 octets
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DownInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time interval for which the PW status will remain down
			DownStart (obj(ixnetwork_restpy.multivalue.Multivalue)): The duration in time after session becomes up and a notification message being sent to make the session down
			EnableCCCVNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that CCCV Negotiation is enabled
			EnablePWStatus (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, this enables the use of PW Status TLV in notification messages to notify the PW status
			Frequency (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the frequency of the payload type
			GroupId (obj(ixnetwork_restpy.multivalue.Multivalue)): A user-defined 32-bit value used to identify a group of VCs
			IfaceType (obj(ixnetwork_restpy.multivalue.Multivalue)): The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface
			IncludeRTPHeader (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that RTP Header is present
			IncludeSSRC (obj(ixnetwork_restpy.multivalue.Multivalue)): Click to enable SSRC
			IncludeTDMBitrate (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that TDM Bitrate is present
			IncludeTDMOption (obj(ixnetwork_restpy.multivalue.Multivalue)): Include TDM Option
			IncludeTDMPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that TDM Payload is present
			Ipv6PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 128-bit IPv6 address of the LDP Peer.
			LSPPingCV (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Ping CV
			Label (obj(ixnetwork_restpy.multivalue.Multivalue)): Label
			MaxATMCells (obj(ixnetwork_restpy.multivalue.Multivalue)): The Maximum number of ATM Cells which may be concatenated and sent in a single MPLS frame
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): The 2-octet value for the maximum Transmission Unit (MTU).
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PWACHCC (obj(ixnetwork_restpy.multivalue.Multivalue)): PW-ACH CC
			PWStatusCode (obj(ixnetwork_restpy.multivalue.Multivalue)): PW Status Code to be sent when to transition to down state if PW Status Send Notification is enabled
			PayloadType (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures the pay load type
			PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 32-bit IPv4 address of the LDP Peer.
			PwStatusSendNotification (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, it signifies whether to send a notification message with a PW status for the corresponding PW
			RepeatCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of times to repeat the Up/Down status of the PW. '0' means keep toggling the Up/Down state indefinitely.
			RouterAlertCC (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Alert CC
			SP (obj(ixnetwork_restpy.multivalue.Multivalue)): SP Value
			SSRC (obj(ixnetwork_restpy.multivalue.Multivalue)): SSRC Value
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TDMBitrate (obj(ixnetwork_restpy.multivalue.Multivalue)): The value of the TDM bitrate
			TDMDataSize (obj(ixnetwork_restpy.multivalue.Multivalue)): The total size of the TDM data
			TimestampMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Timestamp Mode
			UpInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time Interval for which the PW status will remain in Up state before transitioning again to Down state.
			VCIDStart (obj(ixnetwork_restpy.multivalue.Multivalue)): The value of the VC ID

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws.Ldpotherpws))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws import Ldpotherpws
		return self._select(Ldpotherpws(self), locals())

	def add_Ldpotherpws(self, AutoPeerId="False", ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ldpotherpws on the server.

		Args:
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws.Ldpotherpws)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpotherpws import Ldpotherpws
		return self._create(Ldpotherpws(self), locals())

	def Ldppwvpls(self, Active=None, AutoPeerID=None, AutoPeerId=None, BfdPwCV=None, BfdUdpCV=None, CBitEnabled=None, Count=None, DescEnabled=None, Description=None, DescriptiveName=None, DownInterval=None, DownStart=None, EnableCCCVNegotiation=None, EnablePWStatus=None, GroupId=None, InterfaceType=None, Ipv6PeerId=None, LSPPingCV=None, Label=None, Mtu=None, Multiplier=None, Name=None, PWACHCC=None, PWStatusCode=None, PeerId=None, PwStatusSendNotification=None, RepeatCount=None, RouterAlertCC=None, Status=None, UpInterval=None, VCIDStart=None):
		"""Gets child instances of Ldppwvpls from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ldppwvpls will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AutoPeerID (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			BfdPwCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD PW-ACH CV
			BfdUdpCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD IP/UDP CV
			CBitEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that an optional Interface Description is present
			Description (obj(ixnetwork_restpy.multivalue.Multivalue)): An optional user-defined Interface Description. It may be used with ALL VC types. Valid length is 0 to 80 octets
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DownInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time interval for which the PW status will remain down
			DownStart (obj(ixnetwork_restpy.multivalue.Multivalue)): The duration in time after session becomes up and a notification message being sent to make the session down
			EnableCCCVNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that CCCV Negotiation is enabled
			EnablePWStatus (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, this enables the use of PW Status TLV in notification messages to notify the PW status
			GroupId (obj(ixnetwork_restpy.multivalue.Multivalue)): A user-defined 32-bit value used to identify a group of VCs
			InterfaceType (obj(ixnetwork_restpy.multivalue.Multivalue)): The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface
			Ipv6PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 128-bit IPv6 address of the LDP Peer.
			LSPPingCV (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Ping CV
			Label (obj(ixnetwork_restpy.multivalue.Multivalue)): Label
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): The 2-octet value for the maximum Transmission Unit (MTU).
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PWACHCC (obj(ixnetwork_restpy.multivalue.Multivalue)): PW-ACH CC
			PWStatusCode (obj(ixnetwork_restpy.multivalue.Multivalue)): PW Status Code to be sent when to transition to down state if PW Status Send Notification is enabled
			PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 32-bit IPv4 address of the LDP Peer.
			PwStatusSendNotification (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, it signifies whether to send a notification message with a PW status for the corresponding PW
			RepeatCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of times to repeat the Up/Down status of the PW. '0' means keep toggling the Up/Down state indefinitely.
			RouterAlertCC (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Alert CC
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UpInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time Interval for which the PW status will remain in Up state before transitioning again to Down state.
			VCIDStart (obj(ixnetwork_restpy.multivalue.Multivalue)): The value of the VC ID

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls.Ldppwvpls))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls import Ldppwvpls
		return self._select(Ldppwvpls(self), locals())

	def add_Ldppwvpls(self, AutoPeerId="False", ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ldppwvpls on the server.

		Args:
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls.Ldppwvpls)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppwvpls import Ldppwvpls
		return self._create(Ldppwvpls(self), locals())

	def Ldpvplsbgpad(self, Active=None, AsNumberVplsId=None, AssignedNumberVplsId=None, AutoPeerID=None, AutoPeerId=None, BfdPwCV=None, BfdUdpCV=None, CBitEnabled=None, Count=None, DescEnabled=None, Description=None, DescriptiveName=None, DownInterval=None, DownStart=None, EnableCCCVNegotiation=None, EnablePWStatus=None, GroupId=None, InterfaceType=None, IpAddressVplsId=None, Ipv6PeerId=None, LSPPingCV=None, Label=None, Mtu=None, Multiplier=None, Name=None, PWACHCC=None, PWStatusCode=None, PeerId=None, ProvisioningModelType=None, PwStatusSendNotification=None, RepeatCount=None, RouterAlertCC=None, SourceAIIType=None, SourceAIIasIP=None, SourceAIIasNumber=None, Status=None, TargetAIIType=None, TargetAIIasIP=None, TargetAIIasNumber=None, TypeVplsId=None, UpInterval=None):
		"""Gets child instances of Ldpvplsbgpad from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ldpvplsbgpad will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AsNumberVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): The AS number of the VPLS Id
			AssignedNumberVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): The assigned number for the VPLS Id
			AutoPeerID (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			BfdPwCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD PW-ACH CV
			BfdUdpCV (obj(ixnetwork_restpy.multivalue.Multivalue)): BFD IP/UDP CV
			CBitEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, sets the C-Bit (flag). It is the highest order bit in the VC Type field. If the bit is set, it indicates the presence of a control word on this VC.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescEnabled (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that an optional Interface Description is present
			Description (obj(ixnetwork_restpy.multivalue.Multivalue)): An optional user-defined Interface Description. It may be used with ALL VC types. Valid length is 0 to 80 octets
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DownInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time interval for which the PW status will remain down
			DownStart (obj(ixnetwork_restpy.multivalue.Multivalue)): The duration in time after session becomes up and a notification message being sent to make the session down
			EnableCCCVNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, indicates that CCCV Negotiation is enabled
			EnablePWStatus (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, this enables the use of PW Status TLV in notification messages to notify the PW status
			GroupId (obj(ixnetwork_restpy.multivalue.Multivalue)): A user-defined 32-bit value used to identify a group of VCs
			InterfaceType (obj(ixnetwork_restpy.multivalue.Multivalue)): The 15-bit VC Type used in the VC FEC element.It depends on the Layer 2 protocol used on the interface
			IpAddressVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): The IP address of the VPLS id.
			Ipv6PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 128-bit IPv6 address of the LDP Peer.
			LSPPingCV (obj(ixnetwork_restpy.multivalue.Multivalue)): LSP Ping CV
			Label (obj(ixnetwork_restpy.multivalue.Multivalue)): Label
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): The 2-octet value for the maximum Transmission Unit (MTU).
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PWACHCC (obj(ixnetwork_restpy.multivalue.Multivalue)): PW-ACH CC
			PWStatusCode (obj(ixnetwork_restpy.multivalue.Multivalue)): PW Status Code to be sent when to transition to down state if PW Status Send Notification is enabled
			PeerId (obj(ixnetwork_restpy.multivalue.Multivalue)): The 32-bit IPv4 address of the LDP Peer.
			ProvisioningModelType (obj(ixnetwork_restpy.multivalue.Multivalue)): Provisioning Model Type. Manual or BGP Autodiscovery
			PwStatusSendNotification (obj(ixnetwork_restpy.multivalue.Multivalue)): If selected, it signifies whether to send a notification message with a PW status for the corresponding PW
			RepeatCount (obj(ixnetwork_restpy.multivalue.Multivalue)): The number of times to repeat the Up/Down status of the PW. '0' means keep toggling the Up/Down state indefinitely.
			RouterAlertCC (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Alert CC
			SourceAIIType (obj(ixnetwork_restpy.multivalue.Multivalue)): Source AII Type
			SourceAIIasIP (obj(ixnetwork_restpy.multivalue.Multivalue)): Source AII as IP
			SourceAIIasNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Source AII as Number
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			TargetAIIType (obj(ixnetwork_restpy.multivalue.Multivalue)): Target AII Type
			TargetAIIasIP (obj(ixnetwork_restpy.multivalue.Multivalue)): Target AII as IP
			TargetAIIasNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Target AII as Number
			TypeVplsId (obj(ixnetwork_restpy.multivalue.Multivalue)): The VPLS Id format
			UpInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Time Interval for which the PW status will remain in Up state before transitioning again to Down state.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad.Ldpvplsbgpad))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad import Ldpvplsbgpad
		return self._select(Ldpvplsbgpad(self), locals())

	def add_Ldpvplsbgpad(self, AutoPeerId="False", ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ldpvplsbgpad on the server.

		Args:
			AutoPeerId (bool): If selected, LDP Peer IP would be taken from LDP router's peer configuration.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad.Ldpvplsbgpad)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpvplsbgpad import Ldpvplsbgpad
		return self._create(Ldpvplsbgpad(self), locals())

	def LearnedInfo(self, State=None, Type=None):
		"""Gets child instances of LearnedInfo from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LearnedInfo will be returned.

		Args:
			State (str): The state of the learned information query
			Type (str): The type of learned information

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
		return self._select(LearnedInfo(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

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
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableBfdMplsLearnedLsp(self):
		"""If selected, BFD MPLS is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBfdMplsLearnedLsp')

	@property
	def EnableFec128Advertisement(self):
		"""If selected, FEC128 P2P-PW app type is enabled in SAC TLV.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFec128Advertisement')

	@property
	def EnableFec129Advertisement(self):
		"""If selected, FEC129 P2P-PW app type is enabled in SAC TLV.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFec129Advertisement')

	@property
	def EnableGracefulRestart(self):
		"""If selected, LDP Graceful Restart is enabled on this Ixia-emulated LDP Router.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGracefulRestart')

	@property
	def EnableIpv4Advertisement(self):
		"""If selected, IPv4-Prefix LSP app type is enabled in SAC TLV.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableIpv4Advertisement')

	@property
	def EnableIpv6Advertisement(self):
		"""If selected, IPv6-Prefix LSP app type is enabled in SAC TLV.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableIpv6Advertisement')

	@property
	def EnableLspPingLearnedLsp(self):
		"""If selected, LSP Ping is enabled for learned LSPs.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLspPingLearnedLsp')

	@property
	def EnableP2MPCapability(self):
		"""If selected, LDP Router is P2MP capable.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableP2MPCapability')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def IgnoreStateAdvertisementControlCapability(self):
		"""If selected, LDP Router ignores SAC TLV it receives.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ignoreStateAdvertisementControlCapability')

	@property
	def IncludeSac(self):
		"""Select to include 'State Advertisement Control Capability' TLV in Initialization message and Capability message

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSac')

	@property
	def KeepAliveHoldTime(self):
		"""The period of time, in seconds, between KEEP-ALIVE messages sent to the DUT.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('keepAliveHoldTime')

	@property
	def KeepAliveInterval(self):
		"""The frequency, in seconds, at which IxNetwork sends KEEP-ALIVE requests.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('keepAliveInterval')

	@property
	def LdpVersion(self):
		"""Version of LDP. When RFC 5036 is chosen, LDP version is version 1. When draft-pdutta-mpls-ldp-adj-capability-00 is chosen, LDP version is version 2

		Returns:
			str(version1|version2)
		"""
		return self._get_attribute('ldpVersion')
	@LdpVersion.setter
	def LdpVersion(self, value):
		self._set_attribute('ldpVersion', value)

	@property
	def LeafRangesCountV6(self):
		"""The number of Leaf Ranges configured for this LDP router

		Returns:
			number
		"""
		return self._get_attribute('leafRangesCountV6')
	@LeafRangesCountV6.setter
	def LeafRangesCountV6(self, value):
		self._set_attribute('leafRangesCountV6', value)

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

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
	def ReconnectTime(self):
		"""Reconnect Time ms

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reconnectTime')

	@property
	def RecoveryTime(self):
		"""The restarting LSR advertises the amount of time that it will retain its MPLS forwarding state.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('recoveryTime')

	@property
	def RootRangesCountV6(self):
		"""The number of Root Ranges configured for this LDP router

		Returns:
			number
		"""
		return self._get_attribute('rootRangesCountV6')
	@RootRangesCountV6.setter
	def RootRangesCountV6(self, value):
		self._set_attribute('rootRangesCountV6', value)

	@property
	def SessionInfo(self):
		"""Logs additional information about the LDP session state

		Returns:
			list(str[lDP_STATE_INITIALIZED|lDP_STATE_MULTIPLE_PEERS|lDP_STATE_NON_EXISTENT|lDP_STATE_OPENREC|lDP_STATE_OPENSENT|lDP_STATE_OPERATIONAL|none])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SessionPreference(self):
		"""The transport connection preference of the LDP router that is conveyed in Dual-stack capability TLV included in LDP Hello message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sessionPreference')

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

	def remove(self):
		"""Deletes a child instance of LdpBasicRouterV6 on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def ClearAllLearnedInfo(self, Arg1):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAllLearnedInfo', payload=locals(), response_object=None)

	def ClearAllLearnedInfoInClient(self, Arg2):
		"""Executes the clearAllLearnedInfoInClient operation on the server.

		Clears ALL routes from GUI grid for the selected LDP Router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('clearAllLearnedInfoInClient', payload=locals(), response_object=None)

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

	def GetAllLearnedInfo(self, Arg1):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetAllLearnedInfo(self, Arg2):
		"""Executes the getAllLearnedInfo operation on the server.

		Gets ALL routes learnt and stored by this LDP Router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getAllLearnedInfo', payload=locals(), response_object=None)

	def GetFEC128LearnedInfo(self, Arg1):
		"""Executes the getFEC128LearnedInfo operation on the server.

		Get FEC 128 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC128LearnedInfo', payload=locals(), response_object=None)

	def GetFEC128LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getFEC128LearnedInfo operation on the server.

		Get FEC 128 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC128LearnedInfo', payload=locals(), response_object=None)

	def GetFEC128LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getFEC128LearnedInfo operation on the server.

		Get FEC 128 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC128LearnedInfo', payload=locals(), response_object=None)

	def GetFEC128LearnedInfo(self, Arg2):
		"""Executes the getFEC128LearnedInfo operation on the server.

		Gets FEC128 Learned Information learnt by this LDP router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getFEC128LearnedInfo', payload=locals(), response_object=None)

	def GetFEC129LearnedInfo(self, Arg1):
		"""Executes the getFEC129LearnedInfo operation on the server.

		Get FEC 129 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC129LearnedInfo', payload=locals(), response_object=None)

	def GetFEC129LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getFEC129LearnedInfo operation on the server.

		Get FEC 129 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC129LearnedInfo', payload=locals(), response_object=None)

	def GetFEC129LearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getFEC129LearnedInfo operation on the server.

		Get FEC 129 Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getFEC129LearnedInfo', payload=locals(), response_object=None)

	def GetFEC129LearnedInfo(self, Arg2):
		"""Executes the getFEC129LearnedInfo operation on the server.

		Gets FEC129 Learned Information learnt by this LDP router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getFEC129LearnedInfo', payload=locals(), response_object=None)

	def GetIPv4FECLearnedInfo(self, Arg1):
		"""Executes the getIPv4FECLearnedInfo operation on the server.

		Get IPv4 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4FECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4FECLearnedInfo operation on the server.

		Get IPv4 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4FECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv4FECLearnedInfo operation on the server.

		Get IPv4 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv4FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv4FECLearnedInfo(self, Arg2):
		"""Executes the getIPv4FECLearnedInfo operation on the server.

		Gets Learned Information learnt by this LDP router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv4FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6FECLearnedInfo(self, Arg1):
		"""Executes the getIPv6FECLearnedInfo operation on the server.

		Get IPv6 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6FECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6FECLearnedInfo operation on the server.

		Get IPv6 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6FECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getIPv6FECLearnedInfo operation on the server.

		Get IPv6 FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIPv6FECLearnedInfo', payload=locals(), response_object=None)

	def GetIPv6FECLearnedInfo(self, Arg2):
		"""Executes the getIPv6FECLearnedInfo operation on the server.

		Gets Learned Information learnt by this LDP router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getIPv6FECLearnedInfo', payload=locals(), response_object=None)

	def GetP2MPFECLearnedInfo(self, Arg1):
		"""Executes the getP2MPFECLearnedInfo operation on the server.

		Get P2MP FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getP2MPFECLearnedInfo', payload=locals(), response_object=None)

	def GetP2MPFECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getP2MPFECLearnedInfo operation on the server.

		Get P2MP FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getP2MPFECLearnedInfo', payload=locals(), response_object=None)

	def GetP2MPFECLearnedInfo(self, Arg1, SessionIndices):
		"""Executes the getP2MPFECLearnedInfo operation on the server.

		Get P2MP FEC Learned Info

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getP2MPFECLearnedInfo', payload=locals(), response_object=None)

	def GetP2MPFECLearnedInfo(self, Arg2):
		"""Executes the getP2MPFECLearnedInfo operation on the server.

		Gets P2MP FEC Learned Information learnt by this LDP router.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getP2MPFECLearnedInfo', payload=locals(), response_object=None)

	def GracefullyRestart(self, Arg1, Delay):
		"""Executes the gracefullyRestart operation on the server.

		Gracefully Restart

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			Delay (number): This parameter requires a delay of type kInteger

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefullyRestart', payload=locals(), response_object=None)

	def GracefullyRestart(self, Arg1, Delay, SessionIndices):
		"""Executes the gracefullyRestart operation on the server.

		Gracefully Restart

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			Delay (number): This parameter requires a delay of type kInteger
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefullyRestart', payload=locals(), response_object=None)

	def GracefullyRestart(self, Arg1, SessionIndices, Delay):
		"""Executes the gracefullyRestart operation on the server.

		Gracefully Restart

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a delay of type kInteger
			Delay (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('gracefullyRestart', payload=locals(), response_object=None)

	def GracefullyRestart(self, Arg2, Arg3):
		"""Executes the gracefullyRestart operation on the server.

		Gracefully restart selected Routers

		Args:
			Arg2 (list(number)): Action indices for gracefully restart
			Arg3 (number): Restart After Time (in secs)

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('gracefullyRestart', payload=locals(), response_object=None)

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1, SessionIndices):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def ResumeKeepAlive(self, Arg1, SessionIndices):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resumeKeepAlive', payload=locals(), response_object=None)

	def Resumekeepalive(self, Arg2):
		"""Executes the resumekeepalive operation on the server.

		Start Sending Keep Alive Messages.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('resumekeepalive', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop LDP Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1, SessionIndices):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def StopKeepAlive(self, Arg1, SessionIndices):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ldpBasicRouterV6 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopKeepAlive', payload=locals(), response_object=None)

	def Stopkeepalive(self, Arg2):
		"""Executes the stopkeepalive operation on the server.

		Stop Sending Keep Alive Messages.

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopkeepalive', payload=locals(), response_object=None)
