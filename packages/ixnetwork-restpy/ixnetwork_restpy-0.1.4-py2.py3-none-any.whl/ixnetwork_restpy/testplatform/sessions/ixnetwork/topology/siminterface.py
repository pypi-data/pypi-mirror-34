from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SimInterface(Base):
	"""Simulated Interface specific configuration inside a Network Topology
	"""

	_SDM_NAME = 'simInterface'

	def __init__(self, parent):
		super(SimInterface, self).__init__(parent)

	def IsisL3PseudoInterface(self, AdjSID=None, AdministratorGroup=None, BFlag=None, BandwidthPriority0_Bps=None, BandwidthPriority1_Bps=None, BandwidthPriority2_Bps=None, BandwidthPriority3_Bps=None, BandwidthPriority4_Bps=None, BandwidthPriority5_Bps=None, BandwidthPriority6_Bps=None, BandwidthPriority7_Bps=None, Count=None, DedicatedOnePlusOne=None, DedicatedOneToOne=None, DescriptiveName=None, EnableAdjSID=None, EnableIPv6SID=None, EnableLinkProtection=None, EnableSRLG=None, Enhanced=None, ExtraTraffic=None, FFlag=None, Funcflags=None, Function=None, Ipv6SidValue=None, LFlag=None, LinkType=None, MaxBandwidth_Bps=None, MaxReservableBandwidth_Bps=None, MetricLevel=None, Name=None, OverrideFFlag=None, PFlag=None, Reserved0x40=None, Reserved0x80=None, SFlag=None, Shared=None, SrlgCount=None, Srv6SidFlags=None, Unprotected=None, VFlag=None, Weight=None):
		"""Gets child instances of IsisL3PseudoInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3PseudoInterface will be returned.

		Args:
			AdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): AdjSID
			AdministratorGroup (obj(ixnetwork_restpy.multivalue.Multivalue)): Administrator Group
			BFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Backup Flag, if set, the Adj-SID is eligible for protection
			BandwidthPriority0_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 0 (B/sec)
			BandwidthPriority1_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 1 (B/sec)
			BandwidthPriority2_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 2 (B/sec)
			BandwidthPriority3_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 3 (B/sec)
			BandwidthPriority4_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 4 (B/sec)
			BandwidthPriority5_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 5 (B/sec)
			BandwidthPriority6_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 6 (B/sec)
			BandwidthPriority7_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth for Priority 7 (B/sec)
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DedicatedOnePlusOne (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.
			DedicatedOneToOne (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableAdjSID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Adj SID
			EnableIPv6SID (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6 SID
			EnableLinkProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the link protection on the ISIS link between two mentioned interfaces.
			EnableSRLG (obj(ixnetwork_restpy.multivalue.Multivalue)): This enables the SRLG on the ISIS link between two mentioned interfaces.
			Enhanced (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.
			ExtraTraffic (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.
			FFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation
			Funcflags (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the function flags
			Function (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies endpoint function codes
			Ipv6SidValue (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Adj SID
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Flag, if set, then the value/index carried by the Adj-SID has local significance
			LinkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Type
			MaxBandwidth_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Bandwidth (B/sec)
			MaxReservableBandwidth_Bps (obj(ixnetwork_restpy.multivalue.Multivalue)): Maximum Reservable Bandwidth (B/sec)
			MetricLevel (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric Level
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OverrideFFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.
			PFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.
			Reserved0x40 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x40.
			Reserved0x80 (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x80.
			SFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies
			Shared (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.
			SrlgCount (number): This field value shows how many SRLG Value columns would be there in the GUI.
			Srv6SidFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies the value of the SRv6 SID Flags
			Unprotected (obj(ixnetwork_restpy.multivalue.Multivalue)): This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value Flag, if set, the Adjacency SID carries a value
			Weight (obj(ixnetwork_restpy.multivalue.Multivalue)): Weight

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface.IsisL3PseudoInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface import IsisL3PseudoInterface
		return self._select(IsisL3PseudoInterface(self), locals())

	def IsisPseudoInterface(self, Count=None, DescriptiveName=None, LinkType=None, Name=None):
		"""Gets child instances of IsisPseudoInterface from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisPseudoInterface will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkType (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Type
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface.IsisPseudoInterface))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface import IsisPseudoInterface
		return self._select(IsisPseudoInterface(self), locals())

	def SimInterfaceEthernetConfig(self, Count=None, DescriptiveName=None, FromMac=None, Name=None, ToMac=None, VlanCount=None):
		"""Gets child instances of SimInterfaceEthernetConfig from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of SimInterfaceEthernetConfig will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			FromMac (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC address of endpoing-1
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			ToMac (obj(ixnetwork_restpy.multivalue.Multivalue)): MAC address of endpoing-2
			VlanCount (obj(ixnetwork_restpy.multivalue.Multivalue)): number of active VLANs

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig.SimInterfaceEthernetConfig))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig import SimInterfaceEthernetConfig
		return self._select(SimInterfaceEthernetConfig(self), locals())

	def SimInterfaceIPv4Config(self, Count=None, DescriptiveName=None, EnableIp=None, FromIP=None, Name=None, SubnetPrefixLength=None, ToIP=None):
		"""Gets child instances of SimInterfaceIPv4Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of SimInterfaceIPv4Config will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv4
			FromIP (obj(ixnetwork_restpy.multivalue.Multivalue)): 4 Byte IP address in dotted decimal format.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SubnetPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Subnet Prefix Length
			ToIP (obj(ixnetwork_restpy.multivalue.Multivalue)): 4 Byte IP address in dotted decimal format.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config.SimInterfaceIPv4Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config import SimInterfaceIPv4Config
		return self._select(SimInterfaceIPv4Config(self), locals())

	def SimInterfaceIPv6Config(self, Count=None, DescriptiveName=None, EnableIp=None, FromIP=None, Name=None, SubnetPrefixLength=None, ToIP=None):
		"""Gets child instances of SimInterfaceIPv6Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of SimInterfaceIPv6Config will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableIp (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable IPv6
			FromIP (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 Bits IPv6 address.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SubnetPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Subnet Prefix Length
			ToIP (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 Bits IPv6 address.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config.SimInterfaceIPv6Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config import SimInterfaceIPv6Config
		return self._select(SimInterfaceIPv6Config(self), locals())

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
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

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
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simInterface object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simInterface object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
