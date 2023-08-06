====
zuul
====

.. _zuul_3.2.0:

3.2.0
=====

.. _zuul_3.2.0_New Features:

New Features
------------

.. releasenotes/notes/client-check-tenant-config-4b86bfd5bf3572cb.yaml @ b'185f59068c79bcd51fd38f2baf8aba163585236e'

- Zuul client got a new command 'tenant-conf-check'. This command validates the
  schema of the tenant configuration and exits -1 if errors have been detected.

.. releasenotes/notes/inventory-zuul-child-jobs-0e7cf28f0cab83b8.yaml @ b'144df5e2d5728ff584581b8e13fade01faa3c2ec'

- A new Ansible inventory variable :var:`zuul.child_jobs` which is a
  list of the first level child jobs to be run after a job has
  finished successfully.

.. releasenotes/notes/job-extra-vars-9948be1ac2f99497.yaml @ b'a8b31da6eb549484ef1f4a4c85bf5491c37f95d1'

- Jobs are now able to use the :attr:`job.extra-vars` which will
  use the --extra-vars flag when a job runs.

.. releasenotes/notes/project-vars-0d57992a7192a62d.yaml @ b'8d80ec2ba873b76d8de6e3f9e1d61d4c0333414f'

- Project and project-templates may now create variables via a ``vars`` configuration entry.  Jobs can access these at runtime in the same manner as job variables.

.. releasenotes/notes/supercedent-manager-af86f18e8d03ee4b.yaml @ b'aa6d17175bdda88e2a5ed594d41f391271ce9980'

- The :value:`pipeline.manager.supercedent` pipeline manager has
  been added.  It is designed to make post-merge artifact build
  pipelines more efficient.

.. releasenotes/notes/zuul-cli-dequeue-command-4536a4ec1bb21d48.yaml @ b'c2c5ce26bf5bccd0995f927e73d33f5bfa47bbd6'

- The `dequeue` command has been added to the Zuul CLI.
  It allows operators to stop a given buildset at will.

.. releasenotes/notes/zuul-return-skip-child-jobs-772988c87c495cb2.yaml @ b'5c797a12a8229b30124988723f786d4ee8dea807'

- It is now possible to use zuul_return to skip child jobs. You can
  use the :var:`zuul.child_jobs` inventory variable to get a list of
  child jobs configured to run, then use zuul_return to modify the
  list.  Any child job not in zuul_return zuul.child_jobs will be
  skipped. See :ref:`return_values` for examples.


.. _zuul_3.2.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/template-branch-matchers-2259b585d239b6fe.yaml @ b'4f93d6d5270e52928190c6a3a8248ca95ae16265'

- Project Templates are now branch-aware and behave more like
  project stanzas.  If a template is defined on a branch, it will
  only apply to changes to that branch.

.. releasenotes/notes/timer-optimization-a6babecaf1c7dab8.yaml @ b'6e1b4426698735a77b0db8b6ccd69ab37f05a0d8'

- The timer trigger does not enqueue an event for every branch of every
  project anymore and it now only processes projects actually using the
  pipeline triggered by a timer.


.. _zuul_3.1.0:

3.1.0
=====

.. _zuul_3.1.0_New Features:

New Features
------------

.. releasenotes/notes/branch-protection-f79d97c4e6c0b05f.yaml @ b'0445d03542d66bbe2e337d4dad3a267331de6156'

- The GitHub driver can determine the required status checks of pull requests
  which are needed for entering a gate pipeline. This eliminates the need to
  hard code required status checks in the gate pipeline and makes
  interoperation with other GitHub apps much more flexible.

.. releasenotes/notes/broken-config-f41fda98f01a3f4e.yaml @ b'537dbe53773818cbfc08438ee70fdb92d401b427'

- Zuul is now ables to start with an invalid configuration.
  When reading configuration files from project repositories,
  if an issue is detected, Zuul will store the issue and skip
  the broken block of configuration. Issues are then reported
  in the scheduler log at the end of the configuration phase.

.. releasenotes/notes/driver-mqtt-28f62e8510863b40.yaml @ b'91f10d21bdfd09891d382b800debeb8142b605f0'

- A :attr:`<mqtt connection>` driver is added to feature build report over MQTT message.

.. releasenotes/notes/require-merged-70784e1e45cac08e.yaml @ b'735190f2ec538d8e19d9db707d827cb6c84bf901'

- The GitHub driver now supports the :attr:`pipeline.require.<github source>.merged`
  requirement.

.. releasenotes/notes/role-in-json-4bc0d862066a4390.yaml @ b'91f10d21bdfd09891d382b800debeb8142b605f0'

- The json log now also contains the role name and the uuid
  similar to the task entry.


.. _zuul_3.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/override-file-matchers-128731229d551d81.yaml @ b'6ddf3dbb9c7b185010c56e2fa42b694e33839009'

- Files (and irrelevant-files) matchers are now overridable.  Zuul
  now uses only branch matchers to collect job variants.  Once those
  variants are collected, they are combined, and the files and
  irrelevant-files attributes are inherited and overridden as any
  other job attribute.  The final values are used to determine
  whether the job should ultimately run.

.. releasenotes/notes/override-file-matchers-128731229d551d81.yaml @ b'6ddf3dbb9c7b185010c56e2fa42b694e33839009'

- Zuul now uses Ansible 2.5.


.. _zuul_3.1.0_Security Issues:

Security Issues
---------------

.. releasenotes/notes/override-file-matchers-128731229d551d81.yaml @ b'6ddf3dbb9c7b185010c56e2fa42b694e33839009'

- Tobias Henkel (BMW Car IT GmbH) discovered a vulnerability which
  is fixed in this release. If nodes become offline during the
  build, the no_log attribute of a task is ignored. If the
  unreachable error occurred in a task used with a loop variable
  (e.g., with_items), the contents of the loop items would be
  printed in the console. This could lead to accidentally leaking
  credentials or secrets. MITRE has assigned CVE-2018-12557 to this
  vulnerability.


.. _zuul_3.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/whitelist-zuul-return-bd78bf3e598e85f6.yaml @ b'331650718160a7e667b8753477a58a777abe3d31'

- Untrusted playbooks no longer see 'Executing local code is prohibited' when
  using the zuul_return Ansible task.


.. _zuul_3.0.3:

3.0.3
=====

.. _zuul_3.0.3_New Features:

New Features
------------

.. releasenotes/notes/project-config-e906138042e386f7.yaml @ b'c7904bc0b58bf0bac3c8119f9444ffab3e788fce'

- The :attr:`project.default-branch` option is now documented.  It has been
  supported since version 3.0.0, but was omitted from the documentation.

.. releasenotes/notes/project-regex-cb782f699eb10865.yaml @ b'20d33278846361a5ebe5b7c8721dfa0c0de98523'

- Project stanzas now support regex matching of :attr:`project.name`.
  This can be used to apply project pipelines to many projects at once.


.. _zuul_3.0.3_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/project-config-e906138042e386f7.yaml @ b'c7904bc0b58bf0bac3c8119f9444ffab3e788fce'

- The ``merge-mode`` and ``default-branch`` attributes may no longer appear
  in a :ref:`project-template` stanza.


.. _zuul_3.0.3_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/config-memory-e849097ee171a534.yaml @ b'93124758363940034b6618a31b875f985fb6cba1'

- Configuration loading for dynamic configuration changes (i.e.,
  changes to ``zuul.yaml`` files) is now significantly more CPU and
  memory efficient, incurring only a slight penalty compared to
  normal changes.


.. _zuul_3.0.2:

3.0.2
=====

.. _zuul_3.0.2_New Features:

New Features
------------

.. releasenotes/notes/github-regex-status-26ddf3e3c91d182f.yaml @ b'f003cd000323077350cb0596ad134f0364c928b8'

- The GitHub trigger status filter
  :value:`pipeline.trigger.<github source>.action.status` and pipeline
  requirements :attr:`pipeline.require.<github source>.status` now support
  regular expression matching.


.. _zuul_3.0.2_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/github-regex-status-26ddf3e3c91d182f.yaml @ b'f003cd000323077350cb0596ad134f0364c928b8'

- The ``fb-re2`` python library is added as a dependency; this may
  required the installation of the ``re2`` library and header files
  in order to build.


.. _zuul_3.0.2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/reporters-always-report-27702c27369176da.yaml @ b'1a03f7e689115b2fe56da9bf9edbba4ac859e50e'

- Story 2001441 is fixed. Failure by one Zuul reporter will not short
  circuit the reporting of other reporters. This ensures as much
  information as possible is reported for each change even if some
  failures occur. Note that the build set status is changed to 'ERROR'
  after the first failed reporter.

.. releasenotes/notes/zuul-changes-fix-6d1be83959d451ce.yaml @ b'559af7048bc8029cf120d09bb2ed0b74577bc28c'

- The zuul-changes.py script has been adapted to the new zuul-web api routes.


.. _zuul_3.0.1:

3.0.1
=====

.. _zuul_3.0.1_New Features:

New Features
------------

.. releasenotes/notes/git-remote-refs-71bd2fc2bb05155d.yaml @ b'88f796435d304a05fb7d9ee08798fa287e818e9f'

- Git repositories will have a ``origin`` remote with refs pointing to the
  previous change in the speculative state.
  
  This allows jobs to determine the commits that are part of a change, which
  was not possible before. The remote URL is set to a bogus value which
  won't work with git commands that need to talk to the remote repository.

.. releasenotes/notes/postgres-ae4f8594d0f4b256.yaml @ b'68727f6c0262181e4ba70b0ec757823c1847bbeb'

- PostgreSQL is now officially supported as database backend.
  See :attr:`<sql connection>` on how to configure database connections.

.. releasenotes/notes/tenant-from-script-e28d736001db5365.yaml @ b'109766afb25c42f4bce840a050ea01d379228c4b'

- A new option for the scheduler
  :attr:`scheduler.tenant_config_script` can be used to tell Zuul to
  execute a script and read its yaml output as the tenants
  configuration. The option is exclusive with the
  :attr:`scheduler.tenant_config` option.


.. _zuul_3.0.1_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/version-table-prefix-c6a5e84851268f4d.yaml @ b'56fc36dd60062a00e10dfbc0c268595290cd6f98'

- The alembic version table is fixed to being prefixed too. This is necessary
  when using :attr:`<sql connection>.table_prefix`. However if you are
  already using ``table_prefix`` you will need to rename the table
  ``alembic_version`` to ``<prefix>alembic_version`` before starting Zuul.
  Otherwise zuul will try to create the tables again and fail. If you're not
  using ``table_prefix`` you can safely ignore this.


.. _zuul_3.0.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/role-checkouts-89632d2ff5eb8b78.yaml @ b'd0a3567221011eda22c9b42645887e5eb623e308'

- Zuul role repository checkouts now honor :attr:`job.override-checkout`.
  
  Previously, when a Zuul role was specified for a job, Zuul would
  usually checkout the master branch, unless that repository
  appeared in the dependency chain for a patch.  It will now follow
  the usual procedure for determining the branch to check out,
  including honoring :attr:`job.override-checkout` options.
  
  This may alter the behavior of currently existing jobs.  Depending
  on circumstances, you may need to set
  :attr:`job.override-checkout` or copy roles to other branches of
  projects.

