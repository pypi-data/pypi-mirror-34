===================
tripleo-validations
===================

.. _tripleo-validations_9.2.0:

9.2.0
=====

.. _tripleo-validations_9.2.0_New Features:

New Features
------------

.. releasenotes/notes/bug-1776721-2e0abe371abee71c.yaml @ b'5e7c25c1243fdbb38daec2d3f620d18b3c6debd2'

- Adds an undercloud heat-manage purge_deleted cron job validation.


.. _tripleo-validations_9.1.0:

9.1.0
=====

.. _tripleo-validations_9.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/validate-xfs-ftype-equals-0-8fdb1f8c99bee975.yaml @ b'a5e63ee72531c85ee527ce721022fffce3cfcf75'

- Validate that there are no volumes formatted with XFS
  and ftype=0.
  Deployments from OpenStack Kilo or Liberty have XFS
  partitions formatted with ftype=0, which is incompatible
  with the docker overlayfs driver.
  From OpenStack Newton, we have support for XFS ftype=1
  by default.
  This check will make fail the pre-upgrade validations
  if there are deployments coming back from Kilo or Liberty
  and have XFS partitions with ftype=0.


.. _tripleo-validations_9.0.0:

9.0.0
=====

.. _tripleo-validations_9.0.0_New Features:

New Features
------------

.. releasenotes/notes/add-selinux-validation-e23694aaf94d2a66.yaml @ b'c6e62ac7bfee21199f1ccce9d0bee188f59db909'

- New validation to check for the SELinux Enforcing mode on the Undercloud.

.. releasenotes/notes/check-latest-minor-version-14befc616a59002b.yaml @ b'4920dab28df7b16246fe2cc759231bf6a5fd0461'

- New validation to check for latest minor version of python-tripleoclient

.. releasenotes/notes/check-latest-minor-version-14befc616a59002b.yaml @ b'4920dab28df7b16246fe2cc759231bf6a5fd0461'

- New module to check for new minor and major versions of a package


.. _tripleo-validations_9.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/deprecate-ini-inventory-d7446df7e967adfe.yaml @ b'd603d978061da21b70144ce287ccf0a852e88742'

- The ``--static-inventory`` argument to ``tripleo-ansible-inventory`` has
  been deprecated and aliased to ``--static-yaml-inventory``.  See
  `bug 1751855 <https://bugs.launchpad.net/tripleo/+bug/1751855>`__.

