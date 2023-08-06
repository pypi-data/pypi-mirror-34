from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Lns(Base):
	"""L2TP Network Server protocol.
	"""

	_SDM_NAME = 'lns'

	def __init__(self, parent):
		super(Lns, self).__init__(parent)

	@property
	def LnsAuthCredentials(self):
		"""Returns the one and only one LnsAuthCredentials object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lnsauthcredentials.LnsAuthCredentials)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lnsauthcredentials import LnsAuthCredentials
		return self._read(LnsAuthCredentials(self), None)

	def Pppoxserver(self, AcName=None, AcceptAnyAuthValue=None, AuthRetries=None, AuthTimeout=None, AuthType=None, ClientBaseIID=None, ClientBaseIp=None, ClientIID=None, ClientIIDIncr=None, ClientIpIncr=None, Count=None, DescriptiveName=None, DnsServerList=None, EchoReqInterval=None, EnableDnsRa=None, EnableEchoReq=None, EnableEchoRsp=None, EnableMaxPayload=None, Ipv6AddrPrefixLen=None, Ipv6PoolPrefix=None, Ipv6PoolPrefixLen=None, LcpAccm=None, LcpEnableAccm=None, LcpMaxFailure=None, LcpRetries=None, LcpStartDelay=None, LcpTermRetries=None, LcpTimeout=None, MruNegotiation=None, Mtu=None, Multiplier=None, Name=None, NcpRetries=None, NcpTimeout=None, NcpType=None, PppoxServerGlobalAndPortData=None, ServerBaseIID=None, ServerBaseIp=None, ServerDnsOptions=None, ServerIID=None, ServerIIDIncr=None, ServerIpIncr=None, ServerNcpOptions=None, ServerNetmask=None, ServerNetmaskOptions=None, ServerPrimaryDnsAddress=None, ServerSecondaryDnsAddress=None, ServerSignalDslTypeTlv=None, ServerSignalIWF=None, ServerSignalLoopChar=None, ServerSignalLoopEncapsulation=None, ServerSignalLoopId=None, ServerSignalPonTypeTlv=None, ServerV6NcpOptions=None, ServerWinsOptions=None, ServerWinsPrimaryAddress=None, ServerWinsSecondaryAddress=None, ServiceName=None, SessionsCount=None, Status=None):
		"""Gets child instances of Pppoxserver from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Pppoxserver will be returned.

		Args:
			AcName (obj(ixnetwork_restpy.multivalue.Multivalue)): Access Concentrator Name - this option is only available for PPP servers.
			AcceptAnyAuthValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Configures a PAP/CHAP authenticator to accept all offered usernames, passwords, and base domain names
			AuthRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of PPP authentication retries
			AuthTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for PPP authentication, in seconds.
			AuthType (obj(ixnetwork_restpy.multivalue.Multivalue)): The authentication type to use during link setup.
			ClientBaseIID (obj(ixnetwork_restpy.multivalue.Multivalue)): Obsolete - use clientIID instead.
			ClientBaseIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IP address to be used when creating PPP client addresses. This property is used as an incrementor for the 'clientIpIncr' property
			ClientIID (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IPv6CP (RFC5072) interface identifier for the PPP client. Used in conjunction with 'clientIIDIncr' as its incrementor. Valid for IPv6 only. The identifier is used in assigned global and local scope addresses created after negotiation.
			ClientIIDIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Client IPv6CP interface identifier increment, used in conjuction with the base identifier
			ClientIpIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): The incrementor for the clientBaseIp property address when multiple PPP addresses are created.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DnsServerList (obj(ixnetwork_restpy.multivalue.Multivalue)): DNS server list separacted by semicolon
			EchoReqInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Keep alive interval, in seconds
			EnableDnsRa (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable RDNSS routing advertisments
			EnableEchoReq (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableEchoRsp (obj(ixnetwork_restpy.multivalue.Multivalue)): ?
			EnableMaxPayload (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables PPP Max Payload tag
			Ipv6AddrPrefixLen (obj(ixnetwork_restpy.multivalue.Multivalue)): Address prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
			Ipv6PoolPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Pool prefix for the IPv6 IP pool.
			Ipv6PoolPrefixLen (obj(ixnetwork_restpy.multivalue.Multivalue)): Pool prefix length. The difference between the address and pool prefix lengths determine the size of the IPv6 IP pool
			LcpAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Async-Control-Character-Map
			LcpEnableAccm (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Async-Control-Character-Map
			LcpMaxFailure (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of Configure-Nak packets sent without sending a Configure-Ack before assuming that configuration is not converging. Any further Configure-Nak packets for peer requested options are converted to Configure-Reject packets
			LcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP retries
			LcpStartDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Delay time in milliseconds to wait before sending LCP Config Request packet
			LcpTermRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of LCP Termination Retries
			LcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for LCP phase, in seconds
			MruNegotiation (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MRU Negotiation
			Mtu (obj(ixnetwork_restpy.multivalue.Multivalue)): Max Transmit Unit for PPP
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NcpRetries (obj(ixnetwork_restpy.multivalue.Multivalue)): Number of NCP retries
			NcpTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Timeout for NCP phase, in seconds
			NcpType (obj(ixnetwork_restpy.multivalue.Multivalue)): IP address type (IPv4 or IPv6) for Network Control Protocol
			PppoxServerGlobalAndPortData (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Global and Port Settings
			ServerBaseIID (obj(ixnetwork_restpy.multivalue.Multivalue)): Obsolete - use serverIID instead.
			ServerBaseIp (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IP address to be used when create PPP server addresses. This property is used in conjunction with the 'IPv4 Server IP Increment By' property.
			ServerDnsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The server DNS options.
			ServerIID (obj(ixnetwork_restpy.multivalue.Multivalue)): The base IPv6CP (RFC5072) interface identifier for the PPP server, used in conjunction with 'serverIIDIncr' as incrementor. Valid for IPv6 only.
			ServerIIDIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Server IPv6CP interface identifier increment, used in conjuction with the base identifier
			ServerIpIncr (obj(ixnetwork_restpy.multivalue.Multivalue)): Server IP increment, used in conjuction with 'IPv4 Server IP' property
			ServerNcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the NCP configuration mode.
			ServerNetmask (obj(ixnetwork_restpy.multivalue.Multivalue)): The netmask that the server will assign to the client when the Server Netmask Options parameter is set to Supply Netmask.
			ServerNetmaskOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The server netmask option.
			ServerPrimaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The primary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
			ServerSecondaryDnsAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The secondary DNS server address that the server will assign to the client when the Server DNS Options parameter is set to Supply Primary and Secondary.
			ServerSignalDslTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): DSL-Type TLV to be inserted in PPPoE VSA Tag.
			ServerSignalIWF (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0xFE (signaling of interworked sessions) into the DSL tag in PADO and PADS packets.
			ServerSignalLoopChar (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x81 and 0x82 into the DSL tag in PADO and PADS packets.
			ServerSignalLoopEncapsulation (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-option 0x90 into the DSL tag in PADO and PADS packets.
			ServerSignalLoopId (obj(ixnetwork_restpy.multivalue.Multivalue)): This parameter enables or disables the insertion of sub-options 0x01 and 0x02 (Remote ID and Circuit ID) into the DSL tag in PADO and PADS packets.
			ServerSignalPonTypeTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): PON-Type TLV to be inserted in PPPoE VSA Tag.
			ServerV6NcpOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): Specifies the NCP configuration mode.
			ServerWinsOptions (obj(ixnetwork_restpy.multivalue.Multivalue)): The WINS server discovery mode.
			ServerWinsPrimaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The primary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to either Supply Primary and Secondary or Supply Primary Only.
			ServerWinsSecondaryAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): The secondary WINS server address that the server will assign to the client when the Server WINS Options parameter is set to Supply Primary and Secondary.
			ServiceName (obj(ixnetwork_restpy.multivalue.Multivalue)): Access Concentrator Service Name - this option is only available for PPP servers.
			SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver.Pppoxserver))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver import Pppoxserver
		return self._select(Pppoxserver(self), locals())

	def add_Pppoxserver(self, ConnectedVia=None, Multiplier="1", Name=None, SessionsCount="10", StackedLayers=None):
		"""Adds a child instance of Pppoxserver on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SessionsCount (number): Number of PPP clients a single server can accept (multiplier)
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver.Pppoxserver)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoxserver import Pppoxserver
		return self._create(Pppoxserver(self), locals())

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
	def BearerCapability(self):
		"""Indicates to the DUT the bearer device types from which incoming calls will be accepted.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bearerCapability')

	@property
	def BearerType(self):
		"""The bearer type.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bearerType')

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
	def ControlMsgsRetryCounter(self):
		"""Number of L2TP retries

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('controlMsgsRetryCounter')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def CredentialsCount(self):
		"""Number of L2TP authentication credentials the LNS accepts for multiple tunnels establishment.

		Returns:
			number
		"""
		return self._get_attribute('credentialsCount')
	@CredentialsCount.setter
	def CredentialsCount(self, value):
		self._set_attribute('credentialsCount', value)

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableControlChecksum(self):
		"""If checked, UDP checksum is enabled on control plane packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableControlChecksum')

	@property
	def EnableDataChecksum(self):
		"""If checked, UDP checksum is enabled on data plane packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableDataChecksum')

	@property
	def EnableExcludeHdlc(self):
		"""If checked, HDLC header is not encoded in the L2TP packets.

		Returns:
			bool
		"""
		return self._get_attribute('enableExcludeHdlc')
	@EnableExcludeHdlc.setter
	def EnableExcludeHdlc(self, value):
		self._set_attribute('enableExcludeHdlc', value)

	@property
	def EnableHelloRequest(self):
		"""If checked, L2TP hello request is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableHelloRequest')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def FramingCapability(self):
		"""Designates sync or async framing

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('framingCapability')

	@property
	def HelloRequestInterval(self):
		"""Timeout for L2TP hello request, in seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('helloRequestInterval')

	@property
	def InitRetransmitInterval(self):
		"""The initial amount of time that can elapse before an unacknowledged control message is retransmitted.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('initRetransmitInterval')

	@property
	def LacHostName(self):
		"""This is the hostname used in authentication.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lacHostName')

	@property
	def LacSecret(self):
		"""L2TP secret to be used in authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lacSecret')

	@property
	def LnsHostName(self):
		"""L2TP hostname sent by Ixia port when acting as LNS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lnsHostName')

	@property
	def MaxRetransmitInterval(self):
		"""The maximum amount of time that can elapse for receiving a reply for a control message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxRetransmitInterval')

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
	def NoCallTimeout(self):
		"""Timeout for no call establishment, in seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('noCallTimeout')

	@property
	def OffsetByte(self):
		"""L2TP offset byte. Applicable only if offset bit is set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('offsetByte')

	@property
	def OffsetLength(self):
		"""L2TP offset length in bytes. Applicable only if offset bit set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('offsetLength')

	@property
	def ReceiveWindowSize(self):
		"""L2TP Receive Window Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('receiveWindowSize')

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
	def TunnelAuthentication(self):
		"""Enables or disables L2TP tunnel authentication

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tunnelAuthentication')

	@property
	def UdpDestinationPort(self):
		"""UDP port to employ for tunneling destinations

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('udpDestinationPort')

	@property
	def UdpSourcePort(self):
		"""UDP port to employ for tunneling sources

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('udpSourcePort')

	@property
	def UseHiddenAVPs(self):
		"""If checked, Attribute Value Pair hiding is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useHiddenAVPs')

	@property
	def UseLengthBitInPayload(self):
		"""If checked, length bit is set in L2TP data packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useLengthBitInPayload')

	@property
	def UseOffsetBitInPayload(self):
		"""If checked, offset bit is enabled in L2TP data packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useOffsetBitInPayload')

	@property
	def UseSequenceNoInPayload(self):
		"""If checked, sequence bit is set in L2TP data packets.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useSequenceNoInPayload')

	def remove(self):
		"""Deletes a child instance of Lns on the server.

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

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./lns object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
