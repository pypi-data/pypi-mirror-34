from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableHardware(Base):
	"""
	"""

	_SDM_NAME = 'availableHardware'

	def __init__(self, parent):
		super(AvailableHardware, self).__init__(parent)

	def Chassis(self, CableLength=None, ChainTopology=None, ChassisType=None, ChassisVersion=None, ConnectRetries=None, Hostname=None, Ip=None, IsLicensesRetrieved=None, IsMaster=None, IxnBuildNumber=None, IxosBuildNumber=None, MasterChassis=None, ProtocolBuildNumber=None, SequenceId=None, State=None):
		"""Gets child instances of Chassis from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Chassis will be returned.

		Args:
			CableLength (number): 
			ChainTopology (str(daisy|none|star)): 
			ChassisType (str): 
			ChassisVersion (str): 
			ConnectRetries (number): 
			Hostname (str): 
			Ip (str): 
			IsLicensesRetrieved (bool): 
			IsMaster (bool): 
			IxnBuildNumber (str): 
			IxosBuildNumber (str): 
			MasterChassis (str): 
			ProtocolBuildNumber (str): 
			SequenceId (number): 
			State (str(down|down|polling|polling|polling|ready)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis.Chassis))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis import Chassis
		return self._select(Chassis(self), locals())

	def add_Chassis(self, CableLength=None, ChainTopology=None, Hostname=None, MasterChassis=None, SequenceId=None):
		"""Adds a child instance of Chassis on the server.

		Args:
			CableLength (number): 
			ChainTopology (str(daisy|none|star)): 
			Hostname (str): 
			MasterChassis (str): 
			SequenceId (number): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis.Chassis)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis import Chassis
		return self._create(Chassis(self), locals())

	@property
	def IsLocked(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isLocked')

	@property
	def IsOffChassis(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isOffChassis')
	@IsOffChassis.setter
	def IsOffChassis(self, value):
		self._set_attribute('isOffChassis', value)

	@property
	def OffChassisHwM(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('offChassisHwM')
	@OffChassisHwM.setter
	def OffChassisHwM(self, value):
		self._set_attribute('offChassisHwM', value)
