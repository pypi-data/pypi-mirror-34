from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LatencyBin(Base):
	"""
	"""

	_SDM_NAME = 'latencyBin'

	def __init__(self, parent):
		super(LatencyBin, self).__init__(parent)

	@property
	def BinLimits(self):
		"""

		Returns:
			list(number)
		"""
		return self._get_attribute('binLimits')
	@BinLimits.setter
	def BinLimits(self, value):
		self._set_attribute('binLimits', value)

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def NumberOfBins(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('numberOfBins')
	@NumberOfBins.setter
	def NumberOfBins(self, value):
		self._set_attribute('numberOfBins', value)
