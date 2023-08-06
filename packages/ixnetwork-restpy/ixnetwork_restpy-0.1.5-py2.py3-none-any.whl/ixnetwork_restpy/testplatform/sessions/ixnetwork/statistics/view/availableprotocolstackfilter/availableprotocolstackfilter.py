from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AvailableProtocolStackFilter(Base):
	"""
	"""

	_SDM_NAME = 'availableProtocolStackFilter'

	def __init__(self, parent):
		super(AvailableProtocolStackFilter, self).__init__(parent)

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
