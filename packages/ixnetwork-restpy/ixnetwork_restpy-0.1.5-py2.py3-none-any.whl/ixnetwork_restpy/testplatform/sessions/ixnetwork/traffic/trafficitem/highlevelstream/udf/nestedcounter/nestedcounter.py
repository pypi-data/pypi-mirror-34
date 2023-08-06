from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NestedCounter(Base):
	"""
	"""

	_SDM_NAME = 'nestedCounter'

	def __init__(self, parent):
		super(NestedCounter, self).__init__(parent)

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
	def InnerLoopIncrementBy(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopIncrementBy')
	@InnerLoopIncrementBy.setter
	def InnerLoopIncrementBy(self, value):
		self._set_attribute('innerLoopIncrementBy', value)

	@property
	def InnerLoopLoopCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopLoopCount')
	@InnerLoopLoopCount.setter
	def InnerLoopLoopCount(self, value):
		self._set_attribute('innerLoopLoopCount', value)

	@property
	def InnerLoopRepeatValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('innerLoopRepeatValue')
	@InnerLoopRepeatValue.setter
	def InnerLoopRepeatValue(self, value):
		self._set_attribute('innerLoopRepeatValue', value)

	@property
	def OuterLoopIncrementBy(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('outerLoopIncrementBy')
	@OuterLoopIncrementBy.setter
	def OuterLoopIncrementBy(self, value):
		self._set_attribute('outerLoopIncrementBy', value)

	@property
	def OuterLoopLoopCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('outerLoopLoopCount')
	@OuterLoopLoopCount.setter
	def OuterLoopLoopCount(self, value):
		self._set_attribute('outerLoopLoopCount', value)

	@property
	def StartValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('startValue')
	@StartValue.setter
	def StartValue(self, value):
		self._set_attribute('startValue', value)

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
