from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableAdvancedFilters(Base):
	"""
	"""

	_SDM_NAME = 'availableAdvancedFilters'

	def __init__(self, parent):
		super(AvailableAdvancedFilters, self).__init__(parent)

	@property
	def Expression(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('expression')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
