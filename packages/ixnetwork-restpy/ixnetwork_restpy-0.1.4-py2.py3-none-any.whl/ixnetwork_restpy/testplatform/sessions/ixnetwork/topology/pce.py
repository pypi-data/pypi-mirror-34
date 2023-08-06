from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Pce(Base):
	"""Pcep Session (Device) level Configuration
	"""

	_SDM_NAME = 'pce'

	def __init__(self, parent):
		super(Pce, self).__init__(parent)

	def PccGroup(self, Active=None, Authentication=None, BurstInterval=None, Count=None, DeadInterval=None, DescriptiveName=None, KeepaliveInterval=None, MD5Key=None, MaxInitiatedLspPerInterval=None, MaxLspsPerPcInitiate=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PccIpv4Address=None, PceInitiatedLspsPerPcc=None, PcePpagTLVType=None, RateControl=None, SrPceCapability=None, Status=None):
		"""Gets child instances of PccGroup from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PccGroup will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Authentication (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of cryptographic authentication to be used on this link interface
			BurstInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Interval in milisecond in which desired rate of messages needs to be maintained.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DeadInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the time interval, after the expiration of which, a PCEP peer declares the session down if no PCEP message has been received.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			KeepaliveInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Frequency/Time Interval of sending PCEP messages to keep the session active.
			MD5Key (obj(ixnetwork_restpy.multivalue.Multivalue)): A value to be used as the secret MD5 Key.
			MaxInitiatedLspPerInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum number of messages can be sent per interval.
			MaxLspsPerPcInitiate (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls the maximum number of LSPs that can be present in a PCInitiate message.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
			PccIpv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 address of the PCC. This column is greyed out in case of PCEv6.
			PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
			PcePpagTLVType (obj(ixnetwork_restpy.multivalue.Multivalue)): PPAG TLV Type specifies PCE's capability of interpreting this type of PPAG TLV
			RateControl (obj(ixnetwork_restpy.multivalue.Multivalue)): The rate control is an optional feature associated with PCE initiated LSP.
			SrPceCapability (obj(ixnetwork_restpy.multivalue.Multivalue)): The SR PCE Capability TLV is an optional TLV associated with the OPEN Object to exchange SR capability of PCEP speakers.
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccgroup.PccGroup))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccgroup import PccGroup
		return self._select(PccGroup(self), locals())

	def add_PccGroup(self, ConnectedVia=None, Multiplier="1", Name=None, PcReplyLspsPerPcc="0", PceInitiatedLspsPerPcc="1", StackedLayers=None):
		"""Adds a child instance of PccGroup on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
			PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccgroup.PccGroup)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccgroup import PccGroup
		return self._create(PccGroup(self), locals())

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
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def MaxPendingConnection(self):
		"""This control allows the user to configure the maximum number of pending connections that an IXIA PCE controller will process concurrently.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxPendingConnection')

	@property
	def MaxUnknownMessage(self):
		"""This control allows the user to configure the maximum number of unknown messages that PCE will receive before closing the session. If the PCE receives unrecognized messages at a rate equal or greater than this value per minute, the PCE MUST send a PCEP CLOSE message with this as the close value. The PCE MUST close the TCP session and MUST NOT send any further PCEP messages on the PCEP session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxUnknownMessage')

	@property
	def MaxUnknownRequest(self):
		"""This control allows the user to configure the maximum number of unknown requests that PCE will receive before closing the session. If the PCE receives PCRep/ PCReq messages with unknown requests at a rate equal or greater than this value per minute, the PCE MUST send a PCEP CLOSE message with this as the close value. The PCE MUST close the TCP session and MUST NOT send any further PCEP messages on the PCEP session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxUnknownRequest')

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
	def PceActionMode(self):
		"""PCE Mode of Action

		Returns:
			str(none|reset|rsvpPcInitiate|rsvpPcrep|rsvpPcupd|srPcrep)
		"""
		return self._get_attribute('pceActionMode')
	@PceActionMode.setter
	def PceActionMode(self, value):
		self._set_attribute('pceActionMode', value)

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
	def TcpPort(self):
		"""PCEP operates over TCP using a registered TCP port (default - 4189). This allows the requirements of reliable messaging and flow control to be met without further protocol work. This control can be configured when user does not want to use the default one.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tcpPort')

	def remove(self):
		"""Deletes a child instance of Pce on the server.

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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./pce object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
