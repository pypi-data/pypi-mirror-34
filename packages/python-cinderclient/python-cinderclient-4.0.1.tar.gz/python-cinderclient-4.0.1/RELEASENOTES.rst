===================
python-cinderclient
===================

.. _python-cinderclient_4.0.1:

4.0.1
=====

.. _python-cinderclient_4.0.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/volume-transfer-bug-23c760efb9f98a4d.yaml @ b'460229c6099719dec0d027f798f9c751b8ec7e44'

- An issue was discovered with the way API microversions were handled for the
  new volume-transfer with snapshot handling with microversion 3.55. This
  release includes a fix to keep backwards compatibility with earlier
  releases. See `bug #1784703
  <https://bugs.launchpad.net/cinder/+bug/1784703>`_ for more details.


.. _python-cinderclient_4.0.0:

4.0.0
=====

.. _python-cinderclient_4.0.0_New Features:

New Features
------------

.. releasenotes/notes/attachment-mode-8427aa6a2fa26e70.yaml @ b'826c5fc16d6f572cf544e3f0a91330bf92701c69'

- Added the ability to specify the read-write or read-only mode of an
  attachment starting with microversion 3.54. The command line usage is
  `cinder attachment-create --mode [rw|ro]`.

.. releasenotes/notes/transfer-snapshots-555c61477835bcf7.yaml @ b'a554faa6530fa0bb70430572869a6a2555783912'

- Starting with microversion 3.55, the volume transfer command now has the
  ability to exclude a volume's snapshots when transferring a volume to another
  project. The new command format is `cinder transfer-create --no-snapshots`.


.. _python-cinderclient_4.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/remove-deprecations-621919062f867015.yaml @ b'a331f06df0158fff28162eabc765f164855afcee'

- The following CLI options were deprecated for one or more releases and have
  now been removed:
  
  ``--endpoint-type``
    This option has been replaced by ``--os-endpoint-type``.
  
  ``--bypass-url``
    This option has been replaced by ``--os-endpoint``.
  
  ``--os-auth-system``
    This option has been replaced by ``--os-auth-type``.

.. releasenotes/notes/remove-replv1-cabf2194edb9d963.yaml @ b'32251f0ea3863098b4d4d54364c8ee18ff170a44'

- The volume creation argument ``--source-replica`` on the command line and
  the ``source_replica`` kwarg for the ``create()`` call when using the
  cinderclient library were for the replication v1 support that was removed
  in the Mitaka release. These options have now been removed.


.. _python-cinderclient_3.6.0:

3.6.0
=====

.. _python-cinderclient_3.6.0_New Features:

New Features
------------

.. releasenotes/notes/feature-cross-az-backups-9d428ad4dfc552e1.yaml @ b'2c774cc015cb6624fe37823b586864c63525c379'

- Support cross AZ backup creation specifying desired backup service AZ
  (added in microversion v3.51)

.. releasenotes/notes/support-filter-type-7yt69ub7ccbf7419.yaml @ b'5a1513244caf7acbd41e181419bc8b62bf4bcaba'

- New command option ``--filters`` is added to ``type-list`` command to support filter types since 3.52, and it's only valid for administrator.

