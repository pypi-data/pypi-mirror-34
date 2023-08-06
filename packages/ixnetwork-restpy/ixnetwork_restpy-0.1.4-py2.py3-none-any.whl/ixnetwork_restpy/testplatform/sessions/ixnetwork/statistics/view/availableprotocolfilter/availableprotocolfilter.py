from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableProtocolFilter(Base):
	"""
	"""

	_SDM_NAME = 'availableProtocolFilter'

	def __init__(self, parent):
		super(AvailableProtocolFilter, self).__init__(parent)

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
