from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ospfv3PseudoRouter(Base):
	"""Simulated Router Information
	"""

	_SDM_NAME = 'ospfv3PseudoRouter'

	def __init__(self, parent):
		super(Ospfv3PseudoRouter, self).__init__(parent)

	def ExternalRoutes(self, Active=None, Count=None, DescriptiveName=None, EBit=None, ExternalRouteTag=None, FBit=None, ForwardingAddress=None, LABit=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NUBit=None, Name=None, NetworkAddress=None, PBit=None, Prefix=None, RangeSize=None, RefLSType=None, ReferencedLinkStateId=None, TBit=None, UnusedBit4=None, UnusedBit5=None, UnusedBit6=None, UnusedBit7=None):
		"""Gets child instances of ExternalRoutes from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of ExternalRoutes will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): External Metric Bit
			ExternalRouteTag (obj(ixnetwork_restpy.multivalue.Multivalue)): External Route Tag
			FBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Forwarding Address Bit
			ForwardingAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 Bits IPv6 address.
			LABit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-LA Bit(Local Address)
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id of the simulated IPv6 network
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.
			MCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-MC Bit(Multicast)
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			NUBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-NU Bit(No Unicast)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefixes of the simulated IPv6 network
			PBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-P Bit(Propagate)
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Range Size
			RefLSType (obj(ixnetwork_restpy.multivalue.Multivalue)): Reference LS Type
			ReferencedLinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Referenced Link State Id
			TBit (obj(ixnetwork_restpy.multivalue.Multivalue)): External Route Tag Bit
			UnusedBit4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(4)Unused
			UnusedBit5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(5)Unused
			UnusedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(6)Unused
			UnusedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(7)Unused

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes.ExternalRoutes))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes import ExternalRoutes
		return self._select(ExternalRoutes(self), locals())

	def InterAreaPrefix(self, Active=None, Count=None, DescriptiveName=None, LABit=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NUBit=None, Name=None, NetworkAddress=None, PBit=None, Prefix=None, RangeSize=None, UnusedBit4=None, UnusedBit5=None, UnusedBit6=None, UnusedBit7=None):
		"""Gets child instances of InterAreaPrefix from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of InterAreaPrefix will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LABit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-LA Bit(Local Address)
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id of the simulated IPv6 network
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.
			MCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-MC Bit(Multicast)
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			NUBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-NU Bit(No Unicast)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefixes of the simulated IPv6 network
			PBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-P Bit(Propagate)
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Range Size
			UnusedBit4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(4)Unused
			UnusedBit5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(5)Unused
			UnusedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(6)Unused
			UnusedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(7)Unused

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix.InterAreaPrefix))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix import InterAreaPrefix
		return self._select(InterAreaPrefix(self), locals())

	def InterAreaRouter(self, Active=None, Count=None, DCBit=None, DescriptiveName=None, DestRouterId=None, DestRouterIdPrefix=None, EBit=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NBit=None, Name=None, RBit=None, RangeSize=None, ReservedBit6=None, ReservedBit7=None, V6Bit=None):
		"""Gets child instances of InterAreaRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of InterAreaRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Demand Circuit bit
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			DestRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination Router Id
			DestRouterIdPrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Destination Router Id Step
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit describing how AS-external-LSAs are flooded
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id of the simulated IPv6 network
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.
			MCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for forwarding of IP multicast datagrams
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			NBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for handling Type 7 LSAs
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			RBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router bit
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Count
			ReservedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): (6) Reserved Bit
			ReservedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): (7) Reserved Bit
			V6Bit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for excluding the router/link from IPv6 routing calculations. If clear, router/link is excluded

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter.InterAreaRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter import InterAreaRouter
		return self._select(InterAreaRouter(self), locals())

	def IntraAreaPrefix(self, Active=None, Count=None, DescriptiveName=None, LABit=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NUBit=None, Name=None, NetworkAddress=None, PBit=None, Prefix=None, RangeSize=None, RefLSType=None, ReferencedLinkStateId=None, ReferencedRouterId=None, UnusedBit4=None, UnusedBit5=None, UnusedBit6=None, UnusedBit7=None):
		"""Gets child instances of IntraAreaPrefix from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IntraAreaPrefix will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LABit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-LA Bit(Local Address)
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id of the simulated IPv6 network
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.
			MCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-MC Bit(Multicast)
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			NUBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-NU Bit(No Unicast)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefixes of the simulated IPv6 network
			PBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-P Bit(Propagate)
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Range Size
			RefLSType (obj(ixnetwork_restpy.multivalue.Multivalue)): Reference LS Type
			ReferencedLinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Referenced Link State Id
			ReferencedRouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Referenced Advertising Router Id
			UnusedBit4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(4)Unused
			UnusedBit5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(5)Unused
			UnusedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(6)Unused
			UnusedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(7)Unused

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix.IntraAreaPrefix))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix import IntraAreaPrefix
		return self._select(IntraAreaPrefix(self), locals())

	def LinkLsaRoutes(self, Active=None, Count=None, DCBit=None, DescriptiveName=None, EBit=None, LABit=None, LinkLocalAddress=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NBit=None, NUBit=None, Name=None, NetworkAddress=None, PBit=None, Prefix=None, RBit=None, RangeSize=None, ReservedBit6=None, ReservedBit7=None, RouterPriority=None, UnusedBit4=None, UnusedBit5=None, UnusedBit6=None, UnusedBit7=None, V6Bit=None, XBit=None):
		"""Gets child instances of LinkLsaRoutes from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LinkLsaRoutes will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Demand Circuit bit
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit describing how AS-external-LSAs are flooded
			LABit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-LA Bit(Local Address)
			LinkLocalAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 Bits IPv6 address.
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id of the simulated IPv6 network
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.
			MCBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-MC Bit(Multicast)
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			NBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for handling Type 7 LSAs
			NUBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-NU Bit(No Unicast)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefixes of the simulated IPv6 network
			PBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-P Bit(Propagate)
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router bit
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Range Size
			ReservedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): (6) Reserved Bit
			ReservedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): (7) Reserved Bit
			RouterPriority (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Priority
			UnusedBit4 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(4)Unused
			UnusedBit5 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(5)Unused
			UnusedBit6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(6)Unused
			UnusedBit7 (obj(ixnetwork_restpy.multivalue.Multivalue)): Options-(7)Unused
			V6Bit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for excluding the router/link from IPv6 routing calculations. If clear, router/link is excluded
			XBit (obj(ixnetwork_restpy.multivalue.Multivalue)): bit for forwarding of IP multicast datagrams

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes.LinkLsaRoutes))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes import LinkLsaRoutes
		return self._select(LinkLsaRoutes(self), locals())

	def NssaRoutes(self, Active=None, Count=None, DescriptiveName=None, ForwardingAddress=None, IncludeForwardingAddress=None, LinkStateId=None, LinkStateIdStep=None, Metric=None, Name=None, NetworkAddress=None, Prefix=None, Propagate=None, RangeSize=None):
		"""Gets child instances of NssaRoutes from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of NssaRoutes will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Whether this is to be advertised or not
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			ForwardingAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Forwarding Address of IPv6 NSSA LSAs that will be generated due to this range.
			IncludeForwardingAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Include Forwarding Address
			LinkStateId (obj(ixnetwork_restpy.multivalue.Multivalue)): Start Link State Id for the LSAs to be generated for this set of IPv6 NSSA networks.
			LinkStateIdStep (obj(ixnetwork_restpy.multivalue.Multivalue)): Link State Id Step for the LSAs to be generated for this set of IPv6 NSSA networks.
			Metric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NetworkAddress (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefixes of the simulated IPv6 network
			Prefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			Propagate (obj(ixnetwork_restpy.multivalue.Multivalue)): Propagate
			RangeSize (obj(ixnetwork_restpy.multivalue.Multivalue)): Range Size

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes.NssaRoutes))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes import NssaRoutes
		return self._select(NssaRoutes(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def BBit(self):
		"""Router-LSA B-Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bBit')

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
	def EBit(self):
		"""Router-LSA E-Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eBit')

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
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def StartSimulatedRouter(self, Arg1):
		"""Executes the startSimulatedRouter operation on the server.

		Start Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startSimulatedRouter', payload=locals(), response_object=None)

	def StartSimulatedRouter(self, Arg1, SessionIndices):
		"""Executes the startSimulatedRouter operation on the server.

		Start Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startSimulatedRouter', payload=locals(), response_object=None)

	def StartSimulatedRouter(self, Arg1, SessionIndices):
		"""Executes the startSimulatedRouter operation on the server.

		Start Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startSimulatedRouter', payload=locals(), response_object=None)

	def StartSimulatedRouter(self, Arg2):
		"""Executes the startSimulatedRouter operation on the server.

		Shutdown OSPFv3 state machine on this simulated router.

		Args:
			Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('startSimulatedRouter', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def StopSimulatedRouter(self, Arg1):
		"""Executes the stopSimulatedRouter operation on the server.

		Stop Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopSimulatedRouter', payload=locals(), response_object=None)

	def StopSimulatedRouter(self, Arg1, SessionIndices):
		"""Executes the stopSimulatedRouter operation on the server.

		Stop Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopSimulatedRouter', payload=locals(), response_object=None)

	def StopSimulatedRouter(self, Arg1, SessionIndices):
		"""Executes the stopSimulatedRouter operation on the server.

		Stop Pseudo Router

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./ospfv3PseudoRouter object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopSimulatedRouter', payload=locals(), response_object=None)

	def StopSimulatedRouter(self, Arg2):
		"""Executes the stopSimulatedRouter operation on the server.

		Withdraws all the routes mentioned in this route range.

		Args:
			Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the network info.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stopSimulatedRouter', payload=locals(), response_object=None)
