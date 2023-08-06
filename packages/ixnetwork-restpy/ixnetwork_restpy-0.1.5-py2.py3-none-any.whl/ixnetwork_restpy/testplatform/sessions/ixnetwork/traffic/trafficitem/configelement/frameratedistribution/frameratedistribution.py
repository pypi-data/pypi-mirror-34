from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FrameRateDistribution(Base):
	"""
	"""

	_SDM_NAME = 'frameRateDistribution'

	def __init__(self, parent):
		super(FrameRateDistribution, self).__init__(parent)

	@property
	def PortDistribution(self):
		"""

		Returns:
			str(applyRateToAll|splitRateEvenly)
		"""
		return self._get_attribute('portDistribution')
	@PortDistribution.setter
	def PortDistribution(self, value):
		self._set_attribute('portDistribution', value)

	@property
	def StreamDistribution(self):
		"""

		Returns:
			str(applyRateToAll|splitRateEvenly)
		"""
		return self._get_attribute('streamDistribution')
	@StreamDistribution.setter
	def StreamDistribution(self, value):
		self._set_attribute('streamDistribution', value)
