.. _slam_orb_slam2:

`ORB_SLAM2 <https://github.com/raulmur/ORB_SLAM2>`_ 如何整合 
==============================================================


在MYNT® EYE 上运行 ORB_SLAM2 ，请依照这些步骤：
------------------------------------------------

* 1. 下载 `MYNT-EYE-SDK-2 <https://github.com/slightech/MYNT-EYE-SDK-2.git>`_ 及安装。
* 2. 添加 MYNT-EYE-SDK 路径到环境变量。打开 ``.bashrc`` 文件，在最后添加：export MYNTEYE_SDK2_ROOT=MYNT-EYE-SDK-2_INSTALL_PATH 。
* 3. 按照一般步骤安装 ORB_SLAM2。
* 4. 更新 ``distortion_parameters`` 和 ``projection_parameters`` 参数到 ``<ORB_SLAM2>/config/mynteye_*.yaml``。
* 5. 在MYNT® EYE 上运行例子。

双目样例
---------

* 按照 `ROS-StereoCalibration  <http://wiki.ros.org/camera_calibration/Tutorials/StereoCalibration>`_ 或 OpenCV 校准双目摄像头，并在 ``<ORB_SLAM2>/config/mynteye_stereo.yaml`` 中更新参数。

* 运行脚本 `build.sh` ：

.. code-block:: bat
 
  chmod +x build.sh
  ./build.sh

* 依照下面样式运行双目样例：

.. code-block:: bat

  ./Examples/Stereo/stereo_mynt ./Vocabulary/ORBvoc.txt ./config/mynteye_stereo.yaml true /mynteye/left/image_raw /mynteye/right/image_raw


ROS下创建单目和双目节点
------------------------

* 添加 ``Examples/ROS/ORB_SLAM2`` 路径到环境变量 ``ROS_PACKAGE_PATH`` 。打开 ``.bashrc`` 文件，在最后添加下面命令行。 ``PATH`` 为当前 ``ORB_SLAM2`` 存放路径:

.. code-block:: bat

  export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM2/Examples/ROS

* 运行脚本 `build_ros.sh` ：

.. code-block:: bat
 
  chmod +x build_ros.sh
  ./build_ros.sh

Mono_ROS 例子
~~~~~~~~~~~~~~

  * 在 ``<ORBSLAM2>/config/mynteye_mono.yaml`` 里更新 ``distortion_parameters`` 和 ``projection_parameters`` 参数

.. code-block:: bat

  cd MYNT-EYE-SDK-2

  ./samples/_output/bin/tutorials/get_img_params

这时获得针孔模型下 ``distortion_parameters`` 和 ``projection_parameters`` 参数，更新到 ``<ORBSLAM2>/config/mynteye_mono.yaml`` 中。

  * 运行 ORB_SLAM2 ``Mono_ROS`` 例子

.. code-block:: bat
 
  rosrun ORB_SLAM2 mynteye_mono ./Vocabulary/ORBvoc.txt ./config/mynteye_mono.yaml /mynteye/left/image_raw

Stereo_ROS 例子
~~~~~~~~~~~~~~~~

  * 按照 `ROS-StereoCalibration  <http://wiki.ros.org/camera_calibration/Tutorials/StereoCalibration>`_ 或 OpenCV 校准双目摄像头，并在 ``<ORB_SLAM2>/config/mynteye_stereo.yaml`` 中更新参数。

  * 运行 ORB_SLAM2 ``Stereo_ROS`` 例子

.. code-block:: bat

  rosrun ORB_SLAM2 ros_mynteye_stereo ./Vocabulary/ORBvoc.txt ./config/mynteye_stereo.yaml true /mynteye/left/image_raw /mynteye/right/image_raw
