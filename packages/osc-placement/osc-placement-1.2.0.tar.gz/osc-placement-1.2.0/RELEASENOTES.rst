=============
osc-placement
=============

.. _osc-placement_1.2.0:

1.2.0
=====

.. _osc-placement_1.2.0_New Features:

New Features
------------

.. releasenotes/notes/microversion-1.5-0c6342c887669b8e.yaml @ b'0a5493f264902f8f21b87f3fcc792997ac7bfb85'

- The ``openstack resource provider inventory delete`` command now supports
  microversion `1.5`_. Specifically it is possible to delete all inventories
  of the specified resource provider.
  
  See the `command documentation`__ for more details.
  
  .. _1.5: https://docs.openstack.org/nova/latest/user/placement.html#delete-all-inventory-for-a-resource-provider
  .. __: https://docs.openstack.org/osc-placement/latest/cli/index.html#resource-provider-inventory-delete

.. releasenotes/notes/microversion-1.6-54a85ef9ae79f15d.yaml @ b'61b08c5ac76ea1c1998e88e4c14c0e960ca7abec'

- The following list of trait related commands was added for microversion `1.6`_:
    - ``openstack trait list``
    - ``openstack trait show``
    - ``openstack trait create``
    - ``openstack trait delete``
    - ``openstack resource provider trait list``
    - ``openstack resource provider trait set``
    - ``openstack resource provider trait delete``
  
  See the `command documentation`__ for more details.
  
  .. _1.6: https://docs.openstack.org/nova/latest/user/placement.html#traits-api
  
  .. __: https://docs.openstack.org/osc-placement/latest/cli/index.html

.. releasenotes/notes/microversion-1.7-6be2dadd0b27910f.yaml @ b'd839cd9dc566f798aba6ae492c47d4fdb6bfd929'

- The ``openstack resource class set {name}`` command has been added which
  requires ``--os-placement-api-version 1.7``. This command is similar to
  ``openstack resource class create`` except it is idempotent if the resource
  class already exists.
  
  See the `command documentation`__ for more details.
  
  .. __: https://docs.openstack.org/osc-placement/latest/cli/index.html#resource-class-set


.. _osc-placement_1.2.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/microversion-1.5-0c6342c887669b8e.yaml @ b'0a5493f264902f8f21b87f3fcc792997ac7bfb85'

- The ``resource_class`` positional argument in command
   ``openstack resource provider inventory delete`` was replaced with the
   ``--resource-class`` optional argument. The ``--resource-class`` option
   is still required if using ``--os-placement-api-version`` less than
   1.5.


.. _osc-placement_1.1.0:

1.1.0
=====

.. _osc-placement_1.1.0_New Features:

New Features
------------

.. releasenotes/notes/microversion-1.3-and-1.4-becd8058c9dd9ad8.yaml @ b'844414861a90e251cc4f61ee6908009130284353'

- The ``openstack resource provider list`` command now supports microversion
  `1.3`_ and `1.4`_. Specifically two new options are added to the command:
  
  * ``--aggregate-uuid``: List resource providers which are members of at
    least one of the specified resource provider aggregates.
  * ``--resource``: List resource providers which have the capacity to serve
    allocation requests for the given amount of specified resource class.
  
  See the `command documentation`__ for more details.
  
  .. _1.3: https://docs.openstack.org/nova/latest/user/placement.html#member-of-query-parameter
  .. _1.4: https://docs.openstack.org/nova/latest/user/placement.html#filter-resource-providers-by-requested-resource-capacity-maximum-in-ocata
  .. __: https://docs.openstack.org/osc-placement/latest/cli/index.html#resource-provider-list

