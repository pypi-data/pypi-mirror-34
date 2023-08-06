from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Layer23TrafficFlowFilter(Base):
	"""
	"""

	_SDM_NAME = 'layer23TrafficFlowFilter'

	def __init__(self, parent):
		super(Layer23TrafficFlowFilter, self).__init__(parent)

	def EnumerationFilter(self, SortDirection=None, TrackingFilterId=None):
		"""Gets child instances of EnumerationFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of EnumerationFilter will be returned.

		Args:
			SortDirection (str(ascending|descending)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter.EnumerationFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter import EnumerationFilter
		return self._select(EnumerationFilter(self), locals())

	def add_EnumerationFilter(self, SortDirection=None, TrackingFilterId=None):
		"""Adds a child instance of EnumerationFilter on the server.

		Args:
			SortDirection (str(ascending|descending)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter.EnumerationFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.enumerationfilter.enumerationfilter import EnumerationFilter
		return self._create(EnumerationFilter(self), locals())

	def TrackingFilter(self, Operator=None, TrackingFilterId=None):
		"""Gets child instances of TrackingFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TrackingFilter will be returned.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isInAnyRange|isNoneOf|isSmaller)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter.TrackingFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter import TrackingFilter
		return self._select(TrackingFilter(self), locals())

	def add_TrackingFilter(self, Operator=None, TrackingFilterId=None, Value=None):
		"""Adds a child instance of TrackingFilter on the server.

		Args:
			Operator (str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isInAnyRange|isNoneOf|isSmaller)): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): 
			Value (list(str)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter.TrackingFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.trackingfilter.trackingfilter import TrackingFilter
		return self._create(TrackingFilter(self), locals())

	@property
	def AggregatedAcrossPorts(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('aggregatedAcrossPorts')
	@AggregatedAcrossPorts.setter
	def AggregatedAcrossPorts(self, value):
		self._set_attribute('aggregatedAcrossPorts', value)

	@property
	def EgressLatencyBinDisplayOption(self):
		"""

		Returns:
			str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)
		"""
		return self._get_attribute('egressLatencyBinDisplayOption')
	@EgressLatencyBinDisplayOption.setter
	def EgressLatencyBinDisplayOption(self, value):
		self._set_attribute('egressLatencyBinDisplayOption', value)

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
		"""Deletes a child instance of Layer23TrafficFlowFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
