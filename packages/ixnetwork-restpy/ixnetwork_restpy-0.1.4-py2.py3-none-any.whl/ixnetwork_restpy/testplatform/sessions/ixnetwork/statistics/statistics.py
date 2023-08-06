from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Statistics(Base):
	"""
	"""

	_SDM_NAME = 'statistics'

	def __init__(self, parent):
		super(Statistics, self).__init__(parent)

	@property
	def AutoRefresh(self):
		"""Returns the one and only one AutoRefresh object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh.AutoRefresh)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.autorefresh.autorefresh import AutoRefresh
		return self._read(AutoRefresh(self), None)

	@property
	def CsvSnapshot(self):
		"""Returns the one and only one CsvSnapshot object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot.CsvSnapshot)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.csvsnapshot.csvsnapshot import CsvSnapshot
		return self._read(CsvSnapshot(self), None)

	@property
	def Ixreporter(self):
		"""Returns the one and only one Ixreporter object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter.Ixreporter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.ixreporter import Ixreporter
		return self._read(Ixreporter(self), None)

	@property
	def MeasurementMode(self):
		"""Returns the one and only one MeasurementMode object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode.MeasurementMode)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.measurementmode.measurementmode import MeasurementMode
		return self._read(MeasurementMode(self), None)

	@property
	def RawData(self):
		"""Returns the one and only one RawData object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata.RawData)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.rawdata import RawData
		return self._read(RawData(self), None)

	def StatRequest(self, Filter=None, IsReady=None, MaxWaitTime=None, Source=None):
		"""Gets child instances of StatRequest from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of StatRequest will be returned.

		Args:
			Filter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			IsReady (bool): 
			MaxWaitTime (number): 
			Source (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.statrequest.StatRequest))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.statrequest import StatRequest
		return self._select(StatRequest(self), locals())

	def add_StatRequest(self, Filter=None, FilterItems=None, MaxWaitTime=None, Source=None, Stats=None):
		"""Adds a child instance of StatRequest on the server.

		Args:
			Filter (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			FilterItems (list(str[None|/api/v1/sessions/1/ixnetwork/vport?deepchild=*])): 
			MaxWaitTime (number): 
			Source (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*)): 
			Stats (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=*],arg2:str[average|averageRate|countDistinct|delta|divSum|first|intervalAverage|max|maxRate|min|minRate|none|positiveAverageRate|positiveMaxRate|positiveMinRate|positiveRate|rate|runStateAgg|runStateAggIgnoreRamp|standardDeviation|sum|vectorMax|vectorMin|weightedAverage]))): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.statrequest.StatRequest)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statrequest.statrequest import StatRequest
		return self._create(StatRequest(self), locals())

	def View(self, AutoRefresh=None, AutoUpdate=None, Caption=None, CsvFileName=None, EnableCsvLogging=None, Enabled=None, PageTimeout=None, ReadOnly=None, TimeSeries=None, TreeViewNodeName=None, Type=None, TypeDescription=None, ViewCategory=None, Visible=None):
		"""Gets child instances of View from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of View will be returned.

		Args:
			AutoRefresh (bool): 
			AutoUpdate (bool): 
			Caption (str): 
			CsvFileName (str): 
			EnableCsvLogging (bool): 
			Enabled (bool): 
			PageTimeout (number): 
			ReadOnly (bool): 
			TimeSeries (bool): 
			TreeViewNodeName (str): 
			Type (str(layer23NextGenProtocol|layer23ProtocolAuthAccess|layer23ProtocolPort|layer23ProtocolRouting|layer23ProtocolStack|layer23TrafficFlow|layer23TrafficFlowDetective|layer23TrafficItem|layer23TrafficPort|layer47AppLibraryTraffic|sVReadOnly)): 
			TypeDescription (str): 
			ViewCategory (str(ClassicProtocol|L23Traffic|L47Traffic|Mixed|NextGenProtocol|PerSession|Unknown)): 
			Visible (bool): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view.View))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view import View
		return self._select(View(self), locals())

	def add_View(self, AutoRefresh=None, AutoUpdate=None, Caption=None, CsvFileName="", EnableCsvLogging="False", Enabled=None, EnabledStatsSelectorColumns=None, PageTimeout=None, TimeSeries=None, TreeViewNodeName=None, Type=None, Visible=None):
		"""Adds a child instance of View on the server.

		Args:
			AutoRefresh (bool): 
			AutoUpdate (bool): 
			Caption (str): 
			CsvFileName (str): 
			EnableCsvLogging (bool): 
			Enabled (bool): 
			EnabledStatsSelectorColumns (list(str)): 
			PageTimeout (number): 
			TimeSeries (bool): 
			TreeViewNodeName (str): 
			Type (str(layer23NextGenProtocol|layer23ProtocolAuthAccess|layer23ProtocolPort|layer23ProtocolRouting|layer23ProtocolStack|layer23TrafficFlow|layer23TrafficFlowDetective|layer23TrafficItem|layer23TrafficPort|layer47AppLibraryTraffic|sVReadOnly)): 
			Visible (bool): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view.View)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.view import View
		return self._create(View(self), locals())

	@property
	def AdditionalFcoeStat1(self):
		"""

		Returns:
			str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)
		"""
		return self._get_attribute('additionalFcoeStat1')
	@AdditionalFcoeStat1.setter
	def AdditionalFcoeStat1(self, value):
		self._set_attribute('additionalFcoeStat1', value)

	@property
	def AdditionalFcoeStat2(self):
		"""

		Returns:
			str(fcoeInvalidDelimiter|fcoeInvalidFrames|fcoeInvalidSize|fcoeNormalSizeBadFcCRC|fcoeNormalSizeGoodFcCRC|fcoeUndersizeBadFcCRC|fcoeUndersizeGoodFcCRC|fcoeValidFrames)
		"""
		return self._get_attribute('additionalFcoeStat2')
	@AdditionalFcoeStat2.setter
	def AdditionalFcoeStat2(self, value):
		self._set_attribute('additionalFcoeStat2', value)

	@property
	def CsvFilePath(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('csvFilePath')
	@CsvFilePath.setter
	def CsvFilePath(self, value):
		self._set_attribute('csvFilePath', value)

	@property
	def CsvLogPollIntervalMultiplier(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('csvLogPollIntervalMultiplier')
	@CsvLogPollIntervalMultiplier.setter
	def CsvLogPollIntervalMultiplier(self, value):
		self._set_attribute('csvLogPollIntervalMultiplier', value)

	@property
	def DataStorePollingIntervalMultiplier(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('dataStorePollingIntervalMultiplier')
	@DataStorePollingIntervalMultiplier.setter
	def DataStorePollingIntervalMultiplier(self, value):
		self._set_attribute('dataStorePollingIntervalMultiplier', value)

	@property
	def EnableAutoDataStore(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableAutoDataStore')
	@EnableAutoDataStore.setter
	def EnableAutoDataStore(self, value):
		self._set_attribute('enableAutoDataStore', value)

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
	def EnableDataCenterSharedStats(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enableDataCenterSharedStats')
	@EnableDataCenterSharedStats.setter
	def EnableDataCenterSharedStats(self, value):
		self._set_attribute('enableDataCenterSharedStats', value)

	@property
	def GuardrailEnabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('guardrailEnabled')
	@GuardrailEnabled.setter
	def GuardrailEnabled(self, value):
		self._set_attribute('guardrailEnabled', value)

	@property
	def MaxNumberOfStatsPerCustomGraph(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('maxNumberOfStatsPerCustomGraph')
	@MaxNumberOfStatsPerCustomGraph.setter
	def MaxNumberOfStatsPerCustomGraph(self, value):
		self._set_attribute('maxNumberOfStatsPerCustomGraph', value)

	@property
	def PollInterval(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('pollInterval')
	@PollInterval.setter
	def PollInterval(self, value):
		self._set_attribute('pollInterval', value)

	@property
	def TimeSynchronization(self):
		"""

		Returns:
			str(syncTimeToSystemClock|syncTimeToTestStart)
		"""
		return self._get_attribute('timeSynchronization')
	@TimeSynchronization.setter
	def TimeSynchronization(self, value):
		self._set_attribute('timeSynchronization', value)

	@property
	def TimestampPrecision(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('timestampPrecision')
	@TimestampPrecision.setter
	def TimestampPrecision(self, value):
		self._set_attribute('timestampPrecision', value)

	@property
	def UgsTcpPort(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ugsTcpPort')

	def CheckViewTreeGroupExists(self, Arg2):
		"""Executes the checkViewTreeGroupExists operation on the server.

		Args:
			Arg2 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('checkViewTreeGroupExists', payload=locals(), response_object=None)

	def DockStatViewer(self):
		"""Executes the dockStatViewer operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('dockStatViewer', payload=locals(), response_object=None)

	def GetPGIDList(self, Arg2, Arg3):
		"""Executes the getPGIDList operation on the server.

		Args:
			Arg2 (str): 
			Arg3 (str): 

		Returns:
			list(str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getPGIDList', payload=locals(), response_object=None)

	def GetStatsFooters(self, Arg2, Arg3, Arg4):
		"""Executes the getStatsFooters operation on the server.

		Args:
			Arg2 (str): 
			Arg3 (str): 
			Arg4 (str): 

		Returns:
			str: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('getStatsFooters', payload=locals(), response_object=None)
