.. _changelog:

Changelog
=========

This project adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`__
and `human-readable changelog <http://keepachangelog.com/en/1.0.0/>`__.

This file contains only general overview of the changes in the DebOps project.
The detailed changelog can be seen using :command:`git log` command.

You can read information about required changes between releases in the
:ref:`upgrade_notes` documentation.


`debops master`_ - unreleased
-----------------------------

.. _debops master: https://github.com/debops/debops/compare/v0.8.0...master


`debops v0.8.0`_ - 2018-08-06
-----------------------------

.. _debops v0.8.0: https://github.com/debops/debops/compare/v0.7.2...v0.8.0

Added
~~~~~

- New DebOps roles:

  - :ref:`debops.netbase`: manage local host and network database in
    :file:`/etc/hosts` and :file:`/etc/networks` files.

  - :ref:`debops.sudo`: install and manage :command:`sudo` configuration on
    a host. The role is included in the ``common.yml`` playbook.

  - :ref:`debops.system_groups`: configure UNIX system groups used on DebOps
    hosts. The role is included in the ``common.yml`` playbook.

  - :ref:`debops.debops_legacy`: clean up legacy files, directories, APT
    packages or :command:`dpkg-divert` diversions created by DebOps but no
    longer used. This role needs to be executed manually, it's not included in
    the main playbook.

  - :ref:`debops.python`: manage Python environment, with support for multiple
    Python versions used at the same time. The role is included in the
    ``common.yml`` playbook.

  - Icinga 2 support has been implemented with :ref:`debops.icinga`,
    :ref:`debops.icinga_db` and :ref:`debops.icinga_web` Ansible roles.

- [debops.users] Selected UNIX accounts can now be configured to linger when
  not logged in via the ``item.linger`` parameter. This allows these accounts
  to maintain long-running services when not logged in via their own private
  :command:`systemd` instances.

- [debops.sudo] You can now manage configuration files located in the
  :file:`/etc/sudoers.d/` directory using :ref:`sudo__*_sudoers <sudo__ref_sudoers>`
  inventory variables, with multiple level of conditional options.

- [debops.ntp] The OpenNTPD service will now properly integrate the
  :command:`ifupdown` hook script with :command:`systemd`. During boot, NTP
  daemon will be started once network interfaces are configured and will not
  restart multiple times on each network interface change.

- [debops.resources] The role can now generate custom files using templates,
  based on a directory structure. See :ref:`resources__ref_templates` for more
  details.

- [debops.nginx] A ``default`` set of SSL ciphers can be specified using the
  :envvar:`nginx_default_ssl_ciphers` variable. This disables the
  ``ssl_ciphers`` option in the :command:`nginx` configuration and forces the
  server to use the defaults provided by the OS.

- [debops.dhparam] The role will set up a :command:`systemd` timer to
  regenerate Diffie-Hellman parameters periodically if it's available. The
  timer will use random delay time, up to 12h, to help with mass DHparam
  generation in multiple LXC containers/VMs.

- The DebOps installation now depends on the `dnspython`__ Python library. This
  allows usage of the ``dig`` Ansible lookup plugin in DebOps roles to gather
  data via DNS SRV records.

  .. __: http://www.dnspython.org/

- The DebOps installation now depends on the `future`__ Python library which
  provides compatibility between Python 2.7 and Python 3.x environments. It is
  currently used in the custom Ansible filter plugin provided by DebOps, but
  its use will be extended to other scripts in the future to make the code more
  readable.

  .. __: http://python-future.org/

Changed
~~~~~~~

- The :command:`editor` alternative symlink configuration has been moved from
  the ``debops.console`` role to the :ref:`debops.apt_install` role which also
  installs :command:`vim` by default.

- The configuration of automatic removal of APT packages installed via
  ``Recommends:`` or ``Suggests:`` dependencies has been moved from the
  :ref:`debops.apt` role to the :ref:`debops.apt_mark` role which more closely
  reflects its intended purpose. Variable names and their default values
  changed; see the :ref:`upgrade_notes` for more details.

- [debops.owncloud] Support Nextcloud 13 and partially ownCloud 10. Nextcloud
  11 and ownCloud 9.1 are EOL, you should update. The role can help you with
  the update to ensure that everything works smoothly with the new versions.
  Currently, the role can not do the update for you.

- [debops.sshd] The role will now check the :ref:`debops.system_groups` Ansible
  local facts to define what UNIX groups are allowed to connect to the host via
  the SSH service.

- [debops.nodejs] The NPM version installed by the role from GitHub is changed
  from ``v5.4.2`` to ``latest`` which seems to be an equivalent of a stable
  branch.

- Some of the existing DebOps Policies and Guidelines have been reorganized and
  the concept of DebOps Enhancement Proposals (DEPs) is introduced, inspired by
  the `Python Enhancement Proposals`__.

.. __: https://www.python.org/dev/peps/pep-0001/

- [debops.ifupdown] The :ref:`debops.kmod` role is added as a dependency. The
  :ref:`debops.ifupdown` role will generate :command:`modprobe` configuration
  based on the type of configured network interfaces (bridges, VLANs, bonding)
  and the kernel modules will be automatically loaded if missing.

- [debops.nodejs] Recent versions of NPM `require NodeJS 6.0.0+`__ and don't
  work with other releases. Because of that the newest NPM release is not
  installable on hosts that use NodeJS packages from older OS releases.

  .. __: https://github.com/npm/npm/issues/20425

  The 'debops.nodejs' role will install NPM v5.10.0 version in this case to
  allow NPM to work correctly - on Debian Jessie, Stretch and Ubuntu Xenial.
  Otherwise, a NPM from the ``latest`` branch will be installed, as before.

- [debops.nodejs] Instead of NodeJS 6.x release, the role will now install
  NodeJS 8.x release upstream APT packages by default. This is due to the
  NodeJS 6.x release `switching to a Maintenance LTS mode`__. NodeJS 8.x will
  be supported as a LTS release until April 2019.

  .. __: https://github.com/nodejs/Release

- [debops.nodejs] The role will install upstream NodeSource APT packages by
  default. This is due to `no security support in Debian Stable`__, therefore
  an upstream packages should be considered more secure. The upstream NodeJS
  packages include a compatible NPM release, therefore it won't be separately
  installed from GitHub.

  .. __: https://www.debian.org/releases/stretch/amd64/release-notes/ch-information.en.html#libv8

  The existing installations shouldn't be affected, since the role will select
  OS/upstream package versions based on existing Ansible local facts.

- [debops.gitlab] Redesign the GitLab version management to read the versions
  of various components from the GitLab repository files instead of managing
  them manually in a YAML dictionary. The new :envvar:`gitlab__release`
  variable is used to specify desired GitLab version to install/manage.

- [debops.gitlab] The :command:`gitaly` service will be installed using the
  ``git`` UNIX account instead of ``root``. Existing installations might
  require additional manual cleanup; see the :ref:`upgrade_notes` for details.

- [debops.gitlab] The role now supports installation of GitLab 10.7.

- [debops.gitlab] The usage of :envvar:`gitlab__fqdn` variable is revamped
  a bit - it's now used as the main variable that defines the GitLab
  installation FQDN. You might need to update the Ansible inventory if you
  changed the value of the ``gitlab_domain`` variable used previously for this
  purpose.

- [debops.lxc] Redesign system-wide LXC configuration to use list of YAML
  dictionaries merged together instead of custom Jinja templates.

- [debops.lxc] Add :command:`lxc-prepare-ssh` script on the LXC hosts that can
  be used to install OpenSSH and add the user's SSH authorized keys inside of
  the LXC containers. This is a new way to prepare the LXC containers for
  Ansible/DebOps management that doesn't require custom LXC template scripts
  and can be used with different LXC container types.

- [debops.core] The role will add any new administrator accounts to the list of
  existing admin accounts instead of replacing them in the Ansible local fact
  script. This should allow for multiple administrators to easily coexist and
  run the DebOps playbooks/roles from their own accounts without issues.

- [debops.mariadb_server] [debops.mariadb] The MariaDB/MySQL server and client
  will now use the ``utf8mb4`` encoding by default instead of the ``utf8``
  which is an internal MySQL character encoding. This might impact existing
  databases, see the :ref:`upgrade_notes` for details.

- [debops.unattended_upgrades] On hosts without a domain set, the role enabled
  all upgrades, not just security updates. This will not happen anymore, the
  security updates are enabled everywhere by default, you need to enable all
  upgrades specifically via the :envvar:`unattended_upgrades__release`
  variable.

- The :command:`debops` script can now parse multiple playbook names specified
  in any order instead of just looking at the first argument passed to it.

Removed
~~~~~~~

- [debops.apt_install], [debops.auth]: don't install the ``sudo`` package by
  default, this is now done via a separate :ref:`debops.sudo` role to easily
  support switching to the ``sudo-ldap`` APT package.

- [debops.console] Remove support for copying custom files from the role. This
  functionality is covered better by the :ref:`debops.resources` role.

- [debops.console] Remove support for managing entries in the
  :file:`/etc/hosts` database. This is now covered by the :ref:`debops.netbase`
  Ansible role.

- [debops.auth] Remove configuration of UNIX system groups and accounts in the
  ``admins`` UNIX group. This is now done by the :ref:`debops.system_groups`
  Ansible role.

- [debops.bootstrap] The :command:`sudo` configuration has been removed from
  the :ref:`debops.bootstrap` role. The ``bootstrap.yml`` playbook now includes
  the :ref:`debops.sudo` role which configures :command:`sudo` service.

- [debops.bootstrap] The UNIX system group management has been removed from the
  role, the ``bootstrap.yml`` playbook now uses the :ref:`debops.system_groups`
  role to create the UNIX groups used by DebOps during bootstrapping.

- [debops.bootstrap] Remove management of Python packages from the role. The
  ``bootstrap.yml`` playbook uses the :ref:`debops.python` role to configure
  Python support on the host.

- [debops.lxc] Remove support for direct LXC container management from the
  role. This functionality is better suited for other tools like
  :command:`lxc-*` set of commands, or the Ansible ``lxc_container`` module
  which should be used in custom playbooks. The 'debops.lxc' role focus should
  be configuration of LXC support on a host.

- [debops.lxc] Remove custom LXC template support. The LXC containers can be
  created by the normal templates provided by the ``lxc`` package, and then
  configured using DebOps roles as usual.

- [debops.postgresql_server] The tasks that modified the default ``template1``
  database and its schema have been removed to make the PostgreSQL installation
  more compatible with applications packaged in Debian that rely on the
  PostgreSQL service. See the relevant commit for more details. Existing
  installations shouldn't be affected.


`debops v0.7.2`_ - 2018-03-28
-----------------------------

.. _debops v0.7.2: https://github.com/debops/debops/compare/v0.7.2...v0.7.2

Fixed
~~~~~

- Add missing ``python-ldap`` dependency as an APT package in the Dockerfile.


`debops v0.7.1`_ - 2018-03-28
-----------------------------

.. _debops v0.7.1: https://github.com/debops/debops/compare/v0.7.0...v0.7.1

Added
~~~~~

- New DebOps roles:

  - :ref:`debops.ansible`: install Ansible on a Debian/Ubuntu host using
    Ansible. The :ref:`debops.debops` role now uses the new role to install
    Ansible instead of doing it directly.

  - :ref:`debops.apt_mark`: set install state of APT packages (manual/auto) or
    specify that particular packages should be held in their current state.
    The role is included in the ``common.yml`` playbook.

  - :ref:`debops.kmod`: manage kernel module configuration and module loading
    at boot time. This role replaces the ``debops-contrib.kernel_module`` role.

  - The ``debops-contrib.etckeeper`` role has been integrated into DebOps as
    :ref:`debops.etckeeper`. The new role is included in the ``common.yml``
    playbook.

- [debops.ifupdown] The role has new tasks that manage custom hooks in other
  services. First hook is :ref:`ifupdown__ref_custom_hooks_filter_dhcp_options`
  which can be used to selectively apply DHCP options per network interface.

Changed
~~~~~~~

- [debops.lxc] The role will now generate the ``lxc-debops`` LXC template
  script from different templates, based on an OS release. This change should
  help fix the issues with LXC container creation on Debian Stretch.

- The test suite used on Travis-CI now checks the syntax of the YAML files, as
  well as Python and shell scripts included in the repository. The syntax is
  checked using the :command:`yamllint`, :command:`pycodestyle` and
  :command:`shellcheck` scripts, respectively. Tests can also be invoked
  separately via the :command:`make` command.

- [debops.etherpad] The role can now autodetect and use a PostgreSQL database
  as a backend database for Etherpad.

- [debops.pki] The X.509 certificate included in the default ``domain`` PKI
  realm will now have a SubjectAltName wildcard entry for the host's FQDN. This
  should allow for easy usage of services related to a particular host in the
  cluster over encrypted connections, for example host monitoring, service
  discovery, etc. which can be now published in the DNS zone at
  ``*.host.example.org`` resource records.

- [debops.pki] The role now supports Let's Encrypt ACMEv2 API via the
  `acme-tiny`__ Python script. The existing PKI realms will need to be
  re-created or updated for the new API to work, new PKI realms should work out
  of the box. Check the :ref:`upgrade_notes` for more details.

- [debops.proc_hidepid], [debops.lxc] The roles now use a static GID ``70`` for
  the ``procadmins`` group to synchronize the access permissions on a host and
  inside the LXC containers. You will need to remount the filesystems, restart
  services and LXC containers that rely on this functionality.

- [debops.sysctl] The configuration of the kernel parameters has been
  redesigned, instead of being based on YAML dictionaries, is now based on YAML
  lists of dictionaries and can be easily changed via Ansible inventory. You
  will need to update your inventory for the new changes to take effect, refer
  to the :ref:`role documentation <sysctl__ref_parameters>` for details.

- [debops.ferm] The role should now correctly detect what Internet Protocols
  are available on a host (IPv4, IPv6) and configure firewall only for the
  protocols that are present.

.. __: https://github.com/diafygi/acme-tiny

Fixed
~~~~~

- The :command:`debops` command will now generate the :file:`ansible.cfg`
  configuration file with correct path to the Ansible roles provided with the
  DebOps Python package.

- [debops.nginx] Fix a long standing bug in the role with Ansible failing
  during welcome page template generation with Jinja2 >= 2.9.4. It was related
  to `non-backwards compatible change in Jinja`__ that modified how variables
  are processed in a loop.

.. __: https://github.com/pallets/jinja/issues/659

Removed
~~~~~~~

- The ``debops-contrib.kernel_module`` Ansible role has been removed; it was
  replaced by the new :ref:`debops.kmod` Ansible role.

- [debops.ferm] The ``ferm-forward`` hook script in the
  :file:`/etc/network/if-pre-up.d/` directory has been removed (existing
  instances will be cleaned up). Recent changes in the :ref:`debops.ferm` role
  broke idempotency with the :ref:`debops.ifupdown` role, and it was determined
  that the functionality provided by the hook is no longer needed, recent OS
  releases should deal with it adequately.


`debops v0.7.0`_ - 2018-02-11
-----------------------------

.. _debops v0.7.0: https://github.com/debops/debops/compare/v0.6.0...v0.7.0

Added
~~~~~

- New Ansible roles have been imported from the ``debops-contrib``
  organization: ``apparmor``, ``bitcoind``, ``btrfs``, ``dropbear_initramfs``,
  ``etckeeper``, ``firejail``, ``foodsoft``, ``fuse``, ``homeassistant``,
  ``kernel_module``, ``kodi``, ``neurodebian``, ``snapshot_snapper``, ``tor``,
  ``volkszaehler``, ``x2go_server``. They are not yet included in the main
  playbook and still need to be renamed to fit with the rest of the
  ``debops.*`` roles.

- New DebOps roles:

  - :ref:`debops.sysfs`: configuration of the Linux kernel attributes through
    the :file:`/sys` filesystem. The role is not enabled by default.

  - :ref:`debops.locales`: configure localization and internationalization on
    a given host or set of hosts.

  - :ref:`debops.machine`: manage the :file:`/etc/machine-info` file,
    the :file:`/etc/issue` file and a dynamic MOTD.

  - :ref:`debops.proc_hidepid`: configure the ``/proc`` ``hidepid=`` options.

  - :ref:`debops.roundcube`: manage RoundCube Webmail application

  - :ref:`debops.prosody`: configure an xmpp server on a given host

  - :ref:`debops.sysnews`: manage System News bulletin for UNIX accounts

- You can now :ref:`use Vagrant <quick_start__vagrant>` to create an Ansible
  Controller based on Debian Stretch and use it to manage itself or other hosts
  over the network.

- You can now build an Ansible Controller with DebOps support as a Docker
  container. :ref:`Official Docker image <quick_start__docker>` is also
  available, automatically rebuilt on every commit.

- You can now install DebOps on `Arch Linux <https://www.archlinux.org/>`__
  using an included ``PKGBUILD`` file.

- Add new playbook, ``agent.yml``. This playbook is executed at the end of the
  main playbook, and contains applications or services which act as "agents" of
  other services. They may contact their parent applications to report about
  the state of the host they are executed on, therefore the agents are
  installed and configured at the end of the main playbook.

- [debops.libvirtd] The role can now detect if nested KVM is enabled in
  a particular virtual machine and install KVM support.

  [debops.nodejs] The :ref:`debops.nodejs` role can now install `Yarn
  <https://yarnpkg.com/>`_ package manager using its upstream APT repository
  (not enabled by default).

- DebOps roles and playbooks can now be tested using local or remote
  `GitLab CI <https://about.gitlab.com/>`_ instance, with Vagrant, KVM and LXC
  technologies and some custom scripts.

- DebOps roles and playbooks will be included in the Python packages released
  on PyPI. This will allow for easier installation of DebOps via :command:`pip`
  (no need to download the roles and playbooks separately) as well as simple
  stable releases. The DebOps monorepo can still be installed separately.

Changed
~~~~~~~

- [debops-tools] The :command:`debops-update` script will now install or
  update the DebOps monorepo instead of separate ``debops-playbooks`` and
  DebOps roles git repositories. Existing installations shouldn't be affected.

- [debops-tools] The :command:`debops` script will now include the DebOps
  monorepo roles and playbooks in the generated :file:`ansible.cfg`
  configuration. The monorepo roles and playbooks are preferred over the old
  ``debops-playbooks`` ones.

  The script is backwards compatible and should work correctly with or without
  the ``debops-playbooks`` repository and roles installed.

- The project repository is tested using :command:`pycodestyle` for compliance
  with Python's `PEP8 Style Guide <https://pep8.org/>`_.

- [debops.nodejs] The ``npm`` package has been removed from Debian Stable.
  The role will now install NPM using the GitHub source, unless upstream NodeJS is
  enabled, which includes its own NPM version.

- [debops.gunicorn] Update the role to work correctly on Debian Stretch and
  newer releases. The support for multiple :command:`gunicorn` instances using
  custom Debian scripts has been removed in Debian Stretch, therefore the role
  replaces it with its own setup based on :command:`systemd` instances.

- [debops.gitlab_runner] The GitLab Runner playbook is moved to the
  ``agent.yml`` playbook; it will be executed at the end of the main playbook
  and should that way include correct information about installed services.

- Improved Python 3 support in the DebOps scripts and throughout the
  playbooks/roles. DebOps should now be compatible with both Python versions.

Removed
~~~~~~~

- [DebOps playbooks] Remove the :file:`ipaddr.py` Ansible filter plugin, it is
  now included in the Ansible core distribution.

- [debops.console] Remove the ``locales`` configuration from the
  'debops.console' role, this functionality has been moved to the new
  'debops.locales' role. You will need to update the Ansible inventory
  variables to reflect the changes.

- [debops.console] Remove management of the :file:`/etc/issue` and
  :file:`/etc/motd` files from the ``debops.console`` role. That functionality
  is now available in the :ref:`debops.machine` role. You will need to update
  the Ansible inventory variables to reflect the changes.

- [debops.console] Management of the ``/proc`` ``hidepid=`` option has been
  moved to a new role, :ref:`debops.proc_hidepid`. You will need to update the
  Ansible inventory variables to reflect the changes.

- [debops.console] Management of the System News using the ``sysnews`` Debian
  package has been removed from the role; it's now available as a separate
  :ref:`debops.sysnews` Ansible role. You will need to update the Ansible
  inventory variables related to System News due to this changes.


debops v0.6.0 - 2017-10-21
--------------------------

Added
~~~~~

- Various repositories that comprise the DebOps project have been merged into
  a single monorepo which will be used as the main development repository.
  Check the :command:`git` log for information about older releases of DebOps
  roles and/or playbooks.
