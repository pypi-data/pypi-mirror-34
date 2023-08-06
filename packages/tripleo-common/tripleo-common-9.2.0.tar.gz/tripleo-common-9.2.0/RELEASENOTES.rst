==============
tripleo-common
==============

.. _tripleo-common_9.2.0:

9.2.0
=====

.. _tripleo-common_9.2.0_New Features:

New Features
------------

.. releasenotes/notes/config-download-consistent-work-dir-b8a37550c3970722.yaml @ 81b022ce03a83f4764e88b7fbf0e002d67f79546

- The config_download_deploy workflow now uses a consistent working directory for the config-download directory. Since the directory is now managed by git, it can be reused across executions.

.. releasenotes/notes/config-download-git-repo-9a18681afbfb9136.yaml @ cb6c10c8cdbc3224225be100104e9942be33dfbd

- Initialize a git repository in the config-download directory and
  automatically snapshot changes made to the repository.

.. releasenotes/notes/config-download-git-repo-commit-msg-9a550daaae1fc55e.yaml @ ec40eb3edf1bc7b56d3698c18adf37fc79fb548c

- The GetOvercloudConfig action now sets a commit message that indicates the config was downloaded by the Mistral action and what user/project were used to execute the action.

.. releasenotes/notes/config-download-git-repo-commit-msg-9a550daaae1fc55e.yaml @ ec40eb3edf1bc7b56d3698c18adf37fc79fb548c

- Since the config download directory is now managed by git, the GetOvercloudConfig action will now first download the existing config container (default of overcloud-config), so that the git history is preserved and new changes will reuse the same git repo. Each new change to the config-download directory creates a new git commit.

.. releasenotes/notes/deployment-status-workflows-7f6ba3b69f805f06.yaml @ 6a9f9239331568a727f55aaee248d6764f8e3557

- New workflows are added for manipulating the deployment status, including tripleo.deployment.v1.set_deployment_status_success, tripleo.deployment.v1.set_deployment_status_failed, and tripleo.deployment.v1.set_deployment_status_deploying.

.. releasenotes/notes/generate-roles-with-colon-c903826db084b8a6.yaml @ 088ccf774410331349cca54785edfeb6d59186ae

- Generating roles_data.yaml file has been enhanced to generate the defined
  roles's properties with a differnet name, so that a cluster can have
  multiple roles with same set of service, without manual edit. Adds the
  support to provide role name input as ``Compute:ComputeA`` so that the
  role ``ComputeA`` can be generated from the defined role ``Compute``, by
  only chaning the name.

.. releasenotes/notes/nova_metadata_config_image-26e727263be52408.yaml @ 3ea9f95d304eca1b894ea0538cdd30cc1ff2518c

- We are changing nova metadata api to be served via httpd wsgi. Therefore
  we'll have a new config volume for the nova_metadata container.
  
  Adding DockerNovaMetadataConfigImage for this.


.. _tripleo-common_9.2.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/rm_create_default_deployment_plan-397b259f6f641ab9.yaml @ a0222c16e449bae8d3a7f87cfdad2bb5944c573f

- The tripleo.plan_management.v1.create_default_deployment_plan workflow
  has been removed, since it's been deprecated since the pike release and
  is no longer used in TripleO.  Any other users of this workflow should
  switch to tripleo.plan_management.v1.create_deployment_plan instead.


.. _tripleo-common_9.2.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/ironic-ucs-driver-node-uniqueness-fix-c74110a9728d1023.yaml @ ea50e58eb6c4d0aab9d79a531a3644fd136993c5

- Un-deprecated `pm_service_profile` option support at the UCS ironic
  driver.


.. _tripleo-common_9.2.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-update-roles-workflow-with-custom-overcloud-names-35404ceae3ac380e.yaml @ b6c68814197ec18d3d489e0f0c49664f34f27296

- The tripleo.plan_management.v1.update_roles workflow didn't pass the plan
  name (container name) or Zaqar queue name to the sub-workflow it triggered.
  This caused the behaviour to be incorrect when using a name other than the
  default. It now correctly passes on these parameters.

.. releasenotes/notes/ironic-ucs-driver-node-uniqueness-fix-c74110a9728d1023.yaml @ ea50e58eb6c4d0aab9d79a531a3644fd136993c5

- Previously, ironic nodes that only differ in `pm_service_profile`
  or `ucs_service_profile` would override one another ultimately leaving
  just one of them in ironic configuration. This fix un-deprecates
  `pm_service_profile` option support at the UCS ironic driver.


.. _tripleo-common_9.1.0:

9.1.0
=====

.. _tripleo-common_9.1.0_New Features:

New Features
------------

.. releasenotes/notes/adds-create-container-workflow-77ee4557779563c0.yaml @ 2d0116d79bf39d2f3014df0bb411c0635e55bd3d

- Adds a workflow to create a container so the underlying action does
  not need to be called directly.

.. releasenotes/notes/adds-generate-fencing-parameters-e2ea121247779db3.yaml @ 2c7fb29c163d4db111becc086b9e9d09ae99d0f5

- Add a workflow to generate fencing parameters so action
  tripleo.parameters.generate_fencing does not need to be called directly.

.. releasenotes/notes/allow-upload-big-files-f67ff35fcd166612.yaml @ 13f2704c8ef74694fe3ec92cd7f30c111e4571a8

- Allow uploading files bigger than 5GB to swift.
  Currently we have support for uploading files
  to swift using the swift client class, this class
  does not allow to upload files bigger than 5GB.
  This change enables the upload of files bigger than
  5GB by using the swift service class and adjusting
  the headers to allow this operations. This new helper
  will be used for the Undercloud backup, to be able to
  store files bigger than 5GB.

.. releasenotes/notes/create-overcloudrc-workflow-e5150b6b0af462f0.yaml @ 471ca8c24e0344657e71709933ed790387a7cec3

- Adds a workflow to generate the overcloudrc files in a given deployment
  so the tripleo.deployment.overcloudrc action does not need to be called
  directly.

.. releasenotes/notes/enrich-nodes-json-ironic-port-data-0905da3f7b13d149.yaml @ 4603ef678fc7e8eb438170a1cb54a7ffe7bbfb70

- Adds support to specify additional parameters for Bare Metal ports when
  registering nodes.
  
  The  ``mac`` key in nodes_json (instackenv.json) is replaced by the new
  ``ports`` key. Each port-entry supports the following keys: ``address``,
  ``physical_network`` and ``local_link_connection``. (The keys in ``ports``
  mirror a subset off the `Bare Metal service API <https://developer.openstack.org/api-ref/baremetal/#ports-ports>`_
  .)
  
  Example specifying port mac address only::
  
    "ports": [
      {
        "address": "52:54:00:87:c8:2e"
      }
    ]
  
  Example specifying additional parameters::
  
    "ports": [
      {
        "address": "52:54:00:87:c8:2f",
        "physical_network": "network",
        "local_link_connection": {
          "switch_info": "switch",
          "port_id": "gi1/0/11",
          "switch_id": "a6:18:66:33:cb:49"
        }
      }
    ]

.. releasenotes/notes/install-octavia-amphora-image-red-hat-bc8545e36d88f951.yaml @ 411514dea3f993f3c49a4415582f2afdbce857d2

- Install Octavia amphora image on the undercloud if Red Hat.

.. releasenotes/notes/ironic-rescue-ce08f432ccdcece4.yaml @ 1e6fa0bfb0c77a1b29e4de6c989a227a11a6b156

- Sets ``rescue_kernel`` and ``rescue_ramdisk`` to the same values as
  ``deploy_kernel`` and ``deploy_ramdisk`` on node enrollment or
  configuration.

.. releasenotes/notes/ironic-rescue-ce08f432ccdcece4.yaml @ 1e6fa0bfb0c77a1b29e4de6c989a227a11a6b156

- Adds support for ``rescue_interface`` when enrolling nodes.

.. releasenotes/notes/no-classic-drivers-d56f8c3ff15af2c3.yaml @ 274b2d32532ea214a1aeac1baefa9aba87427fe1

- On enrollment, all classic drivers are replaced with their hardware type
  equivalents (e.g. ``pxe_ipmitool`` is replaced with ``ipmi``).
  The ``fake_pxe`` classic driver is replaced with the ``manual-management``
  hardware type (which must be enabled in the undercloud).

.. releasenotes/notes/octavia-amphora-ssh-5dee3678d7b66476.yaml @ bd710fd838896431b25a24e767e43043ed00062e

- Create keypair for SSH access to Octavia amphorae.

.. releasenotes/notes/prepare-includes-0c9a077369e99619.yaml @ 5640ca8cbabc87621956f2792217e8bac4fc920b

- ContainerImagePrepare entries can now take an `includes` option, which like
  `excludes` will take a list of regex patterns. `includes` will filter
  entries which do not match at least one of the include expressions.

.. releasenotes/notes/releasenotes/notes/update-lb-mgmt-subnet-to-class-b-1cd832ef08a30c85.yaml @ aa226f970bfff360471f070ab151ce820735efcd

- Enhance lb-mgmt-subnet to be a class B subnet, so the global amount of Octavia loadbalancers won't be constrained to a very low number.


.. _tripleo-common_9.1.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/enrich-nodes-json-ironic-port-data-0905da3f7b13d149.yaml @ 4603ef678fc7e8eb438170a1cb54a7ffe7bbfb70

- The ``mac`` key in nodes_json is replaced by ``ports``. The ``ports`` key
  expect a list of dictionaries specifying ``address`` (mac address), and
  optional keys  ``physical_network`` and ``local_link_connection``.

.. releasenotes/notes/fencing-hw-types-fddcdb6bf6d79414.yaml @ 812d7e6cbb899983311001d90d6608a0c90f74a5

- The ``os_auth`` argument to the ``generate_fencing_parameters`` workflow
  is deprecated and should not be provided. It will be removed in a future
  version.


.. _tripleo-common_9.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/derive-parameters-using-scheduler-hints-5bb65bc78c1f6f91.yaml @ e25e8564a42d1074034a76da5412bea4fb77b414

- Fix `bug 1760659 <https://bugs.launchpad.net/tripleo/+bug/1760659>`__ by updating the derived parameters workflow to use scheduler hints associated with a given role. The scheduler hints are used to identify overcloud nodes associated with the role, and take precedence over nodes identified by their profile/flavor.

.. releasenotes/notes/fencing-hw-types-fddcdb6bf6d79414.yaml @ 812d7e6cbb899983311001d90d6608a0c90f74a5

- Fixes handling hardware types (new-style Ironic drivers) when generating
  fencing parameters. Also completely removes support for no longer existing
  ``pxe_ssh`` driver.

.. releasenotes/notes/fix-octavia-image-rpm-install-permissions-846cd6780a527084.yaml @ b2e6edfc26994fed6bc9b56e0b70ba82545a7c06

- Fix Octavia amphora image RPM install on undercloud node for Red Hat based deployments (`bug 1772880 <https://bugs.launchpad.net/tripleo/+bug/1772880>`)

.. releasenotes/notes/fix-octavia-pub-key-d195fbf1976a8d36.yaml @ 8a69b692c4bdf3b5b7b32907ea8f117c194058b3

- Check pub key file permissions and default to pub key data for Octavia.

.. releasenotes/notes/fix-syntax-error-in-octavia-undercloud-role-c02b0c5b0f1ece34.yaml @ 8a69b692c4bdf3b5b7b32907ea8f117c194058b3

- Fix syntax error in octavia-undercloud role.


.. _tripleo-common_9.0.1:

9.0.1
=====

.. _tripleo-common_9.0.1_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/config-download-dont-use-tmpdirs-3641db9fd687f85e.yaml @ f8aa548ca692e330bdc47bf32b3f1c309e50d45c

- ``openstack overcloud config download`` now writes directly to the
  directory specified by ``--config-dir``. The directory contents will be
  overwritten, preserving any contents not originating from the stack. A
  ``--no-preserve-config`` option is provided which will cause the
  ``--config-dir`` to be deleted and recreated if the``--config-dir``
  location exists. Tmpdirs are no longer used.


.. _tripleo-common_9.0.0:

9.0.0
=====

.. _tripleo-common_9.0.0_New Features:

New Features
------------

.. releasenotes/notes/adds-list-plan-workflow-c0c6f91c9460a09a.yaml @ 1f58a968f49229fec2dec0d6c6fd69d3e99c28e1

- Adds a workflow to list deployment plans so the tripleo.plan.list action
  does not need to be called directly.

.. releasenotes/notes/role-specific-validation-5ea0a31711ced6fe.yaml @ 8586cc1542e894e52767507e1ec87f3d9ac95e03

- Added role-specific parameter validation workflow.

.. releasenotes/notes/update-params-workflow-b26fd4cc40549537.yaml @ b265e2e7b0f530be8523e69fe7b336366b5be2a4

- Adds a workflow to update the parameters in a given deployment plan so the
  tripleo.parameters.update action does not need to be called directly.


.. _tripleo-common_9.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/deprecate-list-roles-action-12744cee0e6d70e5.yaml @ 29d5b5aa8fed35b35a327fc44de1db15a871b8db

- The tripleo.roles.list action is deprecated.  Please use the
  tripleo.plan_management.v1.list_roles workflow instead.  Calling actions
  directly is no longer supported.


.. _tripleo-common_9.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/change-odl-healthcheck-uri-84d6dea51b110772.yaml @ 9e72a429d1ae1d6be2e747a973be6b6c072cd630

- Modifies the healthcheck for OpenDaylight to a supported URL. See
  https://bugs.launchpad.net/tripleo/+bug/1751857

.. releasenotes/notes/fix-opendaylight-healthcheck-f9bc1d2e067c4680.yaml @ 737439aab51089c27e71137fc30388a87474dc25

- Fixes OpenDaylight healthcheck for TLS and regular deployments.


.. _tripleo-common_9.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/use-hostnames-in-inventory-6d1a3572baebf509.yaml @ 5822ccc62027c5905115120632b4d1622cea7a01

- The inventory code is updated to use hostnames as the host alias. Since the hostname may not always be resolvable, ansible_host is added as a hostvar and set to the host's IP address. Using hostnames produces a much more user friendly result in the ansible output showing task result and play recap.

