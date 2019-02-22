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

  $ sudo add-apt-repository ppa:slightech/mynteye2
  $ sudo apt-get update
  $ sudo apt-get install mynteye2

运行样例
----------

.. tip::

  samples 路径: /opt/mynteye/samples; tools 路径: /opt/mynteye/tools

.. code-block:: bash

  $ cd /opt/mynteye/samples
  $ ./api/camera_a