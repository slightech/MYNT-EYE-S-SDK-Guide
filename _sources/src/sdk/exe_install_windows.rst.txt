.. _sdk_exe_install_windows:

Windows SDK exe 安装
=====================

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

下载并安装 SDK
---------------

.. tip::

  下载地址： mynteye-s-2.2.2-rc1-win-x64-opencv-3.4.3.exe `Google Drive <https://drive.google.com/file/d/1taQeWZyvaXwBIQOG8KOfFayda8kPWDgj>`_ `百度网盘 <https://pan.baidu.com/s/1X-intyUdQEMnaj9LEKC3nw>`_ 。

安装完 SDK 的 exe 安装包后，桌面会生成 SDK 根目录的快捷方式。

进入 ``<SDK_ROOT_DIR>\bin\samples\tutorials`` 目录，双击 ``get_stereo.exe`` 运行，即可看到双目实时画面。

生成样例工程
------------

首先，安装好 `Visual Studio 2017 <https://visualstudio.microsoft.com/>`_ 和 `CMake <https://cmake.org/>`_ 。

接着，进入 ``<SDK_ROOT_DIR>\samples`` 目录， 双击 ``generate.bat`` 即可生成样例工程。

p.s. 样例教程，可见 `SDK <https://slightech.github.io/MYNT-EYE-S-SDK/>`_ 主页给出的 Guide 文档。

如何于 Visual Studio 2017 下使用 SDK
------------------------------------

进入 ``<SDK_ROOT_DIR>\projects\vs2017`` ，见 ``README.md`` 说明。
