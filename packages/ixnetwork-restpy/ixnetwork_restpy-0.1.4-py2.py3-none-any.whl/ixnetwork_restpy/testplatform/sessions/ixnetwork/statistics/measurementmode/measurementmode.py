from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MeasurementMode(Base):
	"""
	"""

	_SDM_NAME = 'measurementMode'

	def __init__(self, parent):
		super(MeasurementMode, self).__init__(parent)

	@property
	def MeasurementMode(self):
		"""

		Returns:
			str(cumulativeMode|instantaneousMode|mixedMode)
		"""
		return self._get_attribute('measurementMode')
	@MeasurementMode.setter
	def MeasurementMode(self, value):
		self._set_attribute('measurementMode', value)
