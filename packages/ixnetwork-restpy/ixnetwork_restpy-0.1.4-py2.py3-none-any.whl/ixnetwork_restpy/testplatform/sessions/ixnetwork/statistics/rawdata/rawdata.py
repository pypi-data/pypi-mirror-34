from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RawData(Base):
	"""
	"""

	_SDM_NAME = 'rawData'

	def __init__(self, parent):
		super(RawData, self).__init__(parent)

	def Statistic(self, Caption=None, Enabled=None):
		"""Gets child instances of Statistic from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Statistic will be returned.

		Args:
			Caption (str): 
			Enabled (bool): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic.Statistic))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic import Statistic
		return self._select(Statistic(self), locals())

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def LastRawDataFolder(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('lastRawDataFolder')

	@property
	def Path(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('path')
	@Path.setter
	def Path(self, value):
		self._set_attribute('path', value)

	def StopCollection(self):
		"""Executes the stopCollection operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopCollection', payload=locals(), response_object=None)
