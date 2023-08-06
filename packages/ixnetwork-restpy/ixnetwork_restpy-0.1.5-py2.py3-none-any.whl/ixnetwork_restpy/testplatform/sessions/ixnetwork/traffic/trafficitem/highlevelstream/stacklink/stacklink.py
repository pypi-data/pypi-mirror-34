from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class StackLink(Base):
	"""
	"""

	_SDM_NAME = 'stackLink'

	def __init__(self, parent):
		super(StackLink, self).__init__(parent)

	@property
	def LinkedTo(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=stackLink)
		"""
		return self._get_attribute('linkedTo')
	@LinkedTo.setter
	def LinkedTo(self, value):
		self._set_attribute('linkedTo', value)
