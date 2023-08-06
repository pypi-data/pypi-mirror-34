from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableStatisticFilter(Base):
	"""
	"""

	_SDM_NAME = 'availableStatisticFilter'

	def __init__(self, parent):
		super(AvailableStatisticFilter, self).__init__(parent)

	@property
	def Caption(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('caption')
