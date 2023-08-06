from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AppErrors(Base):
	"""
	"""

	_SDM_NAME = 'appErrors'

	def __init__(self, parent):
		super(AppErrors, self).__init__(parent)

	def Error(self, Description=None, ErrorCode=None, ErrorLevel=None, InstanceCount=None, LastModified=None, Name=None, Provider=None):
		"""Gets child instances of Error from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Error will be returned.

		Args:
			Description (str): 
			ErrorCode (number): 
			ErrorLevel (str(kAnalysis|kCount|kError|kMessage|kWarning)): 
			InstanceCount (number): 
			LastModified (str): 
			Name (str): 
			Provider (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.error.Error))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.error.error import Error
		return self._select(Error(self), locals())
