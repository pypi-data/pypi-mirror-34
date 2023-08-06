========
nodepool
========

.. _nodepool_3.2.0:

3.2.0
=====

.. _nodepool_3.2.0_New Features:

New Features
------------

.. releasenotes/notes/ignore-provider-quota-aa19e7a7271ee106.yaml @ b'4c8b5f4f99ee824b53fa831d92bbc13a3a5a6f9b'

- A new boolean pool variable ``ignore-provider-quota`` has been added to
  allow the provider quota to be ignored for a pool. Instead, nodepool only
  checks against the configured max values for the pool and the current usage
  based on stored data. This may be useful in circumstances where the
  provider is incorrectly calculating quota.

.. releasenotes/notes/nodepool-list-pool-detail-680f47814fd51427.yaml @ b'5745c807c994004657000d6508e36fdf6e448b8e'

- The detailed nodepool list outputs the node's pool.

.. releasenotes/notes/secure-dib-env-c6013bab90406988.yaml @ b'eca37d13eaf5bb9bcd439d44cc8cd55ecc868a19'

- Diskimages env-vars can be set in the secure.conf file.


.. _nodepool_3.2.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/aborted-node-status-3fd18d39cb468f8f.yaml @ b'60bf606db48eb575ead7c10914cb893878bfec94'

- A new node status (ABORTED) is added to the ZooKeeper data model. It
  is recommended that, during your nodepool upgrade, you shut down all
  launcher processes before restarting any of them. Running multiple
  launchers with mixed support of this new node status may cause
  unexpected errors to be reported in the logs.


.. _nodepool_3.2.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/unmanaged_image_id-cf916620abc630e4.yaml @ b'd39cc6d7ceb31d30aa1923c04033b727427529bc'

- For pre-existing cloud images (not managed by nodepool), referencing
  them by ID was failing since they could not be found with this data,
  only by name.


.. _nodepool_3.1.0:

3.1.0
=====

.. _nodepool_3.1.0_New Features:

New Features
------------

.. releasenotes/notes/default-format-fb859338909defb9.yaml @ b'6ec75970b3e8b81b2800cb1b4e9c0315a70b903a'

- Nodepool now defaults to building qcow2 diskimages instead of failing if
  the diskimage doesn't specify an image format and the diskimage isn't used
  by any provider. This makes it more convenient to build images without
  uploading them to a cloud provider.

.. releasenotes/notes/security-group-support.yaml @ b'674c9516dc8fa63bde2ab36db60560fc72b09a6b'

- Added support for specifying security-groups for the nodes in openstack
  driver. Pool.security-groups takes list of SGs to attach to the server.

.. releasenotes/notes/static-driver-changes-9692c3ee0dc0bc29.yaml @ b'3e0a822bf67139c13f61c74160f655f8f8388788'

- The static driver now pre-registers its nodes with ZooKeeper at startup
  and on configuration changes. A single node may be registered multiple
  times, based on the value of max-parallel-jobs.


.. _nodepool_3.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/multilabel-999f0d38d02848a2.yaml @ b'77edb84fb681ebdd8ce19a4876f511c9233c4dc5'

- Nodepool can now support multiple node labels, although the OpenStack and
  static node drivers do not yet support specifying multiple labels, so this
  is not yet a user-visible change. This does, however, require shutting down
  all launcher processes before restarting them. Running multiple launchers
  with mixed support of multi-label will cause errors, so a full shutdown is
  required.


.. _nodepool_3.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/paused-handler-fix-6c4932dcf71939ba.yaml @ b'3eab2396ae8b6fdacb631e505ceff82efb0415da'

- Fixed a bug where if a request handler is paused and an exception is thrown
  within the handler, the handler was not properly unpaused and the request
  remained in the list of active handlers.


.. _nodepool_3.0.1:

3.0.1
=====

.. _nodepool_3.0.1_New Features:

New Features
------------

.. releasenotes/notes/diskimage-connection-port-f53b0a9c910cb393.yaml @ b'687f120b3c21b527c217a734144e105d7daead76'

- The connection port can now be configured in the provider diskimages
  section.

.. releasenotes/notes/static-driver-windows-cf80096636dbb428.yaml @ b'da95a817bbc742dbab587953b542686a4c375c89'

- Added support for configuring windows static nodes. A static node can now
  define a ``connection-type``. The ``ssh-port`` option has been renamed
  to ``connection-port``.


.. _nodepool_3.0.1_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/static-driver-windows-cf80096636dbb428.yaml @ b'da95a817bbc742dbab587953b542686a4c375c89'

- ``ssh-port`` in static node config is deprecated. Please update config to
  use ``connection-port`` instead.

