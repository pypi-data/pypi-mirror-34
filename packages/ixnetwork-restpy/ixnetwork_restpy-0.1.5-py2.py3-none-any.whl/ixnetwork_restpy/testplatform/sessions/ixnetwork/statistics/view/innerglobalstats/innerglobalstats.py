from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class InnerGlobalStats(Base):
	"""
	"""

	_SDM_NAME = 'innerGlobalStats'

	def __init__(self, parent):
		super(InnerGlobalStats, self).__init__(parent)

	@property
	def ColumnCaptions(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('columnCaptions')

	@property
	def RowValues(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('rowValues')
