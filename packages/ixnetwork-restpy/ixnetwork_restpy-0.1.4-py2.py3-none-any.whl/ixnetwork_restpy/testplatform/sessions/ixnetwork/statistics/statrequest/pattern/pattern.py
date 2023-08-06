from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Pattern(Base):
	"""
	"""

	_SDM_NAME = 'pattern'

	def __init__(self, parent):
		super(Pattern, self).__init__(parent)

	@property
	def FlowLabel(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('flowLabel')
	@FlowLabel.setter
	def FlowLabel(self, value):
		self._set_attribute('flowLabel', value)

	@property
	def RowCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('rowCount')

	def remove(self):
		"""Deletes a child instance of Pattern on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
