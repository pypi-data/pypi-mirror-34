from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ValueList(Base):
	"""
	"""

	_SDM_NAME = 'valueList'

	def __init__(self, parent):
		super(ValueList, self).__init__(parent)

	@property
	def AvailableWidths(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableWidths')

	@property
	def StartValueList(self):
		"""

		Returns:
			list(number)
		"""
		return self._get_attribute('startValueList')
	@StartValueList.setter
	def StartValueList(self, value):
		self._set_attribute('startValueList', value)

	@property
	def Width(self):
		"""

		Returns:
			str(16|24|32|8)
		"""
		return self._get_attribute('width')
	@Width.setter
	def Width(self, value):
		self._set_attribute('width', value)
