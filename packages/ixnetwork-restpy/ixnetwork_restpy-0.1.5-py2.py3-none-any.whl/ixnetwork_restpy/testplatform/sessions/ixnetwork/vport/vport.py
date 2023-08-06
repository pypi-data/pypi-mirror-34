from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Vport(Base):
	"""
	"""

	_SDM_NAME = 'vport'

	def __init__(self, parent):
		super(Vport, self).__init__(parent)

	@property
	def Capture(self):
		"""Returns the one and only one Capture object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture.Capture)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture import Capture
		return self._read(Capture(self), None)

	@property
	def L1Config(self):
		"""Returns the one and only one L1Config object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config.L1Config)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config import L1Config
		return self._read(L1Config(self), None)

	@property
	def ActualSpeed(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('actualSpeed')

	@property
	def AssignedTo(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('assignedTo')

	@property
	def ConnectedTo(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)
		"""
		return self._get_attribute('connectedTo')
	@ConnectedTo.setter
	def ConnectedTo(self, value):
		self._set_attribute('connectedTo', value)

	@property
	def ConnectionInfo(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('connectionInfo')

	@property
	def ConnectionState(self):
		"""Consolidated state of the vport. This combines the connection state with link state.

		Returns:
			str(assignedInUseByOther|assignedUnconnected|connectedLinkDown|connectedLinkUp|connecting|unassigned)
		"""
		return self._get_attribute('connectionState')

	@property
	def ConnectionStatus(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('connectionStatus')

	@property
	def InternalId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('internalId')

	@property
	def IsAvailable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isAvailable')

	@property
	def IsConnected(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isConnected')

	@property
	def IsMapped(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isMapped')

	@property
	def IsPullOnly(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isPullOnly')
	@IsPullOnly.setter
	def IsPullOnly(self, value):
		self._set_attribute('isPullOnly', value)

	@property
	def IsVMPort(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isVMPort')

	@property
	def IxnChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnChassisVersion')

	@property
	def IxnClientVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnClientVersion')

	@property
	def IxosChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixosChassisVersion')

	@property
	def Licenses(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('licenses')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def RxMode(self):
		"""

		Returns:
			str(capture|captureAndMeasure|measure|packetImpairment)
		"""
		return self._get_attribute('rxMode')
	@RxMode.setter
	def RxMode(self, value):
		self._set_attribute('rxMode', value)

	@property
	def State(self):
		"""

		Returns:
			str(busy|down|unassigned|up|versionMismatch)
		"""
		return self._get_attribute('state')

	@property
	def StateDetail(self):
		"""

		Returns:
			str(busy|cpuNotReady|idle|inActive|l1ConfigFailed|protocolsNotSupported|versionMismatched|waitingForCPUStatus)
		"""
		return self._get_attribute('stateDetail')

	@property
	def TransmitIgnoreLinkStatus(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('transmitIgnoreLinkStatus')
	@TransmitIgnoreLinkStatus.setter
	def TransmitIgnoreLinkStatus(self, value):
		self._set_attribute('transmitIgnoreLinkStatus', value)

	@property
	def TxGapControlMode(self):
		"""

		Returns:
			str(averageMode|fixedMode)
		"""
		return self._get_attribute('txGapControlMode')
	@TxGapControlMode.setter
	def TxGapControlMode(self, value):
		self._set_attribute('txGapControlMode', value)

	@property
	def TxMode(self):
		"""

		Returns:
			str(interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse)
		"""
		return self._get_attribute('txMode')
	@TxMode.setter
	def TxMode(self, value):
		self._set_attribute('txMode', value)

	@property
	def Type(self):
		"""

		Returns:
			str(atlasFourHundredGigLan|atlasFourHundredGigLanFcoe|atm|ethernet|ethernetFcoe|ethernetImpairment|ethernetvm|fc|fortyGigLan|fortyGigLanFcoe|hundredGigLan|hundredGigLanFcoe|krakenFourHundredGigLan|novusHundredGigLan|novusHundredGigLanFcoe|novusTenGigLan|novusTenGigLanFcoe|pos|tenFortyHundredGigLan|tenFortyHundredGigLanFcoe|tenGigLan|tenGigLanFcoe|tenGigWan|tenGigWanFcoe)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def ValidTxModes(self):
		"""

		Returns:
			list(str[interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse])
		"""
		return self._get_attribute('validTxModes')

	def remove(self):
		"""Deletes a child instance of Vport on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def AddQuickFlowGroups(self, Arg1, Arg2):
		"""Executes the addQuickFlowGroups operation on the server.

		Add quick flow traffic items to the configuration.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport])): An array of valid virtual port object references.
			Arg2 (number): The number of quick flow groups to add.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('addQuickFlowGroups', payload=locals(), response_object=None)

	def ClearPortTransmitDuration(self, Arg1):
		"""Executes the clearPortTransmitDuration operation on the server.

		Clear the port transmit duration.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearPortTransmitDuration', payload=locals(), response_object=None)

	def ConnectPort(self, Arg1):
		"""Executes the connectPort operation on the server.

		Connect a list of ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('connectPort', payload=locals(), response_object=None)

	def ConnectPorts(self, Arg1):
		"""Executes the connectPorts operation on the server.

		Connect a list of ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('connectPorts', payload=locals(), response_object=None)

	def EnableOAM(self, Arg1, Arg2):
		"""Executes the enableOAM operation on the server.

		Enable/Disable OAM on a list of ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.
			Arg2 (bool): If true, it will enable OAM. Otherwise, it will disable OAM.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('enableOAM', payload=locals(), response_object=None)

	def Import(self, Arg2):
		"""Executes the import operation on the server.

		Imports the port file (also supports legacy port files).

		Args:
			Arg2 (obj(ixnetwork_restpy.files.Files)): The file to be imported.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		self._check_arg_type(Arg2, Files)
		return self._execute('import', payload=locals(), response_object=None)

	def LinkUpDn(self, Arg1, Arg2):
		"""Executes the linkUpDn operation on the server.

		Simulate port link up/down.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.
			Arg2 (str(down|up)): A valid enum value as specified by the restriction.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('linkUpDn', payload=locals(), response_object=None)

	def PullPort(self):
		"""Executes the pullPort operation on the server.

		Pulls config onto vport or group of vports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('pullPort', payload=locals(), response_object=None)

	def ReleasePort(self, Arg1):
		"""Executes the releasePort operation on the server.

		Release a hardware port.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('releasePort', payload=locals(), response_object=None)

	def ResetPortCpu(self, Arg1):
		"""Executes the resetPortCpu operation on the server.

		Reboot port CPU.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resetPortCpu', payload=locals(), response_object=None)

	def ResetPortCpuAndFactoryDefault(self, Arg1):
		"""Executes the resetPortCpuAndFactoryDefault operation on the server.

		Reboots the port CPU and restores the default settings.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('resetPortCpuAndFactoryDefault', payload=locals(), response_object=None)

	def RestartPppNegotiation(self):
		"""Executes the restartPppNegotiation operation on the server.

		Restarts the PPP negotiation on the port.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('restartPppNegotiation', payload=locals(), response_object=None)

	def SetFactoryDefaults(self, Arg1):
		"""Executes the setFactoryDefaults operation on the server.

		Set default values for port settings.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setFactoryDefaults', payload=locals(), response_object=None)

	def StartStatelessTraffic(self, Arg1):
		"""Executes the startStatelessTraffic operation on the server.

		Start the traffic configuration for stateless traffic items only.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startStatelessTraffic', payload=locals(), response_object=None)

	def StartStatelessTrafficBlocking(self, Arg1):
		"""Executes the startStatelessTrafficBlocking operation on the server.

		Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startStatelessTrafficBlocking', payload=locals(), response_object=None)

	def StopStatelessTraffic(self, Arg1):
		"""Executes the stopStatelessTraffic operation on the server.

		Stop the stateless traffic items.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopStatelessTraffic', payload=locals(), response_object=None)

	def StopStatelessTrafficBlocking(self, Arg1):
		"""Executes the stopStatelessTrafficBlocking operation on the server.

		Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopStatelessTrafficBlocking', payload=locals(), response_object=None)

	def UnassignPorts(self, Arg1, Arg2):
		"""Executes the unassignPorts operation on the server.

		Unassign hardware ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): A list of ports to be unassigned.
			Arg2 (bool): If true, virtual ports will be deleted.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('unassignPorts', payload=locals(), response_object=None)
