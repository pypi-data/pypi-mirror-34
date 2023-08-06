from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TrackingFilter(Base):
	"""
	"""

	_SDM_NAME = 'trackingFilter'

	def __init__(self, parent):
		super(TrackingFilter, self).__init__(parent)

	@property
	def Operator(self):
		"""

		Returns:
			str(isAnyOf|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isInAnyRange|isNoneOf|isSmaller)
		"""
		return self._get_attribute('operator')
	@Operator.setter
	def Operator(self, value):
		self._set_attribute('operator', value)

	@property
	def TrackingFilterId(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)
		"""
		return self._get_attribute('trackingFilterId')
	@TrackingFilterId.setter
	def TrackingFilterId(self, value):
		self._set_attribute('trackingFilterId', value)

	@property
	def Value(self):
		"""

		Returns:
			list(str)
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def remove(self):
		"""Deletes a child instance of TrackingFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
