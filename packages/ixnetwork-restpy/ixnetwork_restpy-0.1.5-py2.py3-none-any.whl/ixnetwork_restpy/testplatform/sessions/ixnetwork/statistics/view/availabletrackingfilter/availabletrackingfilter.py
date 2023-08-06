from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableTrackingFilter(Base):
	"""
	"""

	_SDM_NAME = 'availableTrackingFilter'

	def __init__(self, parent):
		super(AvailableTrackingFilter, self).__init__(parent)

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

	@property
	def TrackingType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('trackingType')

	@property
	def ValueType(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('valueType')
