==========
virtualbmc
==========

.. _virtualbmc_1.4.0:

1.4.0
=====

.. _virtualbmc_1.4.0_New Features:

New Features
------------

.. releasenotes/notes/add-client-server-overhaul-c5b6f8c01126b4a3.yaml @ b'047a77d7ded61a97c8a10750ccaf409973ebb866'

- Changes the design of the VirtualBMC tool. Instead of forking the
  ``vbmc`` command-line tool to become a daemon and serve a single
  libvirt domain, the ``vbmcd`` master process and ``vbmc`` command-line
  client have been introduced. These client-server tools communicate
  over the ZeroMQ queue. The ``vbmcd`` process is responsible for
  herding its children, each child still serves a single libvirt
  domain.

.. releasenotes/notes/add-client-server-overhaul-c5b6f8c01126b4a3.yaml @ b'047a77d7ded61a97c8a10750ccaf409973ebb866'

- The ``vbmc start`` command now supports multiple domains.


.. _virtualbmc_1.4.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/add-client-server-overhaul-c5b6f8c01126b4a3.yaml @ b'047a77d7ded61a97c8a10750ccaf409973ebb866'

- It is advised to invoke ``vbmcd`` master process on system boot,
  perhaps by a systemd unit file.


.. _virtualbmc_1.4.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/add-client-server-overhaul-c5b6f8c01126b4a3.yaml @ b'047a77d7ded61a97c8a10750ccaf409973ebb866'

- Deprecates automatically starting up the ``vbmcd`` daemon process if
  it is not running. This backward-compatibility feature will be removed
  in the OpenStack Stein release.


.. _virtualbmc_1.4.0_Security Issues:

Security Issues
---------------

.. releasenotes/notes/add-client-server-overhaul-c5b6f8c01126b4a3.yaml @ b'047a77d7ded61a97c8a10750ccaf409973ebb866'

- Hardens PID file creation to prevent the symlink attack.

