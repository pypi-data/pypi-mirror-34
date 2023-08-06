==============
python-watcher
==============

.. _python-watcher_1.11.0:

1.11.0
======

.. _python-watcher_1.11.0_New Features:

New Features
------------

.. releasenotes/notes/add-ha-support-b9042255e5b76e42.yaml @ b'e426a015eeff3b7d95061fb4180e2cc878db0308'

- Watcher services can be launched in HA mode. From now on Watcher Decision Engine and Watcher Applier services may be deployed on different nodes to run in active-active or active-passive mode. Any ONGOING Audits or Action Plans will be CANCELLED if service they are executed on is restarted.


.. _python-watcher_1.10.0:

1.10.0
======

.. _python-watcher_1.10.0_New Features:

New Features
------------

.. releasenotes/notes/bp-audit-scope-exclude-project-511a7720aac00dff.yaml @ b'fc388d829232cd95251ac487b56d2b1945081b62'

- Feature to exclude instances from audit scope based on project_id is added.
  Now instances from particular project in OpenStack can be excluded from audit
  defining scope in audit templates.

.. releasenotes/notes/host-maintenance-strategy-41f640927948fb56.yaml @ b'58276ec79e856cd11d45baaa3548b9bf0db015d7'

- Added a strategy for one compute node maintenance,
  without having the user's application been interrupted.
  If given one backup node, the strategy will firstly
  migrate all instances from the maintenance node to
  the backup node. If the backup node is not provided,
  it will migrate all instances, relying on nova-scheduler.


.. _python-watcher_1.9.0:

1.9.0
=====

.. _python-watcher_1.9.0_New Features:

New Features
------------

.. releasenotes/notes/add-name-for-audit-0df1f39f00736f06.yaml @ b'9fb5b2a4e78ac80fcf373708a5f19c85589677fe'

- Audits have 'name' field now, that is more friendly to end users. Audit's name can't exceed 63 characters.

.. releasenotes/notes/compute-cdm-include-all-instances-f7506ded2d57732f.yaml @ b'dad60fb87887c82070a509c7909eefc140d90b10'

- Watcher has a whole scope of the cluster, when building compute CDM which includes all instances. It filters excluded instances when migration during the audit.

.. releasenotes/notes/multiple-global-efficacy-indicator-fc11c4844a12a7d5.yaml @ b'9fb5b2a4e78ac80fcf373708a5f19c85589677fe'

- Watcher got an ability to calculate multiple global efficacy indicators during audit's execution. Now global efficacy can be calculated for many resource types (like volumes, instances, network) if strategy supports efficacy indicators.

.. releasenotes/notes/notifications-actionplan-cancel-edb2a4a12543e2d0.yaml @ b'9fb5b2a4e78ac80fcf373708a5f19c85589677fe'

- Added notifications about cancelling of action plan. Now event based plugins know when action plan cancel started and completed.

.. releasenotes/notes/replace-cold-migrate-to-use-nova-migration-api-cecd9a39ddd3bc58.yaml @ b'4179c3527cc09088e70008f1a2959b6e2730d526'

- Instance cold migration logic is now replaced with using Nova migrate
  Server(migrate Action) API which has host option since v2.56.


.. _python-watcher_1.9.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/replace-cold-migrate-to-use-nova-migration-api-cecd9a39ddd3bc58.yaml @ b'4179c3527cc09088e70008f1a2959b6e2730d526'

- Nova API version is now set to 2.56 by default. This needs the migrate
  action of migration type cold with destination_node parameter to work.


.. _python-watcher_1.9.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/replace-cold-migrate-to-use-nova-migration-api-cecd9a39ddd3bc58.yaml @ b'4179c3527cc09088e70008f1a2959b6e2730d526'

- The migrate action of migration type cold with destination_node parameter
  was fixed. Before fixing, it booted an instance in the service project
  as a migrated instance.

