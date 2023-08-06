from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Latency(Base):
	"""
	"""

	_SDM_NAME = 'latency'

	def __init__(self, parent):
		super(Latency, self).__init__(parent)

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Mode(self):
		"""

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('mode')
	@Mode.setter
	def Mode(self, value):
		self._set_attribute('mode', value)
