======================
python-openstackclient
======================

.. _python-openstackclient_3.16.0:

3.16.0
======

.. _python-openstackclient_3.16.0_New Features:

New Features
------------

.. releasenotes/notes/add-image-member-list-1630ead5988348c2.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``image member list`` command to list all members of an image.

.. releasenotes/notes/add-image-tag-filter-support-5cb039416b07caab.yaml @ 9edbab8c90bb74ba12892d0c77c8e8a99d4868fe

- Add ``--tag`` option to ``image list`` command to filter by tag.

.. releasenotes/notes/add-server-create-image-property-ef76af26233b472b.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add  ``--image-property`` option to ``server create`` command.
  This parameter will filter a image which properties that are matching.

.. releasenotes/notes/allow-port-list-with-ip-address-substr-14c5805b241e402f.yaml @ 4a9cb8eea8e47950cb30ecaa7572a23d80d5bfcd

- Add an ``ip-substring`` key to the ``--fixed-ip`` option of the
  ``port list`` command.  This allows filtering ports by a substring
  match of an IP address.
  [Bug `1718605 <https://bugs.launchpad.net/bugs/1718605>`_]

.. releasenotes/notes/bp-unified-limits-58f166401534a4ff.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``registered limit`` commands for managing registered limits in Keystone.
  Registered limits define limits of resources for projects to assume by default.
  [`bp unified-limits <https://blueprints.launchpad.net/keystone/+spec/unified-limit>`_]

.. releasenotes/notes/bp-unified-limits-6c5fdb1c26805d86.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``limit`` commands for managing project-specific limits in keystone.
  Limits define limits of resources for projects to consume once a limit
  has been registered.
  [`bp unified-limits <https://blueprints.launchpad.net/keystone/+spec/unified-limit>`_]

.. releasenotes/notes/bug-1750983-420945d6c0afb509.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``--tag`` and ``--no-tag`` options to ``security group create`` and
  ``security group set`` commands.
  [Bug `1750983 <https://bugs.launchpad.net/python-openstackclient/+bug/1750983>`_]

.. releasenotes/notes/bug-1750983-420945d6c0afb509.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``--tags``, ``--any-tags``, ``--not-tags`` and ``--not-any-tags`` options
  to ``security group list`` command.
  [Bug `1750983 <https://bugs.launchpad.net/python-openstackclient/+bug/1750983>`_]

.. releasenotes/notes/bug-1750983-420945d6c0afb509.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add ``--tag`` and ``--all-tag`` options to ``security group unset`` command.
  [Bug `1750983 <https://bugs.launchpad.net/python-openstackclient/+bug/1750983>`_]

.. releasenotes/notes/flavor-add-description-b618abd4a7fb6545.yaml @ 7e8c55fa1bbc5f44b9233602786c22d6019eef22

- Add ``--description`` option to ``flavor set`` command to update the description of the flavor. Only available starting with ``--os-compute-api-version 2.55``.

.. releasenotes/notes/flavor-add-description-b618abd4a7fb6545.yaml @ 7e8c55fa1bbc5f44b9233602786c22d6019eef22

- Add ``--description`` option to ``flavor create`` command to set the description of the flavor. Only available starting with ``--os-compute-api-version 2.55``.

.. releasenotes/notes/implement-system-scope-4c3c47996f98deac.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- Add support for system-scope to ``role`` commands. This includes the ability to
  generate system-scoped tokens using ``system_scope: all`` in ``cloud.yaml``
  or ``OS_SYSTEM_SCOPE=all`` in an environment variable. Support is also
  included for managing role assignments on the system using ``--system``
  when adding and removing roles.
  [`bp system-scope <https://blueprints.launchpad.net/keystone/+spec/system-scope>`_]

.. releasenotes/notes/subnet-set-segment-id-4440e433b170f9f3.yaml @ e8c731547d85b1241c7898d2fb77b8d635901dfd

- Add ``--network-segment`` option to ``subnet set`` command. This enables the possiblity to set the ``segment_id`` of a subnet on update.

.. releasenotes/notes/versions-show-12a2443624c83048.yaml @ 9ece632f96844fd78c2f717f2f6d35e61c3b9ef2

- A new command, ``openstack versions show`` was added, which will
  provide a list of all versions of all services in the cloud. It
  includes relevant metadata, such as min/max microversion, endpoint,
  status and region.


.. _python-openstackclient_3.16.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add-community-option-to-image-list-ac0651eb2e5d632f.yaml @ 860639a548a2c07193662cd361432cb5061c2a7f

- Add ``--community`` option to ``image list`` command. [Bug `2001925 <https://storyboard.openstack.org/#!/story/2001925>`_]

.. releasenotes/notes/bug-1742453-ae4be6de90a3ae1d.yaml @ c615bcd75e85a2a2231d9944caeffd746e881e5e

- The ``server list --all`` command now resolves non-public flavor names,
  too, so that the ``Flavor`` column will be properly populated.
  [Bug `1742453 <https://bugs.launchpad.net/bugs/1742453>`_]

.. releasenotes/notes/bug-1750985-a5345f715a14825c.yaml @ 09a0916daeeb9c257d84175a43062d5b4a1d0b1a

- Add ``--tag`` support to ``floating ip create|list|set|unset`` commands.
  [:lpbug:`1750985`]

.. releasenotes/notes/bug-1751104-compute-api-2.47-4bfa21cfaa13f408.yaml @ 4236d777ffb6f03bb2682142aaa18b48e9a00d96

- The ``server show`` command will now properly show the server's
  flavor information when using ``--os-compute-api-version 2.47`` or higher.
  [Bug `1751104 <https://storyboard.openstack.org/#!/story/1751104>`_]


.. _python-openstackclient_3.16.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/remove-ip-floating-commands-d5363f313e09249a.yaml @ ea89065dabf92c2684e55c4b37c7be9b667cfa1e

- Remove deprecated ``ip floating`` and ``ip floating pool`` commands.


.. _python-openstackclient_3.15.0:

3.15.0
======

.. _python-openstackclient_3.15.0_New Features:

New Features
------------

.. releasenotes/notes/bp-application-credential-a7031a043efc4a25.yaml @ 375964f270e125b8887e0ca4ee1cbe15d5eddf04

- Adds support for creating, reading, and deleting application credentials
  via the ``appication credential`` command. With application credentials, a
  user can grant their applications limited access to their cloud resources.
  Once created, users can authenticate with an application credential by
  using the ``v3applicationcredential`` auth type.
  [`blueprint application-credentials <https://blueprints.launchpad.net/keystone/+spec/application-credentials>`_]

.. releasenotes/notes/bp-project-tags-b544aef9672d415b.yaml @ d32664150fbc00340f3ff4304c13abf9a191299a

- Add ``--tag`` option to ``project create`` command,  ``--tag``, ``--clear-tags``, and
  ``--remove-tag`` options to ``project set`` command. Add ``--tags``, ``--tags-any``, 
  ``--not-tags``, and ``--not-tags-any`` options to ``project list`` command to filter
  list results by different projects based on their tags.
  [`blueprint project-tags <https://blueprints.launchpad.net/keystone/+spec/project-tags>`_]

.. releasenotes/notes/bug-1714878-46806jv2yv13q054.yaml @ 4a9e84be994575146b30bd40a341d5686174eaad

- Add ``--dns-domain`` option to ``port create`` and ``port set`` commands.
  Requires the ``dns_domain for ports`` extension to be enabled. See the
  `Neutron DNS integration <https://docs.openstack.org/neutron/latest/admin/config-dns-int.html>`_
  documentation for information how to use this.
  [Bug `1714878 <https://bugs.launchpad.net/python-openstackclient/+bug/1714878>`_]

.. releasenotes/notes/keystone-endpoint-group-0c55debbb66844f2.yaml @ 1eae301c4fab30c551ed7542cdaf8735cbbc3822

- Add endpoint group commands: ``endpoint group add project``, ``endpoint group create``,
  ``endpoint group delete``, ``endpoint group list``, ``endpoint group remove project``,
  ``endpoint group set`` and ``endpoint group show``.
  [Blueprint `keystone-endpoint-filter <https://blueprints.launchpad.net/python-openstackclient/+spec/keystone-endpoint-filter>`_]

.. releasenotes/notes/neutron_mtu-d87e53e2d76f8612.yaml @ 18563b4132f794cc6612c2897795f96a31b565ae

- Add ``--mtu`` option to ``network create`` and ``network set``
  commands, allowing CLI users to set the MTU for Neutron networks.

