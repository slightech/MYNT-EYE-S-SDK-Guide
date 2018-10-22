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

下载并安装指定版本opencv
---------------------------

`opencv-3.4.3-vc14_vc15.exe <https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.4.3/>`_

设置环境变量
--------------------
.. code-block:: bash

  设置Opencv路径: OPENCV_DIR = \<opencv>\build
  将该路径添加至PATH：%OPENCV_DIR%\x64\vc15\bin

.. tip::
  <opencv>为opencv的安装路径

下载并安装SDK
---------------

`mynteye-2.0-win-x64-opencv-3.4.3.exe <http://wiki.mynt.com/download/attachments/8028199/mynteye-2.0-win-x64-opencv-3.4.3.exe/>`_

运行样例
----------

.. code-block:: bash

  $ c:
  $ cd Program Files (x86)\Slightech\MYNT EYE SDK 2.0
  $ .\samples\bin\api\camera_a.exe

如何引用
----------
