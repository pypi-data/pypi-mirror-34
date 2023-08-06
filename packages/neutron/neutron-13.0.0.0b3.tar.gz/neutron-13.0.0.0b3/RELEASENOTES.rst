=======
neutron
=======

.. _neutron_13.0.0.0b3:

13.0.0.0b3
==========

.. _neutron_13.0.0.0b3_Prelude:

Prelude
-------

.. releasenotes/notes/add-multiple-port-bindings-f16eb47ebdddff2d.yaml @ b'f7064f2b6c6ba1d0ab5f9872b2d5ad7969a64e7b'

Support multiple bindings for compute owned ports.


.. releasenotes/notes/support-filter-validation-fee2cdeedbe8ad76.yaml @ b'2b1d8ea4a202f24c1b485ccebdbf831c505a4e6a'

Perform validation on filter parameters on listing resources.


.. _neutron_13.0.0.0b3_New Features:

New Features
------------

.. releasenotes/notes/add-multiple-port-bindings-f16eb47ebdddff2d.yaml @ b'f7064f2b6c6ba1d0ab5f9872b2d5ad7969a64e7b'

- In order to better support instance migration, multiple port
  bindings can be associated to compute owned ports.
  
  * Create, update, list, show and activate operations are supported
    for port bindings by the ReST API.
  * A compute owned port can have one active binding and many
    inactive bindings.
  * There can be only one binding (active or inactive) per compute
    host.
  * When the ``activate`` operation is executed, a previously
    inactive binding is made active. The previously active binding
    becomes inactive.
  * As a consequence of the multiple port bindings implementation,
    the ``port_binding`` relationship in the SQLAlchemy ``Port``
    object has been renamed ``port_bindings``. Similarly, the
    ``binding`` attribute of the ``Port`` OVO has been renamed
    ``bindings``.

.. releasenotes/notes/ovs-mac-table-size-config-option-d255d5208650f34b.yaml @ b'1f8378e0ac4b8c3fc4670144e6efc51940d796ad'

- A new config option ``bridge_mac_table_size`` has been added for
  Neutron OVS agent.
  This value will be set on every Open vSwitch bridge managed by the
  openvswitch-neutron-agent in ``other_config:mac-table-size`` column
  in ovsdb.
  Default value for this new option is set to 50000 and it should be enough
  for most systems.
  More details about this option can be found in `Open vSwitch documentation
  <http://www.openvswitch.org/support/dist-docs/ovs-vswitchd.conf.db.5.html>`_
  For more information see bug
  `1775797 <https://bugs.launchpad.net/neutron/+bug/1775797>`_.

.. releasenotes/notes/port-mac-address-regenerate-312978c834abaa52.yaml @ b'8f3a066b20b7ffafec95a618d60e40727504f37c'

- Adds  api extenstion ``port-mac-address-regenerate``. When passing
  ``'null'`` (``None``) as the ``mac_address`` on port update a converter
  will generate a new mac address that will be assigned to the port.
  `RFE:  #1768690 <https://bugs.launchpad.net/neutron/+bug/1768690>`_.

.. releasenotes/notes/routed-networks-hostroutes-a13a9885f0db4f69.yaml @ b'8361b8b5aebad4df3c1012952d9a87b936fef326'

- Adds host routes for subnets on the same network when using routed
  networks. Static routes will be configured for subnets associated with
  other segments on the same network. This ensures that traffic within an L3
  routed network stays within the network even when the default route is on
  a different interface.

.. releasenotes/notes/support-filter-validation-fee2cdeedbe8ad76.yaml @ b'2b1d8ea4a202f24c1b485ccebdbf831c505a4e6a'

- Starting from this release, neutron server will perform validation on
  filter parameters on list requests. Neutron will return a 400 response
  if the request contains invalid filter parameters.
  The list of valid parameters is documented in the neutron API reference.
  
  Add an API extension ``filter-validation`` to indicate this new API
  behavior. This extension can be disabled by operators via a config option.


.. _neutron_13.0.0.0b3_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/support-filter-validation-fee2cdeedbe8ad76.yaml @ b'2b1d8ea4a202f24c1b485ccebdbf831c505a4e6a'

- Prior to the upgrade, if a request contains an unknown or unsupported
  parameter, the server will silently ignore the invalid input.
  After the upgrade, the server will return a 400 Bad Request response
  instead.
  
  API users might observe that requests that received a successful response
  now receive a failure response. If they encounter such experience,
  they are suggested to confirm if the API extension ``filter-validation``
  is present and validate filter parameters in their requests.
  
  Operators can disable this feature if they want to maintain
  backward-compatibility. If they choose to do that, the API extension
  ``filter-validation`` will not be present and the API behavior is
  unchanged.


.. _neutron_13.0.0.0b3_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/dns_domain-6f0e628aeb3c650c.yaml @ b'137a6d61053fb1cfb9a0a583b5a5c0f6253c75e6'

- Previously a network's dns_domain attribute was ignored by the DHCP agent.
  With this release, OpenStack deployments using Neutron's DHCP agent will
  be able to specify a per network dns_domain and have instances configure
  that domain in their dns resolver configuration files (Linux's
  /etc/resolv.conf) to allow for local partial DNS lookups. The per-network
  dns_domain value will override the DHCP agent's default dns_domain
  configuration value. Note that it's also possible to update a network's
  dns_domain, and that new value will be propogated to new instances
  or when instances renew their DHCP lease. However, existing leases will
  live on with the old dns_domain value.


.. _neutron_13.0.0.0b3_Other Notes:

Other Notes
-----------

.. releasenotes/notes/support-filter-validation-fee2cdeedbe8ad76.yaml @ b'2b1d8ea4a202f24c1b485ccebdbf831c505a4e6a'

- Each plugin can decide if it wants to support filter validation by
  setting ``__filter_validation_support`` to True or False. If this field is
  not set, the default value is False.
  Right now, the ML2 plugin and all the in-tree service plugins support
  filter validation. Out-of-tree plugins will have filter validation
  disabled by default but they can turn it on if they choose to.
  For filter validation to be supported, the core plugin and all the
  services plugins in a deployment must support it.


.. _neutron_13.0.0.0b2:

13.0.0.0b2
==========

.. _neutron_13.0.0.0b2_New Features:

New Features
------------

.. releasenotes/notes/add-port_details-to-floatingip-fefceab2c740e482.yaml @ b'c760d4f26f4b4753c80269437d2cd0b8f63dbc7c'

- Add attribute ``port_details`` to floating IP. The value of this attribute
  contains information of the associated port.

.. releasenotes/notes/allow-update-subnet-segment-id-association-1fb02ace27e85bb8.yaml @ b'b6d117fcd577f50a431113c4ad13258a7692e822'

- Add support for setting the ``segment_id`` for an existing
  subnet. This enables users to convert a non-routed network
  with no subnet/segment association to a routed one. It is
  only possible to do this migration if both of the following
  conditions are met - the current ``segment_id`` is ``None``
  and the network contains a single segment and subnet.

.. releasenotes/notes/support-empty-string-filtering-4a39096b62b9abf2.yaml @ b'a732bbf19e31f6bab8d1ffd2540f6e367caab4c8'

- Add support for filtering attributes with value as empty string. A shim
  extension is added to indicate if this feature is supported.


.. _neutron_13.0.0.0b2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/ib-dhcp-allocation-fix-a4ebe8b55bb2c065.yaml @ b'59bc19c14a84283adad555dce8536fd7198b82b3'

- For Infiniband support, Ironic needs to send the 'client-id' DHCP option
  as a number in order for IP address assignment to work.
  This is now supported in Neutron, and can be specified as option number
  61 as defined in RFC 4776.  For more information see bug
  `1770932 <https://bugs.launchpad.net/neutron/+bug/1770932>`_


.. _neutron_13.0.0.0b2_Other Notes:

Other Notes
-----------

.. releasenotes/notes/ivs-interfacedriver-removal-a9cce87310028b99.yaml @ b'3ad91f61f2d40d788764d64b1870d509069aad0a'

- The deprecated ``IVSInterfaceDriver`` class has been removed from the code base.  This means neither the ``ivs`` nor the ``neutron.agent.linux.interface.IVSInterfaceDriver`` can any longer be used as a value for the ``interface_driver`` config option in ``neutron.conf``.


.. _neutron_13.0.0.0b1:

13.0.0.0b1
==========

.. _neutron_13.0.0.0b1_Prelude:

Prelude
-------

.. releasenotes/notes/add-conntrack-workers-89d303e9ec3b4963.yaml @ b'65a81623fc0377b26d2d5800607f7c3acc08c45a'

In order to reduce the time spent processing security group updates in the L2 agent, conntrack deletion is now performed in a set of worker threads instead of the main agent thread, so it can return to processing other events quickly.


.. _neutron_13.0.0.0b1_New Features:

New Features
------------

.. releasenotes/notes/add-new-harouter-state-5612fc5b5c2043a5.yaml @ b'b62d1bfdf71c2f8810d9b143d50127b8f3a4942d'

- Added new ``unknown`` state for HA routers. Sometimes l3 agents may not be able to update health status to Neutron server due to communication issues. During that time the server may not know whether HA routers hosted by that agent are active or standby.

.. releasenotes/notes/security-groups-port-filtering-69d36ac7db90c9e0.yaml @ b'43d3e88a07b4275ad814c6875fa037efd94223bb'

- Support port filtering on security group IDs.
  The feature can be used if 'port-security-group-filtering' extension is available.


.. _neutron_13.0.0.0b1_Known Issues:

Known Issues
------------

.. releasenotes/notes/ovsdb_timeout_override_for_ovs_cleanup_tool-e6ed6db258d0819e.yaml @ b'806d96cbbe45fcd473935e777a2a56037fbb9d12'

- In the case when the number of ports to clean up in a single bridge is
  larger than about 10000, it might require an increase in the
  ``ovsdb_timeout`` config option to some value higher than 600 seconds.


.. _neutron_13.0.0.0b1_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/add-conntrack-workers-89d303e9ec3b4963.yaml @ b'65a81623fc0377b26d2d5800607f7c3acc08c45a'

- On an upgrade, conntrack entries will now be cleaned-up in a worker
  thread, instead of in the calling thread.


.. _neutron_13.0.0.0b1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add-conntrack-workers-89d303e9ec3b4963.yaml @ b'65a81623fc0377b26d2d5800607f7c3acc08c45a'

- Fixes bug `1745468 <https://bugs.launchpad.net/neutron/+bug/1745468>`_.

.. releasenotes/notes/add-new-harouter-state-5612fc5b5c2043a5.yaml @ b'b62d1bfdf71c2f8810d9b143d50127b8f3a4942d'

- Fixes bug `1682145 <https://launchpad.net/bugs/1682145>`_.

.. releasenotes/notes/add-standard-attributes-to-segment-d39c4b89988aa701.yaml @ b'4d84c10ba4430752bf8c1227c770fb3c4f0a1618'

- Fix an issue that standard attributes, such as ``created_at``,
  ``updated_at`` and ``revision_number``, are not rendered in the response
  of segment resource.

.. releasenotes/notes/ovsdb_timeout_override_for_ovs_cleanup_tool-e6ed6db258d0819e.yaml @ b'806d96cbbe45fcd473935e777a2a56037fbb9d12'

- Fixes bug `1763604 <https://bugs.launchpad.net/neutron/+bug/1763604>`_.
  Override default value of ``ovsdb_timeout`` config option in
  ``neutron-ovs-cleanup`` script.
  The default value is 10 seconds, but that is not enough for the
  ``neutron-ovs-cleanup`` script when there are many ports to remove from
  a single bridge, for example, 5000. Because of that, we now override the
  default value for the config option to be 600 seconds (10 minutes).

