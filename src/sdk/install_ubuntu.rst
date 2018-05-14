.. _sdk_install_ubuntu:

Ubuntu 安装 ✓
=============

=============== ===============
Ubuntu 16.04    Ubuntu 14.04
=============== ===============
|build_passing| |build_passing|
=============== ===============

.. |build_passing| image:: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat

获取代码
--------

.. code-block:: bash

  git clone https://github.com/slightech/MYNT-EYE-SDK-2.git

准备依赖
--------

.. code-block:: bash

  cd <sdk>
  make init

* `OpenCV <https://opencv.org/>`_

编译代码
--------

编译前，可在系统终端（Windows 命令提示符）里如下指定 OpenCV 路径，其为 ``OpenCVConfig.cmake`` 目录：

.. code-block:: bash

  # Linux, macOS
  export OpenCV_DIR=~/opencv

  # Windows
  set OpenCV_DIR=C:\opencv

然后，编译并安装：

.. code-block:: bash

  cd <sdk>
  make install

最终，默认会安装在 ``<sdk>/_install`` 目录。

编译样例
--------

.. code-block:: bash

  cd <sdk>
  make samples

运行样例：

.. code-block:: bash

  ./samples/_output/bin/api/camera_a

  # Windows
  .\samples\_output\bin\api\camera_a.bat

教程样例，请阅读 :ref:`data` 和 :ref:`ctrl` 。

编译工具
--------

.. code-block:: bash

  cd <sdk>
  make tools

安装脚本依赖：

.. code-block:: bash

  cd <sdk>/tools/
  sudo pip install -r requirements.txt

工具和脚本的使用，后续会有介绍。

结语
----

工程要引入 SDK 的话，CMake 可参考 ``samples/CMakeLists.txt`` 里的配置。不然，就是直接引入安装目录里的头文件和动态库。
