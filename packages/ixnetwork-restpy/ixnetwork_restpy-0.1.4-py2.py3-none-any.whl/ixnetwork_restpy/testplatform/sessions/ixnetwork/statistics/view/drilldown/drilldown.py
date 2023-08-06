from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DrillDown(Base):
	"""
	"""

	_SDM_NAME = 'drillDown'

	def __init__(self, parent):
		super(DrillDown, self).__init__(parent)

	def AvailableTargetRowFilters(self):
		"""Gets child instances of AvailableTargetRowFilters from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableTargetRowFilters will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.availabletargetrowfilters.availabletargetrowfilters.AvailableTargetRowFilters))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.availabletargetrowfilters.availabletargetrowfilters import AvailableTargetRowFilters
		return self._select(AvailableTargetRowFilters(self), locals())

	@property
	def AvailableDrillDownOptions(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableDrillDownOptions')

	@property
	def TargetDrillDownOption(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('targetDrillDownOption')
	@TargetDrillDownOption.setter
	def TargetDrillDownOption(self, value):
		self._set_attribute('targetDrillDownOption', value)

	@property
	def TargetRow(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('targetRow')

	@property
	def TargetRowFilter(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTargetRowFilters)
		"""
		return self._get_attribute('targetRowFilter')
	@TargetRowFilter.setter
	def TargetRowFilter(self, value):
		self._set_attribute('targetRowFilter', value)

	@property
	def TargetRowIndex(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('targetRowIndex')
	@TargetRowIndex.setter
	def TargetRowIndex(self, value):
		self._set_attribute('targetRowIndex', value)

	def remove(self):
		"""Deletes a child instance of DrillDown on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def DoDrillDown(self):
		"""Executes the doDrillDown operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('doDrillDown', payload=locals(), response_object=None)
