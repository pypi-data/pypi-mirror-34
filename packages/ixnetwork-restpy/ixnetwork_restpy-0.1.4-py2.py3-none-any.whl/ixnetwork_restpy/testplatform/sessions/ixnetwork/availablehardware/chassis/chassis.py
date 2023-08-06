from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Chassis(Base):
	"""
	"""

	_SDM_NAME = 'chassis'

	def __init__(self, parent):
		super(Chassis, self).__init__(parent)

	def Card(self, AggregationMode=None, AggregationSupported=None, CardId=None, Description=None):
		"""Gets child instances of Card from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Card will be returned.

		Args:
			AggregationMode (str(atlasEightByFiftyGigFanOut|atlasFourByOneHundredGigFanOut|atlasOneByFourHundredGigNonFanOut|atlasTwoByTwoHundredGigNonFanOut|dualMode|eightByTenGigFanOut|fortyGigAggregation|fortyGigCapturePlayback|fortyGigFanOut|fortyGigNonFanOut|fourByTenGigFanOut|fourByTwentyFiveGigNonFanOut|hundredGigCapturePlayback|hundredGigNonFanOut|incompatibleMode|krakenFourByFiftyGigFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|mixed|normal|notSupported|novusFourByTenGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusHundredGigNonFanOut|novusOneByFortyGigNonFanOut|novusTwoByFiftyGigNonFanOut|oneByFiftyGigNonFanOut|oneByTenGigFanOut|singleMode|tenGigAggregation|threeByTenGigFanOut|twoByTwentyFiveGigNonFanOut)): 
			AggregationSupported (bool): 
			CardId (number): 
			Description (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card.Card))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card import Card
		return self._select(Card(self), locals())

	@property
	def CableLength(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('cableLength')
	@CableLength.setter
	def CableLength(self, value):
		self._set_attribute('cableLength', value)

	@property
	def ChainTopology(self):
		"""

		Returns:
			str(daisy|none|star)
		"""
		return self._get_attribute('chainTopology')
	@ChainTopology.setter
	def ChainTopology(self, value):
		self._set_attribute('chainTopology', value)

	@property
	def ChassisType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('chassisType')

	@property
	def ChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('chassisVersion')

	@property
	def ConnectRetries(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('connectRetries')

	@property
	def Hostname(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('hostname')
	@Hostname.setter
	def Hostname(self, value):
		self._set_attribute('hostname', value)

	@property
	def Ip(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ip')

	@property
	def IsLicensesRetrieved(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isLicensesRetrieved')

	@property
	def IsMaster(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isMaster')

	@property
	def IxnBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnBuildNumber')

	@property
	def IxosBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixosBuildNumber')

	@property
	def LicenseErrors(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('licenseErrors')

	@property
	def MasterChassis(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('masterChassis')
	@MasterChassis.setter
	def MasterChassis(self, value):
		self._set_attribute('masterChassis', value)

	@property
	def ProtocolBuildNumber(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('protocolBuildNumber')

	@property
	def SequenceId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('sequenceId')
	@SequenceId.setter
	def SequenceId(self, value):
		self._set_attribute('sequenceId', value)

	@property
	def State(self):
		"""

		Returns:
			str(down|down|polling|polling|polling|ready)
		"""
		return self._get_attribute('state')

	def remove(self):
		"""Deletes a child instance of Chassis on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def GetTapSettings(self, Arg1):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for the given chassis

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getTapSettings', payload=locals(), response_object=None)

	def RefreshInfo(self, Arg1):
		"""Executes the refreshInfo operation on the server.

		Refresh the hardware information.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=card])): An array of valid object references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('refreshInfo', payload=locals(), response_object=None)

	def SetTapSettings(self, Arg1):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for the given chassis.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=chassis])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setTapSettings', payload=locals(), response_object=None)
