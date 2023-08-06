=============
osc-placement
=============

.. _osc-placement_1.3.0:

1.3.0
=====

.. _osc-placement_1.3.0_New Features:

New Features
------------

.. releasenotes/notes/microversion-1.10-03ab71969921a0e4.yaml @ b'd343dcb7ca224f3b3998cf4795d308c47b1b3228'

- The ``openstack allocation candidate list`` command is
  available starting from microversion `1.10`_.
  
  See the command documentation for `allocation candidate list`_ for
  more details.
  
  .. _1.10: https://docs.openstack.org/nova/latest/user/placement.html#allocation-candidates-maximum-in-pike
  .. _allocation candidate list: https://docs.openstack.org/osc-placement/latest/cli/index.html#allocation-candidate-list

.. releasenotes/notes/microversion-1.14-support-nested-resource-providers-296961cc93ef30e8.yaml @ b'565fb8d8c4e7dff0e3df1f6708a81c0b6dc13c75'

- Support is added for the `1.14`_ placement API microversion by adding
  the ``root_provider_uuid`` and ``parent_provider_uuid`` to the output of
  resource provider list/show/create/set commands. Also resource provider
  create/set commands now have a new option ``--parent-provider <UUID>``.
  And ``resource provider list`` has a new option ``--in-tree <UUID>``.
  
  .. _1.14: https://docs.openstack.org/nova/latest/user/placement.html#add-nested-resource-providers

.. releasenotes/notes/microversion-1.16-alloc-candidates-limit-8310675ecc99a82a.yaml @ b'9f4e7eb9e82de3bd5778802e11fa15911c79b7bb'

- Support is added for the `1.16`_ placement API microversion by adding
  the ``--limit`` option to the ``openstack allocation candidate list``
  command.
  
  .. _1.16: https://docs.openstack.org/nova/latest/user/placement.html#limit-allocation-candidates

.. releasenotes/notes/microversion-1.17-alloc-candidates-required-traits-57378c735d0beeb4.yaml @ b'5883b82f69f60a64583cc51b7f578c7e8ae2ce9d'

- Support is added for the `1.17`_ placement API microversion by adding
  the ``--required`` option to the ``openstack allocation candidate list``
  command.
  
  .. _1.17: https://docs.openstack.org/nova/latest/user/placement.html#add-required-parameter-to-the-allocation-candidates-maximum-in-queens

.. releasenotes/notes/microversion-1.8-1.9-db26e40571292353.yaml @ b'fcc8081df775cccc73e632e80f034d602e6a0ab8'

- The ``openstack resource provider allocation set`` command now supports
  microversion `1.8`_. Specifically from 1.8 it is necessary to specify
  ``--user-id`` and ``--project-id`` arguments when setting allocations.
  
  The ``openstack resource usage show`` command is
  available starting from microversion `1.9`_. It is possible to
  show usages for a project and user.
  
  See the command documentation for `allocation set`_ and
  `resource usage show`_ for more details.
  
  .. _1.8: https://docs.openstack.org/nova/latest/user/placement.html#require-placement-project-id-user-id-in-put-allocations
  .. _1.9: https://docs.openstack.org/nova/latest/user/placement.html#add-get-usages
  .. _allocation set: https://docs.openstack.org/osc-placement/latest/cli/index.html#resource-provider-allocation-set
  .. _resource usage show: https://docs.openstack.org/osc-placement/latest/cli/index.html#resource-usage-show


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

.. releasenotes/notes/microversion-1.6-54a85ef9ae79f15d.yaml @ b'2bea1cc135bcd0f3c767e911016d0cb1128ddb8e'

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

