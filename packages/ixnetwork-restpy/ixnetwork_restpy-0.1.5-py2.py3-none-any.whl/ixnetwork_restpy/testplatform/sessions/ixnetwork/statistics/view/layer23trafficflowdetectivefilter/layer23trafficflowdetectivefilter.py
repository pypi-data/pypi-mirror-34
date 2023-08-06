from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Layer23TrafficFlowDetectiveFilter(Base):
	"""
	"""

	_SDM_NAME = 'layer23TrafficFlowDetectiveFilter'

	def __init__(self, parent):
		super(Layer23TrafficFlowDetectiveFilter, self).__init__(parent)

	def AllFlowsFilter(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
		"""Gets child instances of AllFlowsFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AllFlowsFilter will be returned.

		Args:
			NumberOfResults (number): 
			SortByStatisticId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			SortingCondition (str(bestPerformers|worstPerformers)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter.AllFlowsFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter import AllFlowsFilter
		return self._select(AllFlowsFilter(self), locals())

	def add_AllFlowsFilter(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
		"""Adds a child instance of AllFlowsFilter on the server.

		Args:
			NumberOfResults (number): 
			SortByStatisticId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			SortingCondition (str(bestPerformers|worstPerformers)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter.AllFlowsFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.allflowsfilter.allflowsfilter import AllFlowsFilter
		return self._create(AllFlowsFilter(self), locals())

	def DeadFlowsFilter(self, NumberOfResults=None, SortingCondition=None):
		"""Gets child instances of DeadFlowsFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DeadFlowsFilter will be returned.

		Args:
			NumberOfResults (number): 
			SortingCondition (str(ascending|descending)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter.DeadFlowsFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter import DeadFlowsFilter
		return self._select(DeadFlowsFilter(self), locals())

	def add_DeadFlowsFilter(self, NumberOfResults=None, SortingCondition=None):
		"""Adds a child instance of DeadFlowsFilter on the server.

		Args:
			NumberOfResults (number): 
			SortingCondition (str(ascending|descending)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter.DeadFlowsFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.deadflowsfilter.deadflowsfilter import DeadFlowsFilter
		return self._create(DeadFlowsFilter(self), locals())

	def LiveFlowsFilter(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
		"""Gets child instances of LiveFlowsFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LiveFlowsFilter will be returned.

		Args:
			NumberOfResults (number): 
			SortByStatisticId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			SortingCondition (str(bestPerformers|worstPerformers)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter.LiveFlowsFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter import LiveFlowsFilter
		return self._select(LiveFlowsFilter(self), locals())

	def add_LiveFlowsFilter(self, NumberOfResults=None, SortByStatisticId=None, SortingCondition=None):
		"""Adds a child instance of LiveFlowsFilter on the server.

		Args:
			NumberOfResults (number): 
			SortByStatisticId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			SortingCondition (str(bestPerformers|worstPerformers)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter.LiveFlowsFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.liveflowsfilter.liveflowsfilter import LiveFlowsFilter
		return self._create(LiveFlowsFilter(self), locals())

	def StatisticFilter(self, Operator=None, StatisticFilterId=None, Value=None):
		"""Gets child instances of StatisticFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of StatisticFilter will be returned.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isLike|isNotLike|isSmaller)): 
			StatisticFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			Value (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter.StatisticFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter import StatisticFilter
		return self._select(StatisticFilter(self), locals())

	def add_StatisticFilter(self, Operator=None, StatisticFilterId=None, Value=None):
		"""Adds a child instance of StatisticFilter on the server.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isLike|isNotLike|isSmaller)): 
			StatisticFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableStatisticFilter)): 
			Value (str): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter.StatisticFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.statisticfilter.statisticfilter import StatisticFilter
		return self._create(StatisticFilter(self), locals())

	def TrackingFilter(self, Operator=None, TrackingFilterId=None):
		"""Gets child instances of TrackingFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TrackingFilter will be returned.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isInAnyRange|isNoneOf|isSmaller)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.trackingfilter.trackingfilter.TrackingFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.trackingfilter.trackingfilter import TrackingFilter
		return self._select(TrackingFilter(self), locals())

	def add_TrackingFilter(self, Operator=None, TrackingFilterId=None, Value=None):
		"""Adds a child instance of TrackingFilter on the server.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isInAnyRange|isNoneOf|isSmaller)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 
			Value (list(str)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.trackingfilter.trackingfilter.TrackingFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.trackingfilter.trackingfilter import TrackingFilter
		return self._create(TrackingFilter(self), locals())

	@property
	def DeadFlowsCount(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('deadFlowsCount')

	@property
	def DeadFlowsThreshold(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('deadFlowsThreshold')
	@DeadFlowsThreshold.setter
	def DeadFlowsThreshold(self, value):
		self._set_attribute('deadFlowsThreshold', value)

	@property
	def FlowFilterType(self):
		"""

		Returns:
			str(allFlows|deadFlows|liveFlows)
		"""
		return self._get_attribute('flowFilterType')
	@FlowFilterType.setter
	def FlowFilterType(self, value):
		self._set_attribute('flowFilterType', value)

	@property
	def PortFilterIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])
		"""
		return self._get_attribute('portFilterIds')
	@PortFilterIds.setter
	def PortFilterIds(self, value):
		self._set_attribute('portFilterIds', value)

	@property
	def ShowEgressFlows(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('showEgressFlows')
	@ShowEgressFlows.setter
	def ShowEgressFlows(self, value):
		self._set_attribute('showEgressFlows', value)

	@property
	def TrafficItemFilterId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)
		"""
		return self._get_attribute('trafficItemFilterId')
	@TrafficItemFilterId.setter
	def TrafficItemFilterId(self, value):
		self._set_attribute('trafficItemFilterId', value)

	@property
	def TrafficItemFilterIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])
		"""
		return self._get_attribute('trafficItemFilterIds')
	@TrafficItemFilterIds.setter
	def TrafficItemFilterIds(self, value):
		self._set_attribute('trafficItemFilterIds', value)

	def remove(self):
		"""Deletes a child instance of Layer23TrafficFlowDetectiveFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
