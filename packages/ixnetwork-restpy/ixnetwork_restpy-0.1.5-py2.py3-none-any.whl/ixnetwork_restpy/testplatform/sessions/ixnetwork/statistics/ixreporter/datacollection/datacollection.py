from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DataCollection(Base):
	"""
	"""

	_SDM_NAME = 'dataCollection'

	def __init__(self, parent):
		super(DataCollection, self).__init__(parent)

	@property
	def Enable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('Enable')
	@Enable.setter
	def Enable(self, value):
		self._set_attribute('Enable', value)

	@property
	def LastRunId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('LastRunId')
