from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DeadFlowsFilter(Base):
	"""
	"""

	_SDM_NAME = 'deadFlowsFilter'

	def __init__(self, parent):
		super(DeadFlowsFilter, self).__init__(parent)

	@property
	def NumberOfResults(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('numberOfResults')
	@NumberOfResults.setter
	def NumberOfResults(self, value):
		self._set_attribute('numberOfResults', value)

	@property
	def SortingCondition(self):
		"""

		Returns:
			str(ascending|descending)
		"""
		return self._get_attribute('sortingCondition')
	@SortingCondition.setter
	def SortingCondition(self, value):
		self._set_attribute('sortingCondition', value)

	def remove(self):
		"""Deletes a child instance of DeadFlowsFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
