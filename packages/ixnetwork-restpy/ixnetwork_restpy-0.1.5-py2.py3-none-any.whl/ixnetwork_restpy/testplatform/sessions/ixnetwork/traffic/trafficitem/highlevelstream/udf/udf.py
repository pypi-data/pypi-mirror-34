from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Udf(Base):
	"""
	"""

	_SDM_NAME = 'udf'

	def __init__(self, parent):
		super(Udf, self).__init__(parent)

	def Counter(self, BitOffset=None, Count=None, Direction=None, StartValue=None, StepValue=None, Width=None):
		"""Gets child instances of Counter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Counter will be returned.

		Args:
			BitOffset (number): 
			Count (number): 
			Direction (str(decrement|increment)): 
			StartValue (number): 
			StepValue (number): 
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter.Counter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter import Counter
		return self._select(Counter(self), locals())

	def Ipv4(self, BitmaskCount=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, OuterLoopLoopCount=None, SkipValues=None, StartValue=None, Width=None):
		"""Gets child instances of Ipv4 from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ipv4 will be returned.

		Args:
			BitmaskCount (number): 
			InnerLoopIncrementBy (number): 
			InnerLoopLoopCount (number): 
			OuterLoopLoopCount (number): 
			SkipValues (bool): 
			StartValue (number): 
			Width (str(32)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4.Ipv4))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4 import Ipv4
		return self._select(Ipv4(self), locals())

	def NestedCounter(self, BitOffset=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, InnerLoopRepeatValue=None, OuterLoopIncrementBy=None, OuterLoopLoopCount=None, StartValue=None, Width=None):
		"""Gets child instances of NestedCounter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NestedCounter will be returned.

		Args:
			BitOffset (number): 
			InnerLoopIncrementBy (number): 
			InnerLoopLoopCount (number): 
			InnerLoopRepeatValue (number): 
			OuterLoopIncrementBy (number): 
			OuterLoopLoopCount (number): 
			StartValue (number): 
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter.NestedCounter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter import NestedCounter
		return self._select(NestedCounter(self), locals())

	def Random(self, Mask=None, Width=None):
		"""Gets child instances of Random from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Random will be returned.

		Args:
			Mask (str): 
			Width (str(16|24|32|8)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random.Random))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random import Random
		return self._select(Random(self), locals())

	def RangeList(self, BitOffset=None, Width=None):
		"""Gets child instances of RangeList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RangeList will be returned.

		Args:
			BitOffset (number): 
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist.RangeList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist import RangeList
		return self._select(RangeList(self), locals())

	def ValueList(self, Width=None):
		"""Gets child instances of ValueList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of ValueList will be returned.

		Args:
			Width (str(16|24|32|8)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist.ValueList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist import ValueList
		return self._select(ValueList(self), locals())

	@property
	def ByteOffset(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('byteOffset')
	@ByteOffset.setter
	def ByteOffset(self, value):
		self._set_attribute('byteOffset', value)

	@property
	def Chained(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('chained')

	@property
	def ChainedFromUdf(self):
		"""

		Returns:
			str(none|udf1|udf2|udf3|udf4|udf5)
		"""
		return self._get_attribute('chainedFromUdf')
	@ChainedFromUdf.setter
	def ChainedFromUdf(self, value):
		self._set_attribute('chainedFromUdf', value)

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
	def Type(self):
		"""

		Returns:
			str(counter|ipv4|nestedCounter|random|rangeList|valueList)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)
