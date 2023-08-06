from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Instance(Base):
	"""
	"""

	_SDM_NAME = 'instance'

	def __init__(self, parent):
		super(Instance, self).__init__(parent)

	@property
	def SourceValues(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceValues')
