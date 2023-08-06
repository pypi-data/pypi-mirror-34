from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SequenceChecking(Base):
	"""
	"""

	_SDM_NAME = 'sequenceChecking'

	def __init__(self, parent):
		super(SequenceChecking, self).__init__(parent)

	@property
	def AdvancedSequenceThreshold(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('advancedSequenceThreshold')
	@AdvancedSequenceThreshold.setter
	def AdvancedSequenceThreshold(self, value):
		self._set_attribute('advancedSequenceThreshold', value)

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
	def SequenceMode(self):
		"""

		Returns:
			str(advanced|rxPacketArrival|rxSwitchedPath|rxThreshold)
		"""
		return self._get_attribute('sequenceMode')
	@SequenceMode.setter
	def SequenceMode(self, value):
		self._set_attribute('sequenceMode', value)
