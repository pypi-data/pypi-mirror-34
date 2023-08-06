from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AppLibFlow(Base):
	"""
	"""

	_SDM_NAME = 'appLibFlow'

	def __init__(self, parent):
		super(AppLibFlow, self).__init__(parent)

	def Connection(self, ConnectionId=None, IsTCP=None):
		"""Gets child instances of Connection from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Connection will be returned.

		Args:
			ConnectionId (number): (Read only) Application library flow connection id.
			IsTCP (bool): (Read only) Application library flow connection type - true is the type is TCP, false if it's UDP.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection.Connection))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.connection import Connection
		return self._select(Connection(self), locals())

	def Parameter(self, DisplayValue=None, Option=None):
		"""Gets child instances of Parameter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Parameter will be returned.

		Args:
			DisplayValue (str): Current parameter UI Display Value
			Option (str(choice|range|value)): Each parameter has one or multiple options. Runtime supported options for specific parameter can be retrieved from supportedOptions attribute

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter.Parameter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.parameter.parameter import Parameter
		return self._select(Parameter(self), locals())

	@property
	def ConfigId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('configId')

	@property
	def ConnectionCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('connectionCount')

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def FlowId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('flowId')

	@property
	def FlowSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('flowSize')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def Parameters(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('parameters')

	@property
	def Percentage(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('percentage')
	@Percentage.setter
	def Percentage(self, value):
		self._set_attribute('percentage', value)
