from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Base64CodeOptions(Base):
	"""
	"""

	_SDM_NAME = 'base64CodeOptions'

	def __init__(self, parent):
		super(Base64CodeOptions, self).__init__(parent)

	@property
	def IncludeSampleCode(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('includeSampleCode')
	@IncludeSampleCode.setter
	def IncludeSampleCode(self, value):
		self._set_attribute('includeSampleCode', value)

	@property
	def SampleObjectReferences(self):
		"""

		Returns:
			list(str[None])
		"""
		return self._get_attribute('sampleObjectReferences')
	@SampleObjectReferences.setter
	def SampleObjectReferences(self, value):
		self._set_attribute('sampleObjectReferences', value)
