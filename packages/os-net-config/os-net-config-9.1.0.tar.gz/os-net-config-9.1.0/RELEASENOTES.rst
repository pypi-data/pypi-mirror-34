=============
os-net-config
=============

.. _os-net-config_9.1.0:

9.1.0
=====

.. _os-net-config_9.1.0_New Features:

New Features
------------

.. releasenotes/notes/add-neutron-route-schema-support-e8e20a8c3b79d14d.yaml @ b'206615288ab284233134da4ab5527888e80a62a5'

- Adds support to use ``destination`` and ``nexthop`` as keys in the
  ``Route`` objects. ``destination`` maps to ``ip_netmask`` and ``nexthop``
  maps to ``next_hop``. Neutron Route objects use ``destination`` and
  ``nexthop``, supporting the same schema allow passing a neutron route
  directly to os-net-config.


.. _os-net-config_9.1.0_Known Issues:

Known Issues
------------

.. releasenotes/notes/add_contrail_vrouter_vlan_linux_bond_type-0a89f3499a7ab08b.yaml @ b'40ce571209087d22e1bf6e9510218eb8efaf0bc1'

- Currently the member interface for a contrail vrouter interface can only
  be of type interface. Types vlan and linux_bond are needed.


.. _os-net-config_9.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add_contrail_vrouter_vlan_linux_bond_type-0a89f3499a7ab08b.yaml @ b'40ce571209087d22e1bf6e9510218eb8efaf0bc1'

- This fix adds support for member interfaces of type vlan and linux_bond

.. releasenotes/notes/check-ovs-ef665418762ca123.yaml @ b'8250d67a237e5f219d839899b96715004cf14fea'

- OVS is not required for os-net-config to run but some objects (OvsBond, OvsBridge etc.) rely on it being installed. This adds a check to ensure OVS is installed before creating objects that need it.


.. _os-net-config_9.0.0:

9.0.0
=====

.. _os-net-config_9.0.0_New Features:

New Features
------------

.. releasenotes/notes/dpdk-on-mellanox-nics-1d8fdb843a4e2b60.yaml @ b'aeaa6fe62b39a00f3b075a94c076f267f0c70af0'

- Adding dpdk support in meallnox nics.
  Dpdk now fully suuported in mellanox nics.

