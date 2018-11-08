.. _sdk_install_ros:

ROS 安装
==========

.. only:: html

  =============== ===============
  ROS Kinetic     ROS Indigo
  =============== ===============
  |build_passing| |build_passing|
  =============== ===============

  .. |build_passing| image:: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat

.. only:: latex

  =============== ===============
  ROS Kinetic     ROS Indigo
  =============== ===============
  ✓               ✓
  =============== ===============

环境准备
--------

* `ROS <http://www.ros.org/>`_

ROS Kinetic (Ubuntu 16.04)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  wget https://raw.githubusercontent.com/oroca/oroca-ros-pkg/master/ros_install.sh && \
  chmod 755 ./ros_install.sh && bash ./ros_install.sh catkin_ws kinetic

ROS Indigo (Ubuntu 14.04)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  wget https://raw.githubusercontent.com/oroca/oroca-ros-pkg/master/ros_install.sh && \
  chmod 755 ./ros_install.sh && bash ./ros_install.sh catkin_ws indigo

编译代码
--------

.. code-block:: bash

  cd <sdk>
  make ros

运行节点
--------

.. code-block:: bash

  source wrappers/ros/devel/setup.bash
  roslaunch mynt_eye_ros_wrapper mynteye.launch

运行节点，同时打开 RViz 预览：

.. code-block:: bash

  source wrappers/ros/devel/setup.bash
  roslaunch mynt_eye_ros_wrapper display.launch

测试服务
--------

运行节点，有提供获取设备信息服务，如下测试：

.. code-block:: bash

  $ source wrappers/ros/devel/setup.bash
  $ rosrun mynt_eye_ros_wrapper get_device_info.py
  LENS_TYPE: 0000
  SPEC_VERSION: 1.0
  NOMINAL_BASELINE: 120
  HARDWARE_VERSION: 2.0
  IMU_TYPE: 0000
  SERIAL_NUMBER: 0610243700090720
  FIRMWARE_VERSION: 2.0
  DEVICE_NAME: MYNT-EYE-S1000

常见问题 - ROS Indigo
----------------------

``make ros`` 时 ``libopencv`` 找不到
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  make[3]: *** No rule to make target `/usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8', needed by `/home/john/Workspace/MYNT-EYE-S-SDK/wrappers/ros/devel/lib/libmynteye_wrapper.so'.  Stop.

**Solution 1)** 安装 OpenCV 2:

.. code-block:: bash

  sudo apt-get update
  sudo apt-get install libcv-dev

**Solution 2)** 安装 OpenCV 3 并重编 ``cv_bridge``:

.. code-block:: bash

  sudo apt-get install ros-indigo-opencv3

  git clone https://github.com/ros-perception/vision_opencv.git
  mv vision_opencv/cv_bridge/ MYNT-EYE-S-SDK/wrappers/ros/src/

然后，重新 ``make ros`` 。

结语
----

关于如何使用，请阅读 :ref:`wrapper_ros` 。
