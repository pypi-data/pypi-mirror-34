from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AdvancedCVFilters(Base):
	"""
	"""

	_SDM_NAME = 'advancedCVFilters'

	def __init__(self, parent):
		super(AdvancedCVFilters, self).__init__(parent)

	@property
	def AvailableFilterOptions(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('availableFilterOptions')

	@property
	def AvailableGroupingOptions(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('availableGroupingOptions')

	@property
	def Caption(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('caption')
	@Caption.setter
	def Caption(self, value):
		self._set_attribute('caption', value)

	@property
	def Expression(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('expression')
	@Expression.setter
	def Expression(self, value):
		self._set_attribute('expression', value)

	@property
	def Grouping(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('grouping')
	@Grouping.setter
	def Grouping(self, value):
		self._set_attribute('grouping', value)

	@property
	def Protocol(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('protocol')
	@Protocol.setter
	def Protocol(self, value):
		self._set_attribute('protocol', value)

	@property
	def SortingStats(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('sortingStats')
	@SortingStats.setter
	def SortingStats(self, value):
		self._set_attribute('sortingStats', value)

	def remove(self):
		"""Deletes a child instance of AdvancedCVFilters on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
