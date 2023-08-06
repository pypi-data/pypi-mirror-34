from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DynamicFrameSize(Base):
	"""
	"""

	_SDM_NAME = 'dynamicFrameSize'

	def __init__(self, parent):
		super(DynamicFrameSize, self).__init__(parent)

	@property
	def FixedSize(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('fixedSize')
	@FixedSize.setter
	def FixedSize(self, value):
		self._set_attribute('fixedSize', value)

	@property
	def HighLevelStreamName(self):
		"""The name of the high level stream

		Returns:
			str
		"""
		return self._get_attribute('highLevelStreamName')

	@property
	def RandomMax(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('randomMax')
	@RandomMax.setter
	def RandomMax(self, value):
		self._set_attribute('randomMax', value)

	@property
	def RandomMin(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('randomMin')
	@RandomMin.setter
	def RandomMin(self, value):
		self._set_attribute('randomMin', value)

	@property
	def TrafficItemName(self):
		"""The name of the parent traffic item.

		Returns:
			str
		"""
		return self._get_attribute('trafficItemName')

	@property
	def Type(self):
		"""

		Returns:
			str(fixed|random)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)
