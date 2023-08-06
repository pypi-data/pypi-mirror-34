from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ProtocolTemplate(Base):
	"""
	"""

	_SDM_NAME = 'protocolTemplate'

	def __init__(self, parent):
		super(ProtocolTemplate, self).__init__(parent)

	def Field(self, __id__=None, DisplayName=None, FieldTypeId=None, Length=None, Trackable=None):
		"""Gets child instances of Field from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Field will be returned.

		Args:
			__id__ (str): 
			DisplayName (str): 
			FieldTypeId (str): 
			Length (number): 
			Trackable (bool): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.field.field.Field))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.field.field import Field
		return self._select(Field(self), locals())

	@property
	def DisplayName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('displayName')

	@property
	def StackTypeId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('stackTypeId')

	@property
	def TemplateName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('templateName')
