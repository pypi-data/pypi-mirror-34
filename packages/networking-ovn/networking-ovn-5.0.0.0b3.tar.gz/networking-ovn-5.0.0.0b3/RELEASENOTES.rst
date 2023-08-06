==============
networking-ovn
==============

.. _networking-ovn_5.0.0.0b3:

5.0.0.0b3
=========

.. _networking-ovn_5.0.0.0b3_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/network-dns-domain-support-85dd1e20d9c432c6.yaml @ fb1b29e74ae7bfe30894fc0a0b840da697fecaee

- Networking-ovn was not supporting the network's dns_domain option.
  This is now supported during network's creation. Updating 'dns_domain'
  during network update is not completely supported. All the existing ports
  are not updated with the new network's dns_domain in OVN Northbound db.


.. _networking-ovn_5.0.0.0b2:

5.0.0.0b2
=========

.. _networking-ovn_5.0.0.0b2_Prelude:

Prelude
-------

.. releasenotes/notes/migration-from-ml2ovs-to-ovn-30ea4dea163d20c0.yaml @ 6546cb8ed94e32e72f1d6a1014338d08e1dbb463

Support migration from an existing ML2OVS tripleo deployment to ML2OVN tripleo deployment.


.. _networking-ovn_5.0.0.0b2_New Features:

New Features
------------

.. releasenotes/notes/migration-from-ml2ovs-to-ovn-30ea4dea163d20c0.yaml @ 6546cb8ed94e32e72f1d6a1014338d08e1dbb463

- A migration tool is provided to carry out in-place migration of an existing
  ML2OVS tripleo deployment to ML2OVN. Please see the relevant documentation
  section for more information.


.. _networking-ovn_5.0.0.0b2_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/ovsdb-probe-interval-to-60-secs-cb4d3c5ec930f4a8.yaml @ 90c2a1c26f5ec276a1154648538efd373e458afa

- The ovsdb_probe_interval configuration option was changed from
  0 (disabled) to 60 seconds.


.. _networking-ovn_5.0.0.0b2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/ovsdb-probe-interval-to-60-secs-cb4d3c5ec930f4a8.yaml @ 90c2a1c26f5ec276a1154648538efd373e458afa

- In a HA environment, when OVSDB server fails over to a different
  controller, the connection change is not detected by neither
  neutron-server nor ovn-metadata-agent. In order to fix this issue,
  a 60 seconds interval probe (by default) is now sent by OVSDB
  server clients.


.. _networking-ovn_4.0.0:

4.0.0
=====

.. _networking-ovn_4.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/SRIOV-port-binding-support-bug-1515005.yaml @ 621e3a4700564a0c493673b4086d158de5fde9d5

support for binding a SR-IOV port in a networking-ovn deployment.


.. releasenotes/notes/distributed-fip-0f5915ef9fd00626.yaml @ b123da3fb1386fcb7521ca8fff189e6d7f40ac87

Support distributed floating IP.


.. _networking-ovn_4.0.0_New Features:

New Features
------------

.. releasenotes/notes/SRIOV-port-binding-support-bug-1515005.yaml @ 621e3a4700564a0c493673b4086d158de5fde9d5

- networking-ovn ML2 mechanism driver now supports binding of direct(SR-IOV) ports. Traffic Control(TC) hardware offload framework for SR-IOV VFs was introduced in Linux kernel 4.8. Open vSwitch(OVS) 2.8 supports offloading OVS datapath rules using the TC framework. By using OVS version 2.8 and Linux kernel >= 4.8, a SR-IOV VF can be controlled via Openflow control plane.

.. releasenotes/notes/distributed-fip-0f5915ef9fd00626.yaml @ b123da3fb1386fcb7521ca8fff189e6d7f40ac87

- Now distributed floating IP is supported and a new configuration option
  ``enable_distributed_floating_ip`` is added to ovn group to control
  the feature.

.. releasenotes/notes/internal_dns_support-83737015a1019222.yaml @ d8d5eeababb1fdae83c1cc38d04cbc45c1a8c372

- Use native OVN DNS support if "dns" extension is loaded and "dns_domain"
  is defined.

.. releasenotes/notes/maintenance-thread-ee65c1ad317204c7.yaml @ cea18015408e52d93f056aeeb8b5aecd4b475e90

- Added a new mechanism that periodically detects and fix
  inconsistencies between resources in the Neutron and OVN database.

.. releasenotes/notes/ovn-cms-options-enable-chassis-as-gw-3adc7024478e3efa.yaml @ d265e93698eee81c1cae0c357883a8c06562acab

- New option "enable-chassis-as-gw" to select gateway router.
  For external connectivity, gateway nodes have to set ovn-cms-options
  with enable-chassis-as-gw in Open_vSwitch table's external_ids column.
  
  $ovs-vsctl set open . external-ids:ovn-cms-options="enable-chassis-as-gw"
  
  Networking-ovn will parse ovn-cms-options and select this chassis
  if it has proper bridge mappings. This helps admin to exclude compute
  nodes to host gateway routers as they are more likely to be restarted
  for maintenance operations. If no chassis with enable-chassis-as-gw and
  proper bridge mappings available, then chassis with only bridge mappings
  are selected for scheduling router gateway.
  
  This is not a config option enabled through conf files. Instead admin
  has to set it through openstack installer or manually in Open_vSwitch
  table.


.. _networking-ovn_4.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/maintenance-thread-ee65c1ad317204c7.yaml @ cea18015408e52d93f056aeeb8b5aecd4b475e90

- Adds a new dependency on the Oslo Futurist library.


.. _networking-ovn_3.0.0.0b1:

3.0.0.0b1
=========

.. _networking-ovn_3.0.0.0b1_Prelude:

Prelude
-------

.. releasenotes/notes/ovsdb-ssl-support-213ff378777cf946.yaml @ 21a2f5782e0500ccb6d6e6a6e13cb5c3bde9fad9

networking-ovn now supports the use of SSL for its OVSDB connections to the OVN databases.


.. _networking-ovn_3.0.0.0b1_New Features:

New Features
------------

.. releasenotes/notes/ovsdb-ssl-support-213ff378777cf946.yaml @ 21a2f5782e0500ccb6d6e6a6e13cb5c3bde9fad9

- networking-ovn now supports the use of SSL for its OVSDB connections to the OVN databases.


.. _networking-ovn_2.0.0:

2.0.0
=====

.. _networking-ovn_2.0.0_New Features:

New Features
------------

.. releasenotes/notes/ovn-native-nat-9bbc92f16edcf2f5.yaml @ b40f1dda476732471e71680632fd02e729351a77

- OVN native L3 implementation.
  The native implementation supports distributed routing for east-west
  traffic and centralized routing for north-south (floatingip and snat)
  traffic. Also supported is the Neutron L3 Configurable external gateway
  mode.

.. releasenotes/notes/ovn_dhcpv6-729158d634aa280e.yaml @ ed998d2dd72b934c2428a963e4b224c57f53946e

- OVN native DHCPv6 implementation.
  The native implementation supports distributed DHCPv6. Support
  Neutron IPv6 subnet whose "ipv6_address_mode" attribute is None,
  "dhcpv6_stateless", or "dhcpv6_stateful".


.. _networking-ovn_2.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/bug-1606458-b9f809b3914bb203.yaml @ 5be7dfeb637984f75937a21b994c1375dfa77d87

- The ``ovn`` group ``vif_type`` configuration option is deprecated and will be removed in the next release. The port VIF type is now determined based on the OVN chassis information when the port is bound to a host. [Bug `1606458 <https://bugs.launchpad.net/bugs/1606458>`_]

.. releasenotes/notes/ovsdb_connection-cef6b02c403163a3.yaml @ d0de15eee9b201d88f4e3b60b3233a8dee71ec0b

- The ``ovn`` group ``ovsdb_connection`` configuration option was deprecated in the ``Newton`` release and has now been removed.


.. _networking-ovn_1.0.0.0b2:

1.0.0.0b2
=========

.. _networking-ovn_1.0.0.0b2_New Features:

New Features
------------

.. releasenotes/notes/networking-ovn-0df373f5a7b22d19.yaml @ 7dffd601889d6288c8ee87280b5e59fc2549c694

- Initial release of the OpenStack Networking service (neutron)
  integration with Open Virtual Network (OVN), a component of the
  `Open vSwitch <http://openvswitch.org/>`_ project. OVN provides
  the following features either via native implementation or
  conventional agents:
  
  * Layer-2 (native OVN implementation)
  * Layer-3 (native OVN implementation or conventional layer-3 agent)
    The native OVN implementation supports distributed routing. However,
    it currently lacks support for floating IP addresses, NAT, and the
    metadata proxy.
  * DHCP (native OVN implementation or conventional DHCP agent)
    The native implementation supports distributed DHCP. However,
    it currently lacks support for IPv6, internal DNS, and metadata
    proxy.
  * Metadata (conventional metadata agent)
  * DPDK - Usable with OVS via either the Linux kernel datapath
    or the DPDK datapath.
  * Trunk driver - Driver to back the neutron's 'trunk' service plugin
  
  The initial release also supports the following Networking service
  API extensions:
  
  * ``agent``
  * ``Address Scopes`` \*
  * ``Allowed Address Pairs``
  * ``Auto Allocated Topology Services``
  * ``Availability Zone``
  * ``Default Subnetpools``
  * ``DHCP Agent Scheduler`` \*\*
  * ``Distributed Virtual Router`` \*
  * ``DNS Integration`` \*
  * ``HA Router extension`` \*
  * ``L3 Agent Scheduler`` \*
  * ``Multi Provider Network``
  * ``Network Availability Zone`` \*\*
  * ``Network IP Availability``
  * ``Neutron external network``
  * ``Neutron Extra DHCP opts``
  * ``Neutron Extra Route``
  * ``Neutron L3 Configurable external gateway mode`` \*
  * ``Neutron L3 Router``
  * ``Network MTU``
  * ``Port Binding``
  * ``Port Security``
  * ``Provider Network``
  * ``Quality of Service``
  * ``Quota management support``
  * ``RBAC Policies``
  * ``Resource revision numbers``
  * ``Router Availability Zone`` \*
  * ``security-group``
  * ``standard-attr-description``
  * ``Subnet Allocation``
  * ``Tag support``
  * ``Time Stamp Fields``
  
  (\*) Only applicable if using the conventional layer-3 agent.
  
  (\*\*) Only applicable if using the conventional DHCP agent.

