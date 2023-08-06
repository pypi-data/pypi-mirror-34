from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet(Base):
	"""Ethernet
	"""

	_SDM_NAME = 'ethernet'

	def __init__(self, parent):
		super(Ethernet, self).__init__(parent)

	def Connector(self, ConnectedTo=None, Count=None, PropagateMultiplier=None):
		"""Gets child instances of Connector from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Connector will be returned.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*)): Scenario element this connector is connecting to
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			PropagateMultiplier (bool): The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.connector.Connector))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.connector import Connector
		return self._select(Connector(self), locals())

	def add_Connector(self, ConnectedTo=None):
		"""Adds a child instance of Connector on the server.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*)): Scenario element this connector is connecting to

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.connector.Connector)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.connector import Connector
		return self._create(Connector(self), locals())

	def Nglacp(self, Active=None, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, CollectingFlag=None, CollectorsMaxdelay=None, Count=None, DescriptiveName=None, DistributingFlag=None, InterMarkerPDUDelay=None, InterMarkerPDUDelayRandomMax=None, InterMarkerPDUDelayRandomMin=None, LacpActivity=None, LacpduPeriodicTimeInterval=None, LacpduTimeout=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, Multiplier=None, Name=None, PeriodicSendingOfMarkerRequest=None, SendMarkerRequestOnLagChange=None, Status=None, SupportRespondingToMarker=None, SynchronizationFlag=None):
		"""Gets child instances of Nglacp from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Nglacp will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			ActorKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Key
			ActorPortNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Number
			ActorPortPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor Port Priority
			ActorSystemId (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Id
			ActorSystemPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Actor System Priority
			AdministrativeKey (obj(ixnetwork_restpy.multivalue.Multivalue)): Administrative Key
			AggregationFlagState (obj(ixnetwork_restpy.multivalue.Multivalue)): Aggregation Flag State
			CollectingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Collecting Flag
			CollectorsMaxdelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Collectors Maximum Delay
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DistributingFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Distributing Flag
			InterMarkerPDUDelay (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay (sec)
			InterMarkerPDUDelayRandomMax (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Max (sec)
			InterMarkerPDUDelayRandomMin (obj(ixnetwork_restpy.multivalue.Multivalue)): Inter Marker PDU Delay Random Min (sec)
			LacpActivity (obj(ixnetwork_restpy.multivalue.Multivalue)): LACP Actvity
			LacpduPeriodicTimeInterval (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Periodic Time Interval
			LacpduTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): Lacp PDU Timeout
			MarkerRequestMode (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Request Mode
			MarkerResponseWaitTime (obj(ixnetwork_restpy.multivalue.Multivalue)): Marker Response Wait Time (sec)
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PeriodicSendingOfMarkerRequest (obj(ixnetwork_restpy.multivalue.Multivalue)): Periodic Sending Of Marker Request
			SendMarkerRequestOnLagChange (obj(ixnetwork_restpy.multivalue.Multivalue)): Send Marker Request On Lag Change
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			SupportRespondingToMarker (obj(ixnetwork_restpy.multivalue.Multivalue)): Support Responding To Marker
			SynchronizationFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Synchronization Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.nglacp.Nglacp))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.nglacp import Nglacp
		return self._select(Nglacp(self), locals())

	def add_Nglacp(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Nglacp on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.nglacp.Nglacp)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.nglacp import Nglacp
		return self._create(Nglacp(self), locals())

	def Ngstaticlag(self, Active=None, Count=None, DescriptiveName=None, LagId=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of Ngstaticlag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ngstaticlag will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LagId (obj(ixnetwork_restpy.multivalue.Multivalue)): LAG ID
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.ngstaticlag.Ngstaticlag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.ngstaticlag import Ngstaticlag
		return self._select(Ngstaticlag(self), locals())

	def add_Ngstaticlag(self, ConnectedVia=None, Multiplier="1", Name=None, StackedLayers=None):
		"""Adds a child instance of Ngstaticlag on the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.ngstaticlag.Ngstaticlag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.ngstaticlag import Ngstaticlag
		return self._create(Ngstaticlag(self), locals())

	def PbbEVpnParameter(self, BMac=None, Count=None, UsePbbEVpnParameters=None):
		"""Gets child instances of PbbEVpnParameter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PbbEVpnParameter will be returned.

		Args:
			BMac (obj(ixnetwork_restpy.multivalue.Multivalue)): Broadcast MAC addresses of the devices
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			UsePbbEVpnParameters (bool): Flag to determine whether optional PBB EVPN parameters are provided.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.pbbevpnparameter.PbbEVpnParameter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.pbbevpnparameter import PbbEVpnParameter
		return self._select(PbbEVpnParameter(self), locals())

	def add_PbbEVpnParameter(self, UsePbbEVpnParameters="False"):
		"""Adds a child instance of PbbEVpnParameter on the server.

		Args:
			UsePbbEVpnParameters (bool): Flag to determine whether optional PBB EVPN parameters are provided.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.pbbevpnparameter.PbbEVpnParameter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.pbbevpnparameter import PbbEVpnParameter
		return self._create(PbbEVpnParameter(self), locals())

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
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.tag.Tag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.tag import Tag
		return self._select(Tag(self), locals())

	def add_Tag(self, Enabled="False", Name=None):
		"""Adds a child instance of Tag on the server.

		Args:
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.tag.Tag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.tag import Tag
		return self._create(Tag(self), locals())

	def Vlan(self, Count=None, DescriptiveName=None, Name=None, Priority=None, Tpid=None, VlanId=None):
		"""Gets child instances of Vlan from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Vlan will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): 3-bit user priority field in the VLAN tag.
			Tpid (obj(ixnetwork_restpy.multivalue.Multivalue)): 16-bit Tag Protocol Identifier (TPID) or EtherType in the VLAN tag.
			VlanId (obj(ixnetwork_restpy.multivalue.Multivalue)): 12-bit VLAN ID in the VLAN tag.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vlan.Vlan))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vlan import Vlan
		return self._select(Vlan(self), locals())

	def VpnParameter(self, Count=None, SiteId=None, UseVpnParameters=None):
		"""Gets child instances of VpnParameter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of VpnParameter will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			SiteId (obj(ixnetwork_restpy.multivalue.Multivalue)): VPN Site Identifier
			UseVpnParameters (bool): Flag to determine whether optional VPN parameters are provided.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vpnparameter.VpnParameter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vpnparameter import VpnParameter
		return self._select(VpnParameter(self), locals())

	def add_VpnParameter(self, UseVpnParameters="False"):
		"""Adds a child instance of VpnParameter on the server.

		Args:
			UseVpnParameters (bool): Flag to determine whether optional VPN parameters are provided.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vpnparameter.VpnParameter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.vpnparameter import VpnParameter
		return self._create(VpnParameter(self), locals())

	@property
	def ConnectedVia(self):
		"""List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])
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
	def EnableVlans(self):
		"""Enables VLANs for the sessions.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableVlans')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def Mac(self):
		"""MAC addresses of the devices

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mac')

	@property
	def Mtu(self):
		"""Maximum transmission unit

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
	def NotifyMACMove(self):
		"""Flag to determine if MAC move notification to be sent

		Returns:
			bool
		"""
		return self._get_attribute('notifyMACMove')
	@NotifyMACMove.setter
	def NotifyMACMove(self, value):
		self._set_attribute('notifyMACMove', value)

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
			list(str[None|/api/v1/sessions/1/ixnetwork/lag?deepchild=*])
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
	def UseVlans(self):
		"""Flag to determine whether VLANs are enabled

		Returns:
			bool
		"""
		return self._get_attribute('useVlans')
	@UseVlans.setter
	def UseVlans(self, value):
		self._set_attribute('useVlans', value)

	@property
	def VlanCount(self):
		"""Number of active VLANs

		Returns:
			number
		"""
		return self._get_attribute('vlanCount')
	@VlanCount.setter
	def VlanCount(self, value):
		self._set_attribute('vlanCount', value)

	def remove(self):
		"""Deletes a child instance of Ethernet on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def RestartDown(self, Arg1):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', payload=locals(), response_object=None)

	def RestartDown(self, Arg1, SessionIndices):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Start selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
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
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./ethernet object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
