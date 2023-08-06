from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class View(Base):
	"""
	"""

	_SDM_NAME = 'view'

	def __init__(self, parent):
		super(View, self).__init__(parent)

	def AdvancedCVFilters(self, AvailableFilterOptions=None, AvailableGroupingOptions=None, Caption=None, Expression=None, Grouping=None, Protocol=None, SortingStats=None):
		"""Gets child instances of AdvancedCVFilters from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AdvancedCVFilters will be returned.

		Args:
			AvailableFilterOptions (str): 
			AvailableGroupingOptions (str): 
			Caption (str): 
			Expression (str): 
			Grouping (str): 
			Protocol (str): 
			SortingStats (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters.AdvancedCVFilters))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters import AdvancedCVFilters
		return self._select(AdvancedCVFilters(self), locals())

	def add_AdvancedCVFilters(self, Caption=None, Expression=None, Grouping=None, Protocol=None, SortingStats=None):
		"""Adds a child instance of AdvancedCVFilters on the server.

		Args:
			Caption (str): 
			Expression (str): 
			Grouping (str): 
			Protocol (str): 
			SortingStats (str): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters.AdvancedCVFilters)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters import AdvancedCVFilters
		return self._create(AdvancedCVFilters(self), locals())

	def AvailableAdvancedFilters(self, Expression=None, Name=None):
		"""Gets child instances of AvailableAdvancedFilters from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableAdvancedFilters will be returned.

		Args:
			Expression (str): 
			Name (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableadvancedfilters.availableadvancedfilters.AvailableAdvancedFilters))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableadvancedfilters.availableadvancedfilters import AvailableAdvancedFilters
		return self._select(AvailableAdvancedFilters(self), locals())

	def AvailablePortFilter(self, Name=None):
		"""Gets child instances of AvailablePortFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailablePortFilter will be returned.

		Args:
			Name (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableportfilter.availableportfilter.AvailablePortFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableportfilter.availableportfilter import AvailablePortFilter
		return self._select(AvailablePortFilter(self), locals())

	def AvailableProtocolFilter(self, Name=None):
		"""Gets child instances of AvailableProtocolFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableProtocolFilter will be returned.

		Args:
			Name (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolfilter.availableprotocolfilter.AvailableProtocolFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolfilter.availableprotocolfilter import AvailableProtocolFilter
		return self._select(AvailableProtocolFilter(self), locals())

	def AvailableProtocolStackFilter(self, Name=None):
		"""Gets child instances of AvailableProtocolStackFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableProtocolStackFilter will be returned.

		Args:
			Name (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolstackfilter.availableprotocolstackfilter.AvailableProtocolStackFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolstackfilter.availableprotocolstackfilter import AvailableProtocolStackFilter
		return self._select(AvailableProtocolStackFilter(self), locals())

	def AvailableStatisticFilter(self, Caption=None):
		"""Gets child instances of AvailableStatisticFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableStatisticFilter will be returned.

		Args:
			Caption (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availablestatisticfilter.availablestatisticfilter.AvailableStatisticFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availablestatisticfilter.availablestatisticfilter import AvailableStatisticFilter
		return self._select(AvailableStatisticFilter(self), locals())

	def AvailableTrackingFilter(self, Name=None, TrackingType=None, ValueType=None):
		"""Gets child instances of AvailableTrackingFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableTrackingFilter will be returned.

		Args:
			Name (str): 
			TrackingType (str): 
			ValueType (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrackingfilter.availabletrackingfilter.AvailableTrackingFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrackingfilter.availabletrackingfilter import AvailableTrackingFilter
		return self._select(AvailableTrackingFilter(self), locals())

	def AvailableTrafficItemFilter(self, Name=None):
		"""Gets child instances of AvailableTrafficItemFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AvailableTrafficItemFilter will be returned.

		Args:
			Name (str): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrafficitemfilter.availabletrafficitemfilter.AvailableTrafficItemFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrafficitemfilter.availabletrafficitemfilter import AvailableTrafficItemFilter
		return self._select(AvailableTrafficItemFilter(self), locals())

	@property
	def Data(self):
		"""Returns the one and only one Data object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.data.Data)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.data import Data
		return self._read(Data(self), None)

	def DrillDown(self, TargetDrillDownOption=None, TargetRowFilter=None, TargetRowIndex=None):
		"""Gets child instances of DrillDown from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of DrillDown will be returned.

		Args:
			TargetDrillDownOption (str): 
			TargetRowFilter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTargetRowFilters)): 
			TargetRowIndex (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown.DrillDown))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown import DrillDown
		return self._select(DrillDown(self), locals())

	def add_DrillDown(self, TargetDrillDownOption=None, TargetRowFilter=None, TargetRowIndex=None):
		"""Adds a child instance of DrillDown on the server.

		Args:
			TargetDrillDownOption (str): 
			TargetRowFilter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTargetRowFilters)): 
			TargetRowIndex (number): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown.DrillDown)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown import DrillDown
		return self._create(DrillDown(self), locals())

	@property
	def FormulaCatalog(self):
		"""Returns the one and only one FormulaCatalog object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.formulacatalog.formulacatalog.FormulaCatalog)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.formulacatalog.formulacatalog import FormulaCatalog
		return self._read(FormulaCatalog(self), None)

	@property
	def InnerGlobalStats(self):
		"""Returns the one and only one InnerGlobalStats object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.innerglobalstats.innerglobalstats.InnerGlobalStats)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.innerglobalstats.innerglobalstats import InnerGlobalStats
		return self._read(InnerGlobalStats(self), None)

	def Layer23NextGenProtocolFilter(self, AdvancedCVFilter=None, AdvancedFilterName=None, AggregationType=None, AllAdvancedFilters=None, MatchingAdvancedFilters=None):
		"""Gets child instances of Layer23NextGenProtocolFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23NextGenProtocolFilter will be returned.

		Args:
			AdvancedCVFilter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=advancedCVFilters)): 
			AdvancedFilterName (str): 
			AggregationType (str(perPort|perSession)): 
			AllAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 
			MatchingAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter.Layer23NextGenProtocolFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter import Layer23NextGenProtocolFilter
		return self._select(Layer23NextGenProtocolFilter(self), locals())

	def add_Layer23NextGenProtocolFilter(self, AdvancedCVFilter=None, AdvancedFilterName=None, AggregationType=None, PortFilterIds=None, ProtocolFilterIds=None):
		"""Adds a child instance of Layer23NextGenProtocolFilter on the server.

		Args:
			AdvancedCVFilter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=advancedCVFilters)): 
			AdvancedFilterName (str): 
			AggregationType (str(perPort|perSession)): 
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter.Layer23NextGenProtocolFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter import Layer23NextGenProtocolFilter
		return self._create(Layer23NextGenProtocolFilter(self), locals())

	def Layer23ProtocolAuthAccessFilter(self):
		"""Gets child instances of Layer23ProtocolAuthAccessFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23ProtocolAuthAccessFilter will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter.Layer23ProtocolAuthAccessFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter import Layer23ProtocolAuthAccessFilter
		return self._select(Layer23ProtocolAuthAccessFilter(self), locals())

	def add_Layer23ProtocolAuthAccessFilter(self, PortFilterIds=None, ProtocolFilterIds=None):
		"""Adds a child instance of Layer23ProtocolAuthAccessFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter.Layer23ProtocolAuthAccessFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter import Layer23ProtocolAuthAccessFilter
		return self._create(Layer23ProtocolAuthAccessFilter(self), locals())

	def Layer23ProtocolPortFilter(self):
		"""Gets child instances of Layer23ProtocolPortFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23ProtocolPortFilter will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter.Layer23ProtocolPortFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter import Layer23ProtocolPortFilter
		return self._select(Layer23ProtocolPortFilter(self), locals())

	def add_Layer23ProtocolPortFilter(self, PortFilterIds=None):
		"""Adds a child instance of Layer23ProtocolPortFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter.Layer23ProtocolPortFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter import Layer23ProtocolPortFilter
		return self._create(Layer23ProtocolPortFilter(self), locals())

	def Layer23ProtocolRoutingFilter(self):
		"""Gets child instances of Layer23ProtocolRoutingFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23ProtocolRoutingFilter will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter.Layer23ProtocolRoutingFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter import Layer23ProtocolRoutingFilter
		return self._select(Layer23ProtocolRoutingFilter(self), locals())

	def add_Layer23ProtocolRoutingFilter(self, PortFilterIds=None, ProtocolFilterIds=None):
		"""Adds a child instance of Layer23ProtocolRoutingFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter.Layer23ProtocolRoutingFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter import Layer23ProtocolRoutingFilter
		return self._create(Layer23ProtocolRoutingFilter(self), locals())

	def Layer23ProtocolStackFilter(self, DrilldownType=None, NumberOfResults=None, SortAscending=None, SortingStatistic=None):
		"""Gets child instances of Layer23ProtocolStackFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23ProtocolStackFilter will be returned.

		Args:
			DrilldownType (str(perRange|perSession)): 
			NumberOfResults (number): 
			SortAscending (bool): 
			SortingStatistic (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=statistic)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter.Layer23ProtocolStackFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter import Layer23ProtocolStackFilter
		return self._select(Layer23ProtocolStackFilter(self), locals())

	def add_Layer23ProtocolStackFilter(self, DrilldownType=None, NumberOfResults=None, ProtocolStackFilterId=None, SortAscending=None, SortingStatistic=None):
		"""Adds a child instance of Layer23ProtocolStackFilter on the server.

		Args:
			DrilldownType (str(perRange|perSession)): 
			NumberOfResults (number): 
			ProtocolStackFilterId (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolStackFilter])): 
			SortAscending (bool): 
			SortingStatistic (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=statistic)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter.Layer23ProtocolStackFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter import Layer23ProtocolStackFilter
		return self._create(Layer23ProtocolStackFilter(self), locals())

	def Layer23TrafficFlowDetectiveFilter(self, DeadFlowsCount=None, DeadFlowsThreshold=None, FlowFilterType=None, ShowEgressFlows=None, TrafficItemFilterId=None):
		"""Gets child instances of Layer23TrafficFlowDetectiveFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23TrafficFlowDetectiveFilter will be returned.

		Args:
			DeadFlowsCount (number): 
			DeadFlowsThreshold (number): 
			FlowFilterType (str(allFlows|deadFlows|liveFlows)): 
			ShowEgressFlows (bool): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter.Layer23TrafficFlowDetectiveFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter import Layer23TrafficFlowDetectiveFilter
		return self._select(Layer23TrafficFlowDetectiveFilter(self), locals())

	def add_Layer23TrafficFlowDetectiveFilter(self, DeadFlowsThreshold=None, FlowFilterType=None, PortFilterIds=None, ShowEgressFlows=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
		"""Adds a child instance of Layer23TrafficFlowDetectiveFilter on the server.

		Args:
			DeadFlowsThreshold (number): 
			FlowFilterType (str(allFlows|deadFlows|liveFlows)): 
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			ShowEgressFlows (bool): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 
			TrafficItemFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter.Layer23TrafficFlowDetectiveFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter import Layer23TrafficFlowDetectiveFilter
		return self._create(Layer23TrafficFlowDetectiveFilter(self), locals())

	def Layer23TrafficFlowFilter(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, TrafficItemFilterId=None):
		"""Gets child instances of Layer23TrafficFlowFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23TrafficFlowFilter will be returned.

		Args:
			AggregatedAcrossPorts (bool): 
			EgressLatencyBinDisplayOption (str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter.Layer23TrafficFlowFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter import Layer23TrafficFlowFilter
		return self._select(Layer23TrafficFlowFilter(self), locals())

	def add_Layer23TrafficFlowFilter(self, AggregatedAcrossPorts=None, EgressLatencyBinDisplayOption=None, PortFilterIds=None, TrafficItemFilterId=None, TrafficItemFilterIds=None):
		"""Adds a child instance of Layer23TrafficFlowFilter on the server.

		Args:
			AggregatedAcrossPorts (bool): 
			EgressLatencyBinDisplayOption (str(none|showEgressFlatView|showEgressRows|showLatencyBinStats)): 
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 
			TrafficItemFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter)): 
			TrafficItemFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter.Layer23TrafficFlowFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter import Layer23TrafficFlowFilter
		return self._create(Layer23TrafficFlowFilter(self), locals())

	def Layer23TrafficItemFilter(self):
		"""Gets child instances of Layer23TrafficItemFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23TrafficItemFilter will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter.Layer23TrafficItemFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter import Layer23TrafficItemFilter
		return self._select(Layer23TrafficItemFilter(self), locals())

	def add_Layer23TrafficItemFilter(self, TrafficItemFilterIds=None):
		"""Adds a child instance of Layer23TrafficItemFilter on the server.

		Args:
			TrafficItemFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrafficItemFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter.Layer23TrafficItemFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter import Layer23TrafficItemFilter
		return self._create(Layer23TrafficItemFilter(self), locals())

	def Layer23TrafficPortFilter(self):
		"""Gets child instances of Layer23TrafficPortFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer23TrafficPortFilter will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter.Layer23TrafficPortFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter import Layer23TrafficPortFilter
		return self._select(Layer23TrafficPortFilter(self), locals())

	def add_Layer23TrafficPortFilter(self, PortFilterIds=None):
		"""Adds a child instance of Layer23TrafficPortFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter.Layer23TrafficPortFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter import Layer23TrafficPortFilter
		return self._create(Layer23TrafficPortFilter(self), locals())

	def Layer47AppLibraryTrafficFilter(self, AdvancedFilterName=None, AllAdvancedFilters=None, MatchingAdvancedFilters=None, TopxEnabled=None, TopxValue=None):
		"""Gets child instances of Layer47AppLibraryTrafficFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Layer47AppLibraryTrafficFilter will be returned.

		Args:
			AdvancedFilterName (str): 
			AllAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 
			MatchingAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 
			TopxEnabled (bool): 
			TopxValue (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter.Layer47AppLibraryTrafficFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter import Layer47AppLibraryTrafficFilter
		return self._select(Layer47AppLibraryTrafficFilter(self), locals())

	def add_Layer47AppLibraryTrafficFilter(self, AdvancedFilterName=None, TopxEnabled=None, TopxValue=None):
		"""Adds a child instance of Layer47AppLibraryTrafficFilter on the server.

		Args:
			AdvancedFilterName (str): 
			TopxEnabled (bool): 
			TopxValue (number): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter.Layer47AppLibraryTrafficFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter import Layer47AppLibraryTrafficFilter
		return self._create(Layer47AppLibraryTrafficFilter(self), locals())

	@property
	def Page(self):
		"""Returns the one and only one Page object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.page.Page)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.page import Page
		return self._read(Page(self), None)

	def Statistic(self, AggregationType=None, Caption=None, DefaultCaption=None, Enabled=None, ScaleFactor=None):
		"""Gets child instances of Statistic from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Statistic will be returned.

		Args:
			AggregationType (str(average|averageRate|ax|axRate|intervalAverage|min|minRate|none|rate|runStateAgg|runStateAggIgnoreRamp|sum|vectorMax|vectorMin|weightedAverage)): 
			Caption (str): 
			DefaultCaption (str): 
			Enabled (bool): 
			ScaleFactor (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.statistic.statistic.Statistic))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.statistic.statistic import Statistic
		return self._select(Statistic(self), locals())

	@property
	def AutoRefresh(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('autoRefresh')
	@AutoRefresh.setter
	def AutoRefresh(self, value):
		self._set_attribute('autoRefresh', value)

	@property
	def AutoUpdate(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('autoUpdate')
	@AutoUpdate.setter
	def AutoUpdate(self, value):
		self._set_attribute('autoUpdate', value)

	@property
	def AvailableStatsSelectorColumns(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('availableStatsSelectorColumns')

	@property
	def Caption(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('caption')
	@Caption.setter
	def Caption(self, value):
		self._set_attribute('caption', value)

	@property
	def CsvFileName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('csvFileName')
	@CsvFileName.setter
	def CsvFileName(self, value):
		self._set_attribute('csvFileName', value)

	@property
	def EnableCsvLogging(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableCsvLogging')
	@EnableCsvLogging.setter
	def EnableCsvLogging(self, value):
		self._set_attribute('enableCsvLogging', value)

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
	def EnabledStatsSelectorColumns(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('enabledStatsSelectorColumns')
	@EnabledStatsSelectorColumns.setter
	def EnabledStatsSelectorColumns(self, value):
		self._set_attribute('enabledStatsSelectorColumns', value)

	@property
	def PageTimeout(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('pageTimeout')
	@PageTimeout.setter
	def PageTimeout(self, value):
		self._set_attribute('pageTimeout', value)

	@property
	def ReadOnly(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('readOnly')

	@property
	def TimeSeries(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('timeSeries')
	@TimeSeries.setter
	def TimeSeries(self, value):
		self._set_attribute('timeSeries', value)

	@property
	def TreeViewNodeName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('treeViewNodeName')
	@TreeViewNodeName.setter
	def TreeViewNodeName(self, value):
		self._set_attribute('treeViewNodeName', value)

	@property
	def Type(self):
		"""

		Returns:
			str(layer23NextGenProtocol|layer23ProtocolAuthAccess|layer23ProtocolPort|layer23ProtocolRouting|layer23ProtocolStack|layer23TrafficFlow|layer23TrafficFlowDetective|layer23TrafficItem|layer23TrafficPort|layer47AppLibraryTraffic|sVReadOnly)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def TypeDescription(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('typeDescription')

	@property
	def ViewCategory(self):
		"""

		Returns:
			str(ClassicProtocol|L23Traffic|L47Traffic|Mixed|NextGenProtocol|PerSession|Unknown)
		"""
		return self._get_attribute('viewCategory')

	@property
	def Visible(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('visible')
	@Visible.setter
	def Visible(self, value):
		self._set_attribute('visible', value)

	def remove(self):
		"""Deletes a child instance of View on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def ExportData(self, FilePathName):
		"""Executes the exportData operation on the server.

		Args:
			FilePathName (str): 

		Returns:
			str: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('exportData', payload=locals(), response_object=None)

	def GetColumnValues(self, Arg2):
		"""Executes the getColumnValues operation on the server.

		Args:
			Arg2 (str): 

		Returns:
			dict(arg1:list[str],arg2:str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getColumnValues', payload=locals(), response_object=None)

	def GetResultsPath(self):
		"""Executes the getResultsPath operation on the server.

		Returns:
			str: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getResultsPath', payload=locals(), response_object=None)

	def GetRowValues(self, Arg2):
		"""Executes the getRowValues operation on the server.

		Args:
			Arg2 (str): 

		Returns:
			dict(arg1:list[str],arg2:str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getRowValues', payload=locals(), response_object=None)

	def GetValue(self, Arg2, Arg3):
		"""Executes the getValue operation on the server.

		Args:
			Arg2 (str): 
			Arg3 (str): 

		Returns:
			str: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getValue', payload=locals(), response_object=None)

	def Refresh(self):
		"""Executes the refresh operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('refresh', payload=locals(), response_object=None)

	def RestoreToDefaults(self):
		"""Executes the restoreToDefaults operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('restoreToDefaults', payload=locals(), response_object=None)
