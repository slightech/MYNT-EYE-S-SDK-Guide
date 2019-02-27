.. _sdk_ppa_install_ubuntu:

Ubuntu SDK PPA 安装
=====================

.. only:: html

  =============== =============== ===============
  Ubuntu 14.04    Ubuntu 16.04    Ubuntu 18.04
  =============== =============== ===============
  |build_passing| |build_passing| |build_passing|
  =============== =============== ===============

  .. |build_passing| image:: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat

.. only:: latex

  =============== =============== ===============
  Ubuntu 14.04    Ubuntu 16.04    Ubuntu 18.04
  =============== =============== ===============
  ✓               ✓               ✓
  =============== =============== ===============

PPA安装
---------

.. code-block:: bash

  $ sudo add-apt-repository ppa:slightech/mynt-eye-s-sdk
  $ sudo apt-get update
  $ sudo apt-get install mynt-eye-s-sdk

运行样例
----------

.. tip::

  samples 路径: /opt/mynt-eye-s-sdk/samples; tools 路径: /opt/mynt-eye-s-sdk/tools

.. code-block:: bash

  $ cd /opt/mynt-eye-s-sdk/samples
  $ ./api/camera_a