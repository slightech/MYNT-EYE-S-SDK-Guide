.. _sdk_install_windows:

Windows 安装
==============

.. only:: html

  +-----------------+
  | Windows 10      |
  +=================+
  | |build_passing| |
  +-----------------+

  .. |build_passing| image:: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat

.. only:: latex

  +-----------------+
  | Windows 10      |
  +=================+
  | ✓               |
  +-----------------+

.. tip::

  Windows 不直接提供 Visual Studio ``*.sln`` 工程文件，需要用 CMake 来构建生成。一是 CMake 跨平台、易配置、可持续维护，二是第三方代码（glog, OpenCV）也都是用的 CMake 构建。

.. tip::

  目前暂未提供二进制安装程序，需要你从源码编译。也是配置开发环境的过程。

前提条件
--------

CMake（提供构建）
~~~~~~~~~~~~~~~~~

* `CMake <https://cmake.org/download/>`_，用于构建编译（必要）。
* `Git <https://git-scm.com/downloads>`_，用于获取代码（可选）。
* `Doxygen <http://www.stack.nl/~dimitri/doxygen/download.html>`_，用于生成文档（可选）。

安装好上述工具后，在命令提示符（Command Prompt）里确认可运行此些命令：

.. code-block:: bat

  >cmake --version
  cmake version 3.10.1

  >git --version
  git version 2.11.1.windows.1

  >doxygen --version
  1.8.13

Visual Studio（提供编译）
~~~~~~~~~~~~~~~~~~~~~~~~~

* `Visual Studio <https://www.visualstudio.com/>`_

  * `Visual Studio 2017 <https://my.visualstudio.com/Downloads?q=Visual Studio 2017>`_
  * `Visual Studio 2015 <https://my.visualstudio.com/Downloads?q=Visual Studio 2015>`_

* `Windows 10 SDK <https://developer.microsoft.com/en-US/windows/downloads/windows-10-sdk>`_

安装好 Visual Studio 后，在其 Visual Studio Command Prompt 里确认可运行如下命令：

.. code-block:: bat

  >cl
  Microsoft (R) C/C++ Optimizing Compiler Version 19.14.26429.4 for x86

  >msbuild
  Microsoft (R) 生成引擎版本 15.7.179.6572

.. tip::

  Visual Studio Command Prompt 可以从开始菜单打开，

  .. image:: ../../images/vs_cmd_menu.png
    :width: 30%

  也可以从 Visual Studio 的工具菜单里打开，

  .. image:: ../../images/vs_cmd.png
    :width: 40%

  但如 Visual Studio 2015 工具菜单里可能没有，可以自己添加个。

  打开 Tools 的 External Tools… ，然后 Add 如下内容：

  ================= =======================================================================================
  Field             Value
  ================= =======================================================================================
  Title             Visual Studio Command Prompt
  Command           ``C:\Windows\System32\cmd.exe``
  Arguments         ``/k "C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\VsDevCmd.bat"``
  Initial Directory ``$(SolutionDir)``
  ================= =======================================================================================

  Visual Studio Command Prompt 里就可以用编译命令 ``cl`` ``link`` ``lib`` ``msbuild`` 等，

  .. image:: ../../images/vs_cmd_test.png

MSYS2（提供 Linux 命令）
~~~~~~~~~~~~~~~~~~~~~~~~

* `MSYS2 <http://www.msys2.org/>`_

  * `国内镜像 <https://lug.ustc.edu.cn/wiki/mirrors/help/msys2>`_
  * `pacman <https://wiki.archlinux.org/index.php/pacman>`_

安装后，确认系统环境变量 ``PATH`` 里添加了如下路径：

.. code-block:: none

    C:\msys64\usr\bin

然后，打开 MSYS2 MSYS ，执行更新并安装 ``make`` ：

.. code-block:: bash

  $ pacman -Syu
  $ pacman -S make

最终，命令提示符（Command Prompt）里可运行如下命令：

.. code-block:: bat

  >make --version
  GNU Make 4.2.1

获取代码
--------

.. code-block:: bat

  git clone https://github.com/slightech/MYNT-EYE-SDK-2.git

准备依赖
--------

.. code-block:: bat

  >cd <sdk>
  >make init
  Make init
  Init deps
  Install cmd: pacman -S
  Install deps: git clang-format
  pacman -S clang-format (not exists)
  error: target not found: clang-format
  pip install --upgrade autopep8 cpplint pylint requests
  ...
  Init git hooks
  ERROR: clang-format-diff is not installed!
  Expect cmake version >= 3.0
  cmake version 3.10.1

* `OpenCV <https://opencv.org/>`_

.. tip::

  OpenCV 官方提供了 ``exe`` 进行安装。如果想从源码编译，请见官方文档 `Installation in Windows <https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html>`_ 。或参考如下命令：

  .. code-block:: bat

    >git clone https://github.com/opencv/opencv.git
    >cd opencv
    >git checkout tags/3.4.1

    >cd opencv
    >mkdir _build
    >cd _build

    >cmake ^
    -D CMAKE_BUILD_TYPE=RELEASE ^
    -D CMAKE_INSTALL_PREFIX=C:/opencv ^
    -D WITH_CUDA=OFF ^
    -D BUILD_DOCS=OFF ^
    -D BUILD_EXAMPLES=OFF ^
    -D BUILD_TESTS=OFF ^
    -D BUILD_PERF_TESTS=OFF ^
    -G "Visual Studio 15 2017 Win64" ^
    ..

    >msbuild ALL_BUILD.vcxproj /property:Configuration=Release
    >msbuild INSTALL.vcxproj /property:Configuration=Release

编译代码
--------

.. tip::

  如果 OpenCV 安装到了自定义目录或想指定某一版本，编译前可如下设置路径：

  .. code-block:: bat

    # OpenCV_DIR 为 OpenCVConfig.cmake 所在目录
    set OpenCV_DIR=C:\opencv

  不然， CMake 会提示找不到 OpenCV 。如果不想依赖 OpenCV ，请阅读 :ref:`sdk_without_opencv` 。

编译并安装：

.. code-block:: bat

  cd <sdk>
  make install

最终，默认会安装在 ``<sdk>/_install`` 目录。

编译样例
--------

.. code-block:: bat

  cd <sdk>
  make samples

运行样例：

.. code-block:: bat

  .\samples\_output\bin\api\camera_a.bat

教程样例，请阅读 :ref:`data` 和 :ref:`ctrl` 。

.. tip::

  所有编译出的样例程序 ``exe`` 都会有个相应的 ``bat`` 。 ``bat`` 会临时设定下系统环境变量，然后再运行 ``exe`` 。所以建议执行 ``bat`` 运行程序。

  如果直接运行 ``exe`` 的话，可能会报 ``dll`` 找不到。说明你需要将 ``<sdk>\_install\bin`` ``%OPENCV_DIR%\bin`` 加入到系统环境变量 ``PATH`` 里。

  OpenCV 如何设定环境变量，可见官方文档 `Set the OpenCV environment variable and add it to the systems path <https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html#tutorial_windows_install_path>`_ 。

编译工具
--------

.. code-block:: bat

  cd <sdk>
  make tools

工具和脚本的使用，后续会有介绍。

.. tip::

  脚本为 Python 实现，需要先安装 Python 及其包管理工具 pip ，然后再如下安装依赖：

  .. code-block:: bat

    cd <sdk>\tools
    pip install -r requirements.txt

  注：MSYS2 里也带了 Python ，但测试未能安装上 matplotlib 。

结语
----

工程要引入 SDK 的话，CMake 可参考 ``samples/CMakeLists.txt`` 里的配置。不然，就是直接引入安装目录里的头文件和动态库。
