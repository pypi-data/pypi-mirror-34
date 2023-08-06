from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Layer47AppLibraryTrafficFilter(Base):
	"""
	"""

	_SDM_NAME = 'layer47AppLibraryTrafficFilter'

	def __init__(self, parent):
		super(Layer47AppLibraryTrafficFilter, self).__init__(parent)

	def AdvancedFilter(self, Expression=None, Name=None, SortingStats=None, TrackingFilterId=None):
		"""Gets child instances of AdvancedFilter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of AdvancedFilter will be returned.

		Args:
			Expression (str): 
			Name (str): 
			SortingStats (str): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter.AdvancedFilter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter import AdvancedFilter
		return self._select(AdvancedFilter(self), locals())

	def add_AdvancedFilter(self, Expression=None, Name=None, SortingStats=None, TrackingFilterId=None):
		"""Adds a child instance of AdvancedFilter on the server.

		Args:
			Expression (str): 
			Name (str): 
			SortingStats (str): 
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter.AdvancedFilter)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter import AdvancedFilter
		return self._create(AdvancedFilter(self), locals())

	@property
	def AdvancedFilterName(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('advancedFilterName')
	@AdvancedFilterName.setter
	def AdvancedFilterName(self, value):
		self._set_attribute('advancedFilterName', value)

	@property
	def AllAdvancedFilters(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)
		"""
		return self._get_attribute('allAdvancedFilters')

	@property
	def MatchingAdvancedFilters(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)
		"""
		return self._get_attribute('matchingAdvancedFilters')

	@property
	def TopxEnabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('topxEnabled')
	@TopxEnabled.setter
	def TopxEnabled(self, value):
		self._set_attribute('topxEnabled', value)

	@property
	def TopxValue(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('topxValue')
	@TopxValue.setter
	def TopxValue(self, value):
		self._set_attribute('topxValue', value)

	def remove(self):
		"""Deletes a child instance of Layer47AppLibraryTrafficFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def AddAdvancedFilter(self, Arg2):
		"""Executes the addAdvancedFilter operation on the server.

		Args:
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('addAdvancedFilter', payload=locals(), response_object=None)

	def RemoveAdvancedFilter(self, Arg2):
		"""Executes the removeAdvancedFilter operation on the server.

		Args:
			Arg2 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('removeAdvancedFilter', payload=locals(), response_object=None)

	def RemoveAllAdvancedFilters(self):
		"""Executes the removeAllAdvancedFilters operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('removeAllAdvancedFilters', payload=locals(), response_object=None)
