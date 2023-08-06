from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableTrafficItemFilter(Base):
	"""
	"""

	_SDM_NAME = 'availableTrafficItemFilter'

	def __init__(self, parent):
		super(AvailableTrafficItemFilter, self).__init__(parent)

	@property
	def Constraints(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('constraints')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
