from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Error(Base):
	"""
	"""

	_SDM_NAME = 'error'

	def __init__(self, parent):
		super(Error, self).__init__(parent)

	def Instance(self):
		"""Gets child instances of Instance from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Instance will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance.Instance))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.instance.instance import Instance
		return self._select(Instance(self), locals())

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def ErrorCode(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('errorCode')

	@property
	def ErrorLevel(self):
		"""

		Returns:
			str(kAnalysis|kCount|kError|kMessage|kWarning)
		"""
		return self._get_attribute('errorLevel')

	@property
	def InstanceCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('instanceCount')

	@property
	def LastModified(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('lastModified')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def Provider(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('provider')

	@property
	def SourceColumns(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceColumns')

	@property
	def SourceColumnsDisplayName(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceColumnsDisplayName')
