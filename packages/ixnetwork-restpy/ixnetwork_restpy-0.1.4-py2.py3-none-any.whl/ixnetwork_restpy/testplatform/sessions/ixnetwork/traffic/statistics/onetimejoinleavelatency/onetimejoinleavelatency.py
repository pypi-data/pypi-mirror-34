from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OneTimeJoinLeaveLatency(Base):
	"""
	"""

	_SDM_NAME = 'oneTimeJoinLeaveLatency'

	def __init__(self, parent):
		super(OneTimeJoinLeaveLatency, self).__init__(parent)

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
