.. _sdk_source_install_ubuntu:

Ubuntu SDK 源码安装
=====================

.. only:: html

  =============== ===============
  Ubuntu 16.04    Ubuntu 14.04
  =============== ===============
  |build_passing| |build_passing|
  =============== ===============

  .. |build_passing| image:: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat

.. only:: latex

  =============== ===============
  Ubuntu 16.04    Ubuntu 14.04
  =============== ===============
  ✓               ✓
  =============== ===============

.. tip::

  如果是其他 Linux 发行版，不是用的 ``apt-get`` 包管理工具，那你准备依赖时不能 ``make init`` 自动安装，得自己手动安装了。必要安装项如下：

  ============= =====================================================================
  Linux         How to install required packages
  ============= =====================================================================
  Debian based  sudo apt-get install build-essential cmake git libv4l-dev
  Red Hat based sudo yum install make gcc gcc-c++ kernel-devel cmake git libv4l-devel
  Arch Linux    sudo pacman -S base-devel cmake git v4l-utils
  ============= =====================================================================

.. ::

  `Installation of System Dependencies <https://github.com/LuaDist/Repository/wiki/Installation-of-System-Dependencies>`_

获取代码
--------

.. code-block:: bash

  sudo apt-get install git
  git clone https://github.com/slightech/MYNT-EYE-SDK-2.git

准备依赖
--------

.. code-block:: bash

  cd <sdk>
  make init

* `OpenCV <https://opencv.org/>`_

.. tip::

  OpenCV 如何编译安装，请见官方文档 `Installation in Linux <https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html>`_ 。或参考如下命令：

  .. code-block:: bash

    [compiler] sudo apt-get install build-essential
    [required] sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    [optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

    $ git clone https://github.com/opencv/opencv.git
    $ cd opencv/
    $ git checkout tags/3.4.1

    $ mkdir _build
    $ cd _build/

    $ cmake \
    -DCMAKE_BUILD_TYPE=RELEASE \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    \
    -DWITH_CUDA=OFF \
    \
    -DBUILD_DOCS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_PERF_TESTS=OFF \
    ..

    $ make -j4
    $ sudo make install

编译代码
--------

.. tip::

  如果 OpenCV 安装到了自定义目录或想指定某一版本，编译前可如下设置路径：

  .. code-block:: bash

    # OpenCV_DIR 为 OpenCVConfig.cmake 所在目录
    export OpenCV_DIR=~/opencv

  不然， CMake 会提示找不到 OpenCV 。如果不想依赖 OpenCV ，请阅读 :ref:`sdk_without_opencv` 。

编译并安装：

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
