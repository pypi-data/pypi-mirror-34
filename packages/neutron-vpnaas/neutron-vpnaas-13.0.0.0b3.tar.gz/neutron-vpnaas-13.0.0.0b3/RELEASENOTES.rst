==============
neutron-vpnaas
==============

.. _neutron-vpnaas_13.0.0.0b3:

13.0.0.0b3
==========

.. _neutron-vpnaas_13.0.0.0b3_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/drivers-removal-944ce5e75d55b449.yaml @ eadee693a90845e27ddbfb898592fc56e1bed682

- The following drivers are removed due to the lack of maintainers of the drivers ``CiscoCsrIPsecDriver``, ``FedoraStrongSwanDriver``, ``VyattaIPsecDriver``. Please refer the following `mailing list post <http://lists.openstack.org/pipermail/openstack-dev/2018-February/127793.html>`_ for more detail.


.. _neutron-vpnaas_13.0.0.0b3_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/libreswan-driver-works-with-3.19+-7e1fc79ac6c7efe5.yaml @ b6c8ea8a3cca39bb4138bc7063569352faeb612f

- The libreswan driver of neutron-vpnaas can now also work with Libreswan 3.19+ (bug `#1711456 <https://launchpad.net/bugs/1711456>`_).


.. _neutron-vpnaas_13.0.0.0b1:

13.0.0.0b1
==========

.. _neutron-vpnaas_13.0.0.0b1_Prelude:

Prelude
-------

.. releasenotes/notes/Enable-sha384-and-sha512-auth-algorithms-for-Swan-drivers-9897b96f90737a20.yaml @ 03b6cc81876df2423c17532b8f2e0ef2bbb6a84b

Enable sha384 and sha512 auth algorithms for \*Swan drivers


.. _neutron-vpnaas_13.0.0.0b1_New Features:

New Features
------------

.. releasenotes/notes/Enable-sha384-and-sha512-auth-algorithms-for-Swan-drivers-9897b96f90737a20.yaml @ 03b6cc81876df2423c17532b8f2e0ef2bbb6a84b

- Users can now specify sha384 and sha512 as the auth algorithm for both IKE policy and IPsec policy, when using \*Swan IPsec drivers.

