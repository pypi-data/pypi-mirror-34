from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DataIntegrity(Base):
	"""
	"""

	_SDM_NAME = 'dataIntegrity'

	def __init__(self, parent):
		super(DataIntegrity, self).__init__(parent)

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
