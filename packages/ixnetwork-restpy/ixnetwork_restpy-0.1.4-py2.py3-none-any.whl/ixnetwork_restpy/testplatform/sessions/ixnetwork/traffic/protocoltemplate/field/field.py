from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Field(Base):
	"""
	"""

	_SDM_NAME = 'field'

	def __init__(self, parent):
		super(Field, self).__init__(parent)

	@property
	def __id__(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('__id__')

	@property
	def DisplayName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('displayName')

	@property
	def FieldTypeId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('fieldTypeId')

	@property
	def Length(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('length')

	@property
	def Trackable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('trackable')
