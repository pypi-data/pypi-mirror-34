=======
bifrost
=======

.. _bifrost_5.1.0:

5.1.0
=====

.. _bifrost_5.1.0_New Features:

New Features
------------

.. releasenotes/notes/change-ipa-version-cacaec52a55188cc.yaml @ b'7792531443642823f666ae06566af4e077bc8734'

- By adding extra variable ``-e ipa_upstream_release=stable-mitaka`` for instance,
  the deployment can now use all ramdisk and kernel images available in
  https://tarballs.openstack.org/ironic-python-agent/tinyipa/files/
  instead of the default ``master``.
  
  Furthermore, as some of these files do not have any .sha256
  checksum associated to them, the downloading of these file
  is now just issuing a "warning" and is not reported as an
  Ansible error in the final summary.

.. releasenotes/notes/custom-partitioning-78d7ac12d80a993f.yaml @ b'17a232ad04967beb4e9787783d9a538a5160ff41'

- Custom partitioning YAML file can now be specified using partitioning_file
  variable which contains a path to the YAML file describing the partitions
  layout. For example:
  
  .. code-block:: yaml
  
      - local_loop:
          name: image0
      - partitioning:
          base: image0
          label: mbr
          partitions:
            - name: root
              flags: [ boot,primary ]
              size: 6G
              mkfs:
                type: xfs
                label: "img-rootfs"
                mount:
                  mount_point: /
                  fstab:
                    options: "rw,relatime"
                    fck-passno: 1
            - name: tmp
              size: 1G
              mkfs:
                type: xfs
                mount:
                  mount_point: /tmp
                  fstab:
                      options: "rw,nosuid,nodev,noexec,relatime"
            - name: var
              size: 7G
              mkfs:
                type: xfs
                mount:
                  mount_point: /var
                  fstab:
                    options: "rw,relatime"
            - name: log
              size: 5G
              mkfs:
                type: xfs
                mount:
                  mount_point: /var/log
                  fstab:
                    options: "rw,relatime"
            - name: home
              size: 1G
              mkfs:
                type: xfs
                mount:
                  mount_point: /home
                  fstab:
                    options: "rw,nodev,relatime"
  
  
  For more informations please refer to the following links:
  `Disk Image Layout Section <https://docs.openstack.org/diskimage-builder/latest/user_guide/building_an_image.html#disk-image-layout>`_
  `Standard Partitioning <http://teknoarticles.blogspot.fr/2017/07/build-and-use-security-hardened-images.html>`_
  `LVM Partitioning <http://teknoarticles.blogspot.fr/2017/11/security-hardened-images-with-volumes.html>`_

.. releasenotes/notes/populate_ntp_servers_dnsmasq-249d2a26b94b0bf1.yaml @ b'bbce94c783003846d7c049adb5d5b5b925751529'

- Allow to populate the NTP servers setting of dnsmasq. This is optional, but if ``dnsmasq_ntp_servers``setting is set, it adds a ``dhcp-option=42,dnsmasq_ntp_servers`` to the generated dnsmasq configuration for bifrost.

.. releasenotes/notes/store-introspection-data-bc4f2fef2f5bb543.yaml @ b'507228a22877c5a4af8c9c7668c228f1c967fa78'

- Stores introspection data in nginx.
  
  In the absence of swift, we can now use the bifrost nginx web server -
  masquerading as an object store - to store raw and processed introspection
  data for nodes.  This is configured via the boolean variable
  ``inspector_store_data_in_nginx`` and is enabled by default.


.. _bifrost_5.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/no-classic-drivers-0b8a346bcab8a004.yaml @ b'212d25a364f338203075a39bb5010a9ec52e7c9c'

- The deprecated support for classic drivers has been removed.


.. _bifrost_5.1.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/populate_ntp_servers_dnsmasq-249d2a26b94b0bf1.yaml @ b'bbce94c783003846d7c049adb5d5b5b925751529'

- When configuring the ``dnsmasq_ntp_servers`` setting, several NTP servers can be specified, separated by commas.

