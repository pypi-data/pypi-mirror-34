from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableAdvancedFilterOptions(Base):
	"""
	"""

	_SDM_NAME = 'availableAdvancedFilterOptions'

	def __init__(self, parent):
		super(AvailableAdvancedFilterOptions, self).__init__(parent)

	@property
	def Operators(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('operators')

	@property
	def Stat(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('stat')
