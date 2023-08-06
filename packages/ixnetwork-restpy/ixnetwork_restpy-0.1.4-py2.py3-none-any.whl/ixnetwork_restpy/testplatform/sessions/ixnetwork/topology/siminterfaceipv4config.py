from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SimInterfaceIPv4Config(Base):
	"""Data associated with simulated IPv4 interface link configuration inside a Network Topology.
	"""

	_SDM_NAME = 'simInterfaceIPv4Config'

	def __init__(self, parent):
		super(SimInterfaceIPv4Config, self).__init__(parent)

	def OspfPseudoInterface(self, AdjSID=None, AdministratorGroup=None, BFlag=None, BandwidthPriority0=None, BandwidthPriority1=None, BandwidthPriority2=None, BandwidthPriority3=None, BandwidthPriority4=None, BandwidthPriority5=None, BandwidthPriority6=None, BandwidthPriority7=None, Count=None, Dedicated1Plus1=None, Dedicated1To1=None, DescriptiveName=None, EnLinkProtection=None, Enable=None, EnableAdjSID=None, EnableSRLG=None, Enhanced=None, ExtraTraffic=None, LFlag=None, MaxBandwidth=None, MaxReservableBandwidth=None, Metric=None, MetricLevel=None, Name=None, Reserved40=None, Reserved80=None, SFlag=None, Shared=None, SrlgCount=None, Unprotected=None, VFlag=None, Weight=None):
		"""Gets child instances of OspfPseudoInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OspfPseudoInterface will be returned.

		Args:
			AdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Adjacency SID
			AdministratorGroup (obj(ixnetwork_restpy.multivalue.Multivalue)): Administrator Group
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Backup Flag
			BandwidthPriority0 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 0 (B/sec)
			BandwidthPriority1 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 1 (B/sec)
			BandwidthPriority2 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 2 (B/sec)
			BandwidthPriority3 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 3 (B/sec)
			BandwidthPriority4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 4 (B/sec)
			BandwidthPriority5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 5 (B/sec)
			BandwidthPriority6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 6 (B/sec)
			BandwidthPriority7 (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 7 (B/sec)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Dedicated1Plus1 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
			Dedicated1To1 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnLinkProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the link protection on the OSPF link between two mentioned interfaces.
			Enable (obj(ixnetwork_restpy.multivalue.Multivalue)): TEEnabled
			EnableAdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Adj SID
			EnableSRLG (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the SRLG on the OSPF link between two mentioned interfaces.
			Enhanced (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
			ExtraTraffic (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local/Global Flag
			MaxBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Bandwidth (B/sec)
			MaxReservableBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Reservable Bandwidth (B/sec)
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			MetricLevel (obj(ixnetwork_restpy.multivalue.Multivalue)): TE Metric Level
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Reserved40 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x40.
			Reserved80 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x80.
			SFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set Flag
			Shared (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			Unprotected (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value/Index Flag
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudointerface.OspfPseudoInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudointerface import OspfPseudoInterface
		return self._select(OspfPseudoInterface(self), locals())

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableIp(self):
		"""Enable IPv4

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableIp')

	@property
	def FromIP(self):
		"""4 Byte IP address in dotted decimal format.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fromIP')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def SubnetPrefixLength(self):
		"""Subnet Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('subnetPrefixLength')

	@property
	def ToIP(self):
		"""4 Byte IP address in dotted decimal format.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('toIP')

	def FetchAndUpdateConfigFromCloud(self, Mode):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		Args:
			Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('fetchAndUpdateConfigFromCloud', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simInterfaceIPv4Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simInterfaceIPv4Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
