from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Stack(Base):
	"""
	"""

	_SDM_NAME = 'stack'

	def __init__(self, parent):
		super(Stack, self).__init__(parent)

	def Field(self, __id__=None, ActiveFieldChoice=None, Auto=None, CountValue=None, DefaultValue=None, DisplayName=None, FieldChoice=None, FieldTypeId=None, FieldValue=None, FixedBits=None, FullMesh=None, Length=None, Level=None, MaxValue=None, MinValue=None, Name=None, Offset=None, OffsetFromRoot=None, OnTheFlyMask=None, Optional=None, OptionalEnabled=None, RandomMask=None, RateVaried=None, ReadOnly=None, RequiresUdf=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, SupportsNonRepeatableRandom=None, SupportsOnTheFlyMask=None, TrackingEnabled=None, ValueFormat=None, ValueType=None):
		"""Gets child instances of Field from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Field will be returned.

		Args:
			__id__ (str): 
			ActiveFieldChoice (bool): 
			Auto (bool): 
			CountValue (str): 
			DefaultValue (str): 
			DisplayName (str): 
			FieldChoice (bool): 
			FieldTypeId (str): 
			FieldValue (str): 
			FixedBits (str): 
			FullMesh (bool): 
			Length (number): 
			Level (bool): 
			MaxValue (str): 
			MinValue (str): 
			Name (str): 
			Offset (number): 
			OffsetFromRoot (number): 
			OnTheFlyMask (str): 
			Optional (bool): 
			OptionalEnabled (bool): 
			RandomMask (str): 
			RateVaried (bool): 
			ReadOnly (bool): 
			RequiresUdf (bool): 
			Seed (str): 
			SingleValue (str): 
			StartValue (str): 
			StepValue (str): 
			SupportsNonRepeatableRandom (bool): 
			SupportsOnTheFlyMask (bool): 
			TrackingEnabled (bool): 
			ValueFormat (str(aTM|bool|debug|decimal|decimalFixed2|decimalSigned8|fCID|float|floatEng|hex|hex8WithColons|hex8WithSpaces|iPv4|iPv6|mAC|mACMAC|mACSiteId|mACVLAN|mACVLANSiteId|string|unknown|varLenHex)): 
			ValueType (str(decrement|increment|nonRepeatableRandom|random|repeatableRandomRange|singleValue|valueList)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.stack.field.field.Field))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.stack.field.field import Field
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

	def Append(self, Arg2):
		"""Executes the append operation on the server.

		Append a protocol template after the specified stack object reference.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=protocolTemplate)): A valid /traffic/protocolTemplate object reference.

		Returns:
			str: This exec returns an object reference to the newly appended stack item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('append', payload=locals(), response_object=None)

	def AppendProtocol(self, Arg2):
		"""Executes the appendProtocol operation on the server.

		Append a protocol template after the specified stack object reference.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=protocolTemplate)): A valid /traffic/protocolTemplate object reference.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=stack): This exec returns an object reference to the newly appended stack item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('appendProtocol', payload=locals(), response_object=None)

	def Insert(self, Arg2):
		"""Executes the insert operation on the server.

		Insert a protocol template before the specified stack object reference.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=protocolTemplate)): A valid /traffic/protocolTemplate object reference

		Returns:
			str: This exec returns an object reference to the newly inserted stack item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('insert', payload=locals(), response_object=None)

	def InsertProtocol(self, Arg2):
		"""Executes the insertProtocol operation on the server.

		Insert a protocol template before the specified stack object reference.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=protocolTemplate)): A valid /traffic/protocolTemplate object reference

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=stack): This exec returns an object reference to the newly inserted stack item.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('insertProtocol', payload=locals(), response_object=None)

	def Remove(self):
		"""Executes the remove operation on the server.

		Delete the specified stack object reference.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('remove', payload=locals(), response_object=None)
