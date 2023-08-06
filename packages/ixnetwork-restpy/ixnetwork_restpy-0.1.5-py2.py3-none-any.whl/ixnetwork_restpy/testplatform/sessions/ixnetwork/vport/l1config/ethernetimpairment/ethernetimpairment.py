from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class EthernetImpairment(Base):
	"""
	"""

	_SDM_NAME = 'ethernetImpairment'

	def __init__(self, parent):
		super(EthernetImpairment, self).__init__(parent)

	@property
	def EnablePPM(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enablePPM')
	@EnablePPM.setter
	def EnablePPM(self, value):
		self._set_attribute('enablePPM', value)

	@property
	def Ppm(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ppm')
	@Ppm.setter
	def Ppm(self, value):
		self._set_attribute('ppm', value)
