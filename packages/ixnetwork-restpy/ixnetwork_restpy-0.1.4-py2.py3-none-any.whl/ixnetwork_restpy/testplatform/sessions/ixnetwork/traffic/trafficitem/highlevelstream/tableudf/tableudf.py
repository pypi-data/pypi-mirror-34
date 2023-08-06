from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TableUdf(Base):
	"""
	"""

	_SDM_NAME = 'tableUdf'

	def __init__(self, parent):
		super(TableUdf, self).__init__(parent)

	def Column(self, Format=None, Offset=None, Size=None):
		"""Gets child instances of Column from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Column will be returned.

		Args:
			Format (str(ascii|binary|custom|decimal|hex|ipv4|ipv6|mac)): 
			Offset (number): 
			Size (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column.Column))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column import Column
		return self._select(Column(self), locals())

	def add_Column(self, Format=None, Offset=None, Size=None, Values=None):
		"""Adds a child instance of Column on the server.

		Args:
			Format (str(ascii|binary|custom|decimal|hex|ipv4|ipv6|mac)): 
			Offset (number): 
			Size (number): 
			Values (list(str)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column.Column)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column import Column
		return self._create(Column(self), locals())

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
