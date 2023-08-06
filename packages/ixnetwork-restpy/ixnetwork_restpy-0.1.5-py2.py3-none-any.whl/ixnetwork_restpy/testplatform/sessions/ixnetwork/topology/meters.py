from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Meters(Base):
	"""Openflow Meter Configuration
	"""

	_SDM_NAME = 'meters'

	def __init__(self, parent):
		super(Meters, self).__init__(parent)

	def Bands(self, BandDescription=None, BandType=None, BurstSize=None, Count=None, DescriptiveName=None, Experimenter=None, Multiplier=None, Name=None, PrecedenceLevel=None, Rate=None):
		"""Gets child instances of Bands from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Bands will be returned.

		Args:
			BandDescription (obj(ixnetwork_restpy.multivalue.Multivalue)): The description of the Meter. It is a read-only field.
			BandType (obj(ixnetwork_restpy.multivalue.Multivalue)): Select the band type from the list. Options are as follows: 1) Drop 2) DSCP Remark 3) Experimenter
			BurstSize (obj(ixnetwork_restpy.multivalue.Multivalue)): This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Experimenter (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicats the experimenter ID. The default value is 1.
			Multiplier (number): Number of instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PrecedenceLevel (obj(ixnetwork_restpy.multivalue.Multivalue)): This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
			Rate (obj(ixnetwork_restpy.multivalue.Multivalue)): This indicates the rate value above which the corresponding band may apply to packets. The default value is 1.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bands.Bands))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bands import Bands
		return self._select(Bands(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Advertise(self):
		"""When this check box is cleared, no meter is advertised when the OpenFlow channel comes up or when the Enable check box is selected or cleared.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertise')

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
	def Flags(self):
		"""Select the meter configuration flags from the list.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flags')

	@property
	def MeterDesc(self):
		"""A description of the meter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('meterDesc')

	@property
	def MeterId(self):
		"""The value by which a meter is uniquely identified .

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('meterId')

	@property
	def Multiplier(self):
		"""Number of instances per parent instance (multiplier)

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
	def NumberOfBands(self):
		"""Specify the number of Bands.

		Returns:
			number
		"""
		return self._get_attribute('numberOfBands')
	@NumberOfBands.setter
	def NumberOfBands(self, value):
		self._set_attribute('numberOfBands', value)

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

	def SendAllMeterAdd(self):
		"""Executes the sendAllMeterAdd operation on the server.

		Sends a Meter Add on all meters.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendAllMeterAdd', payload=locals(), response_object=None)

	def SendAllMeterRemove(self):
		"""Executes the sendAllMeterRemove operation on the server.

		Sends a Meter Remove on all meters.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendAllMeterRemove', payload=locals(), response_object=None)

	def SendMeterAdd(self, Arg2):
		"""Executes the sendMeterAdd operation on the server.

		Sends a Meter Add on selected Meter.

		Args:
			Arg2 (list(number)): List of indices into the meter range grid

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendMeterAdd', payload=locals(), response_object=None)

	def SendMeterRemove(self, Arg2):
		"""Executes the sendMeterRemove operation on the server.

		Sends a Meter Remove on selected Meter.

		Args:
			Arg2 (list(number)): List of indices into the meter range grid

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('sendMeterRemove', payload=locals(), response_object=None)
