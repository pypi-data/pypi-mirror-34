from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TransmissionDistribution(Base):
	"""
	"""

	_SDM_NAME = 'transmissionDistribution'

	def __init__(self, parent):
		super(TransmissionDistribution, self).__init__(parent)

	@property
	def AvailableDistributions(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableDistributions')

	@property
	def Distributions(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('distributions')
	@Distributions.setter
	def Distributions(self, value):
		self._set_attribute('distributions', value)

	@property
	def DistributionsDisplayNames(self):
		"""Returns user friendly list of distribution fields

		Returns:
			list(str)
		"""
		return self._get_attribute('distributionsDisplayNames')
