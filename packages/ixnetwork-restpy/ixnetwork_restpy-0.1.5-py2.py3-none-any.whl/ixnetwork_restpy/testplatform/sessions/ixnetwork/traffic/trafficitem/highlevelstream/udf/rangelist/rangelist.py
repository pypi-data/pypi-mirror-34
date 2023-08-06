from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RangeList(Base):
	"""
	"""

	_SDM_NAME = 'rangeList'

	def __init__(self, parent):
		super(RangeList, self).__init__(parent)

	@property
	def AvailableWidths(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableWidths')

	@property
	def BitOffset(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('bitOffset')
	@BitOffset.setter
	def BitOffset(self, value):
		self._set_attribute('bitOffset', value)

	@property
	def StartValueCountStepList(self):
		"""

		Returns:
			list(number)
		"""
		return self._get_attribute('startValueCountStepList')
	@StartValueCountStepList.setter
	def StartValueCountStepList(self, value):
		self._set_attribute('startValueCountStepList', value)

	@property
	def Width(self):
		"""

		Returns:
			str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)
		"""
		return self._get_attribute('width')
	@Width.setter
	def Width(self, value):
		self._set_attribute('width', value)
