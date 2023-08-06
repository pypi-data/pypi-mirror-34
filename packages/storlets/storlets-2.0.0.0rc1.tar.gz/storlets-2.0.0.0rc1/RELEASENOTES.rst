========
storlets
========

.. _storlets_2.0.0.0rc1:

2.0.0.0rc1
==========

.. _storlets_2.0.0.0rc1_Known Issues:

Known Issues
------------

.. releasenotes/notes/2_0_0-e987cd43729edf86.yaml @ b'201f2b99411ee78af1882fc550166aa58d4b1d8a'

- Secure container isolation for Storlets environment is still an ongoing
  work. Storlets enables user-defined code to run on the OpenStack Swift
  node with Docker container isolation level but a malicious user would run
  any attacking code there using recent vulnerability. Using more secure
  container like kata may mitigate such a risk of vulnerability.

.. releasenotes/notes/2_0_0-e987cd43729edf86.yaml @ b'201f2b99411ee78af1882fc550166aa58d4b1d8a'

- Support user function written by py3 (current runner only supports python2 env)


.. _storlets_2.0.0.0rc1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/2_0_0-e987cd43729edf86.yaml @ b'201f2b99411ee78af1882fc550166aa58d4b1d8a'

- Fix all python Storlets daemon processes as py3 compatible.

.. releasenotes/notes/2_0_0-e987cd43729edf86.yaml @ b'201f2b99411ee78af1882fc550166aa58d4b1d8a'

- Switch test runner from testr to stestr

.. releasenotes/notes/2_0_0-e987cd43729edf86.yaml @ b'201f2b99411ee78af1882fc550166aa58d4b1d8a'

- Other various minor bug fixes

