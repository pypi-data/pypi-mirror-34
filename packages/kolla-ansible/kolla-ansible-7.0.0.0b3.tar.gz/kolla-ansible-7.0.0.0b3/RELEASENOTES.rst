=============
kolla-ansible
=============

.. _kolla-ansible_7.0.0.0b3:

7.0.0.0b3
=========

.. _kolla-ansible_7.0.0.0b3_Prelude:

Prelude
-------

.. releasenotes/notes/kolla-ceph-bluestore-b48673a85dda06d1.yaml @ b'3591d0fa9f3211bcc707bb0fc652a8fb33545dcb'

Since Ceph Luminous release, bluestore OSDs are recommended. Kolla Ceph currently only supports filestore. Bluestore is required in Kolla Ceph.


.. _kolla-ansible_7.0.0.0b3_New Features:

New Features
------------

.. releasenotes/notes/add-forks-flag-faf0d27618265bd4.yaml @ b'7321fe772d702f6446c7dd25de00dc01cbedb8d0'

- Adds a new argument to the ``kolla-ansible`` command, ``--forks NUM``.
  This argument is passed through directly to ``ansible-playbook``.

.. releasenotes/notes/add-monasca-log-persister-f4da4370a0c5777e.yaml @ b'5441963c9a25257e67d63762d993aaf07d9a1b4c'

- Add support for deploying the Monasca Log Persister. The Log
  Persister is responsible for reading logs from the Kafka processed
  logs topic and writing them to Elasticsearch.

.. releasenotes/notes/add-monasca-log-transformer-80d985fc77603478.yaml @ b'9c88262ad93f224c2fd057373a491362f7176ba0'

- Add support for deploying the Monasca Log Transformer for
  providing log standardisation in Monasca.

.. releasenotes/notes/allow-disabling-nova-ssh-51028805f163e5a2.yaml @ b'6781c181347553e02a001aff3960ac9ede035978'

- Add a configuration option `enable_nova_ssh` to allow disabling the
  service. This is useful when an operator is not supporting cold-migration
  and does not want to manage additional SSH keys.

.. releasenotes/notes/allow-external-swift-as-glance-backend-242a6dbf7c830d7a.yaml @ b'07dfc20292059583217900cbec78838ba954dd26'

- Allow overriding the variable `glance_backend_swift` to enable the swift
  backend for glance, without requiring swift to be enabled in kolla-ansible.
  This allows operators to enable an external swift endpoint as the glance
  backend.

.. releasenotes/notes/expire-mariadb-bin-logs-c3df2b87460ca807.yaml @ b'f450dd9779202e699a7d7858bc0ccf6946af51f0'

- Automatically expire MariaDB binary logs after 14 days.

.. releasenotes/notes/implement-ironic-rolling-upgrade-c45536fe4814212e.yaml @ b'0152e51d7ee0de38377ea81cba6c5ec18f9a861b'

- Implement Ironic rolling upgrade logic, enabled by default at
  ironic_enable_rolling_upgrade: "yes" in etc/kolla/globals.yml file.

.. releasenotes/notes/kolla-ceph-bluestore-b48673a85dda06d1.yaml @ b'3591d0fa9f3211bcc707bb0fc652a8fb33545dcb'

- Support Kolla Ceph to deploy bluestore OSDs in Rocky release.

.. releasenotes/notes/nsxv3-support-0bd45afcb7e71cc5.yaml @ b'0ef27dd07672ca4268b6ec4b5c78145b395773ac'

- Add support for the VMware NSX Transformers plugin

.. releasenotes/notes/onos-support-2ea385cceb8104d6.yaml @ b'5f3cbd8360c85213ab3e5d761a59f95ec28170a3'

- Add onos support, Networking-onos is Neutron’s sub-project to provide
  connectivity between Neutron/Neutron’s sub-project’s and ONOS.

.. releasenotes/notes/optional-sudoers-f5ea08d6f7cbed2b.yaml @ b'8ec92df8e373cdd97ebf724ca6c7b85ed6ebd608'

- Adds support for skipping the configuration of sudoers files in the
  ``kolla-ansible bootstrap-servers`` command. This depends on the
  ``create_kolla_user_sudoers`` variable, which defaults to the same value as
  ``create_kolla_user``.

.. releasenotes/notes/prometheus-alertmanager-dd6d38da2357b917.yaml @ b'1596475db6249911bc61fcf218b66cf850b657fc'

- Deploy prometheus-alertmanager (https://prometheus.io/docs/alerting/alertmanager/)
  as part of the prometheus monitoring stack.

.. releasenotes/notes/support-ceph-dashboard-3ee5e489ea16ea25.yaml @ b'fd6c9f3882074137ad4db74d8785afefa5684c4f'

- Add support for ceph-dashboard. It enables 'dashboard' module in ceph cluster.
  Its uses command 'ceph mgr module enable dashboard'.

.. releasenotes/notes/support-check-and-diff-mode-for-genconfig-97703a2ed13ab9ec.yaml @ b'1db352f007e79f33d969361fa4997b60ef04e9a6'

- Support ansible check and diff module for generate configrations. You could
  use ``EXTRA_OPTS='--check --diff' kolla-ansible genconfig`` to check what
  the configration file will be like in dry-run mode.

.. releasenotes/notes/support_ironic_neutron_agent-3eac1e71069ea845.yaml @ b'5dd080a130ba8fb5bbf1423f6d6cecc6b1fef12d'

- Add support for configuration of the Ironic Neutron Agent, and the Neutron networking-baremetal ML2 plugin.


.. _kolla-ansible_7.0.0.0b3_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/docker_insecure_registry-857bfb9c760aa3bf.yaml @ b'acfc4fd26acd007a72061adc97c9c62c06bab86b'

- Add option `docker_registry_insecure` to enable the SSL verification
  for the docker registry. Default value is true when a private
  registry is defined.


.. _kolla-ansible_7.0.0.0b3_Security Issues:

Security Issues
---------------

.. releasenotes/notes/disable_tlsv11-51d6be67d593f7ab.yaml @ b'16df54eaa532025f674cffcf7e7d2b1bde56e98f'

- Disable TLS 1.1 on haproxy for external network if
  tls is enabled.


.. _kolla-ansible_7.0.0.0b3_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-gnocchi-external-ceph-filepath-672ea7ac3c325ec2.yaml @ b'dfb5ddaad670ae60f5da92a051bdc79cf74b76ac'

- Load custom ceph.conf and keyring file from <<node_custom_config>>/gnocchi
  folder rathen than each folder of gnocchi components.


.. _kolla-ansible_7.0.0.0b2:

7.0.0.0b2
=========

.. _kolla-ansible_7.0.0.0b2_New Features:

New Features
------------

.. releasenotes/notes/add-blazar-dashboard-g6595d27c034f8xc.yaml @ b'6bda3feb6e63fe5a088a4aebe7b1521936eaac68'

- Add blazar-dashboard to horizon.

.. releasenotes/notes/add-congress-dashboard-q65x5d27c034f8xc.yaml @ b'7f11d35b0d37b745d0dd6c5f9f2a9c10927023d6'

- Add congress-dashboard to horizon.

.. releasenotes/notes/add-freezer-sceduler-b646fba6666889a1.yaml @ b'b81442a0822b012e757bcb55d59893da433c6a3e'

- Add a kolla-ansible role for freezer-scheduler

.. releasenotes/notes/add-horizon-custom-settings-file-d5dfab8a1a3b4ee7.yaml @ b'd516ad7da2d86ad03374f8244f6738ee65d6f6a4'

- The settings file ``{{ node_custom_config}}/horizon/custom_local_settings`` can be
  used in Horizon to overwrite the default local_settings without a need to sync it at image build time.

.. releasenotes/notes/add-kafka-role-ec7a9def49e06e51.yaml @ b'6647ed818a96ed8516393a684be606ddd3621f7c'

- Add a role for deploying Apache Kafka, a distributed streaming platform. See https://kafka.apache.org/ for more details. Requires Apache Zookeeper to be configured.

.. releasenotes/notes/add-monasca-api-eb536dd5a6d77563.yaml @ b'c11f9f521d5833a8dd41bfdb32c1927daa42b00c'

- Add a role for deploying the Monasca API which forms part of the Monasca distributed monitoring and logging as a service platform. See https://wiki.openstack.org/wiki/Monasca for more details.

.. releasenotes/notes/add-monasca-log-api-d47662a4e643cd7f.yaml @ b'eab66ab02ef97f8925fba414f44fd881f3745dc0'

- Add support for deploying the Monasca Log API which forms part of the Monasca distributed monitoring and logging as a service platform. See https://wiki.openstack.org/wiki/Monasca for more details.

.. releasenotes/notes/add-neutron-ipam-driver-infoblox-3621f44bb0017e91.yaml @ b'2f69b3cbc66eafaaec1920ceb85255d0f84aa6a4'

- Add support for the configuration of Infoblox as a pluggable
  IPAM driver in neutron. Configure by selecting 'infoblox' as
  the 'neutron_ipam_driver'. In addition to handling IP address
  management within neutron, an agent will be started to
  automatically manage DNS entries within the Infoblox appliance.

.. releasenotes/notes/add-octavia-dashboard-f6595d27c034f89c.yaml @ b'24f4fcdd22f8d9c5fa91c03d5448fd3885e0cc78'

- Add Octavia Horizon plugin

.. releasenotes/notes/add-trove-singletenant-dd02a7b7cc1a4f99.yaml @ b'c5b303732315e2f01e7f80a799ba91787f2881fd'

- Add "enable_trove_singletenant" option to enable the Trove single
  tenant functionnality. This feature will allow Trove to create
  Nova instances in a different tenant than the user tenant.

.. releasenotes/notes/add-zookeeper-role-9eb474f26035ec77.yaml @ b'f87b238db52353884dffd60b86dea78c5139ebd4'

- Add a role for deploying Apache Zookeeper for the purpose of supporting Apache Kafka. See https://zookeeper.apache.org/ for more details.

.. releasenotes/notes/bootstrap-servers-virtualenv-723a0e80942604bd.yaml @ b'69979efc2e75dc4ab8e8e41a7136afdb64df678d'

- Adds support for installing python dependencies into a virtualenv on remote
  hosts.
  
  Installing python packages directly to the system site-packages can cause
  various problems, in particular when pip overwrites a system package.
  Python virtualenvs are one solution to this issue, as they allow python
  packages to be installed in an isolated environment.  Typically we will
  need to enable use of system site-packages from within this virtualenv, to
  support the use of modules such as yum, apt, and selinux, which are not
  available on PyPI.
  
  The path to the virtualenv is configured via the ``virtualenv`` variable,
  and access to site-packages is controlled via ``virtualenv_site_packages``.
  The default value for ``virtualenv`` is None, in which case the old
  behaviour of installing packages directly to the system site-packages is
  maintained.
  
  When executing other kolla-ansible commands, the variable
  ``ansible_python_interpreter`` should be set to the python interpreter
  installed in ``virtualenv``. Note that this variable cannot be templated.

.. releasenotes/notes/custom_option_docker-f5b810a8edce06fa.yaml @ b'b6bab5b9318de460bb95b3cecf4e7162cae3fe6b'

- Add custom option for docker daemon by configure the docker service. An operator
  named "docker_custom_option" will be added.

.. releasenotes/notes/dvr-mode-property-13b3699f9a9c4359.yaml @ b'1c1d6e20c1629a5452bc10ddc750be169da67394'

- [`blueprint Replace inner-/external computes with a dvr mode variable <https://blueprints.launchpad.net/kolla-ansible/+spec/dvr_mode_property>`_]
  A new variable "neutron_compute_dvr_mode" is introduced. This variable
  controls whether a compute host has external connection and is
  allowed to do full-blown DVR or distributed routing is only used for
  tenant networking. Corresponding values are "dvr" and "dvr_no_external"
  The variable has to be set either globally or per group (per host)
  to get desired behavior.

.. releasenotes/notes/extra-ml2-plugins-817d0b392c06ffc7.yaml @ b'418cb52767270d85e28a6f3027c561f47b805d9d'

- Introduces support to use extra ml2 plugins non maintained
  by kolla-ansible, an operator may add a file
  ``/etc/kolla/config/neutron/plugins/awesome_plugin.ini`` and
  will be copied into ml2 plugins folder during runtime.

.. releasenotes/notes/haproxy-listen-options-ef1dc74a239f6f9d.yaml @ b'55773923b1256e03482bf6ba61e2bbfd72493cac'

- HAProxy - Add ability for operators to specify additional options per HTTP
  or TCP listener stanza.

.. releasenotes/notes/horizon-keystone-url-97dcc26389f6d025.yaml @ b'fd186a2a7c1201d5b1b2a9873770189d43d064d9'

- Introduces a new variable, horizon_keystone_url, which facilitates
  overriding the URL used by Horizon to talk to the identity service
  (Keystone).  Defaults to the identity service's internal URL.

.. releasenotes/notes/implement-glance-zero-downtime-upgrade-822fea4739beda62.yaml @ b'365e3d3a3f740f203b4691dc04c633fc2f4be0ff'

- Implement Glance zero-downtime upgrade logic.

.. releasenotes/notes/ldap-grafana-configuration-0112d84771addbe7.yaml @ b'965669b461bdc054708d349ba6f57737060c4dc0'

- Add support of custom configuration files for grafana.

.. releasenotes/notes/prometheus-dbb1aee8c88943c4.yaml @ b'4d1f37359d51687e8a96e706664ef3c309d633b2'

- Deploy prometheus (prometheus.io) as the timeseries database.
  Containers for node_exporter, haproxy_exporter and mysqld_exporter are
  provided and added to prometheus as scrape targets.

.. releasenotes/notes/support-docker-runtime-directory-set-da7e77a70626c0d1.yaml @ b'f3e19ecf7bcdb94f82e3ef6356dadf96b255d7c6'

- Set docker runtime directory by configure the docker daemon.An operator
  named "docker_runtime_directory" will be add.

.. releasenotes/notes/support-ironic-ipxe-boot-2ea7f598748403bd.yaml @ b'0a1ccc2612240ff15c255eeafc67f56835278adf'

- Adds support for booting bare metal nodes with Ironic using iPXE.
  This is enabled via the ``enable_ironic_ipxe`` flag.


.. _kolla-ansible_7.0.0.0b2_Known Issues:

Known Issues
------------

.. releasenotes/notes/reduce-ceph-pgs-27e88e3b6e3b809c.yaml @ b'36f33f089bbda9bcc7e451b69413907cce8e3bb6'

- As of Ceph Luminous 12.2.1 the maximum number of PGs per OSD before the
  monitor issues a warning has been reduced from 300 to 200 PGs. In addition,
  Ceph now fails with an error rather than a warning in the case of exeeding
  the max value.
  In order to allow Kolla to continue to be used out of the box we have
  reduced the default values for pg_num and pgp_num from 128 to 8. This will
  allow a deploy of Kolla with all possible services enabled and then some,
  with the minimum recommended three OSDs.  Operators are *highly*
  recommended to review the Ceph documentation regarding these values in
  order to ensure optimal performance for their own cluster.


.. _kolla-ansible_7.0.0.0b2_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/dvr-mode-property-13b3699f9a9c4359.yaml @ b'1c1d6e20c1629a5452bc10ddc750be169da67394'

- All hosts from "[inner-compute]" and "[external-compute]" can be moved to
  "[compute]" to avoid problems in OpenStack S release, though the groups
  still will function well in this release.

.. releasenotes/notes/merge-neutron-vpnaas-role-with-neutron-l3-agent-90b91725344dda76.yaml @ b'9fe70f45f3316b9afe0f946fc412d11aa66b6fba'

- The neutron-vpnaas-agent has been loaded just inside of the existing l3 agent
  rather than requiring operators to run a completely different binary with a
  subclass of the existing L3 agent.


.. _kolla-ansible_7.0.0.0b2_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/disable-glance-registry-fdbba9daa5169b06.yaml @ b'a155e796afca1e748a1aba749a375d92f6d95574'

- Disable glance registry as it is deprecated.

.. releasenotes/notes/dvr-mode-property-13b3699f9a9c4359.yaml @ b'1c1d6e20c1629a5452bc10ddc750be169da67394'

- Splitting of compute group into inner and external compute hosts is
  deprecated and will be removed in OpenStack S release.

.. releasenotes/notes/merge-neutron-vpnaas-role-with-neutron-l3-agent-90b91725344dda76.yaml @ b'9fe70f45f3316b9afe0f946fc412d11aa66b6fba'

- As neutron-vpnaas-agent can be loaded by the neutron l3 agent, neutron-vpnaas
  standalone mode is not supported. We have already removed the neutron-vpnaas-agent
  container, currently, there is no need to keep this role.


.. _kolla-ansible_7.0.0.0b2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/dvr-mode-property-13b3699f9a9c4359.yaml @ b'1c1d6e20c1629a5452bc10ddc750be169da67394'

- External bridge setup on compute hosts that depends on whether DVR mode
  is enabled is also accompanied by a check for the new variable.

.. releasenotes/notes/fix-ansible-warning-f9b382a13446f625.yaml @ b'c567055176648cc6e0bb4b3fd5c3a80be0374dd9'

- fixed ansible warning when using ansible>2.2

.. releasenotes/notes/fix-ansible-warning-f9b382a13446f625.yaml @ b'c567055176648cc6e0bb4b3fd5c3a80be0374dd9'

- avoid using ansible reserved action and serial word in playbooks. use kolla_action and kolla_serial instead.

.. releasenotes/notes/remove-uuid-keystone-token-provider-c3a3ba2da5fd417d.yaml @ b'84aeff4e9290a01c85677136114bda332268f9ee'

- Remove uuid option form keystone_token_provider due to it's removed in
  Keystone.

