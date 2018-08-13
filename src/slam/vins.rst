.. _slam_vins:

`VINS-Mono <https://github.com/HKUST-Aerial-Robotics/VINS-Mono>`_ 如何整合
============================================================================


在 MYNT® EYE 上运行 VINS-Mono，请依照这些步骤：
------------------------------------------------

1. 下载 `MYNT-EYE-SDK-2 <https://github.com/slightech/MYNT-EYE-SDK-2.git>`_ 及安装 mynt_eye_ros_wrapper。
2. 按照一般步骤安装 VINS-Mono 。
3. 在 `这里 <https://github.com/slightech/MYNT-EYE-VINS-Sample/blob/sdk2/config/mynteye/mynteye_config.yaml>`__ 更新 ``distortion_parameters`` 和 ``projection_parameters`` 参数。
4. 运行 mynt_eye_ros_wrapper 和 VINS-Mono 。

快捷安装 ROS Kinetic (若已安装，请忽略)
---------------------------------------

.. code-block:: bash

  cd ~
  wget https://raw.githubusercontent.com/oroca/oroca-ros-pkg/master/ros_install.sh && \
  chmod 755 ./ros_install.sh && bash ./ros_install.sh catkin_ws kinetic

安装 MYNT-EYE-VINS-Sample
--------------------------

.. code-block:: bash

  mkdir -p ~/catkin_ws/src
  cd ~/catkin_ws/src
  git clone -b sdk2 https://github.com/slightech/MYNT-EYE-VINS-Sample.git
  cd ..
  catkin_make
  source devel/setup.bash
  echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
  source ~/.bashrc

获取图像校准参数
----------------

使用 MYNT® EYE 的左目摄像头和 IMU 。通过 `MYNT-EYE-SDK-2 <https://github.com/slightech/MYNT-EYE-SDK-2.git>`_ API的 ``GetIntrinsics()`` 函数和 ``GetExtrinsics()`` 函数，可以获得当前工作设备的图像校准参数：

.. code-block:: bash

  cd MYNT-EYE-SDK-2
  ./samples/_output/bin/tutorials/get_img_params

这时，可以获得针孔模型下的 ``distortion_parameters`` 和 ``projection_parameters`` 参数，然后在 `这里 <https://github.com/slightech/MYNT-EYE-VINS-Sample/blob/sdk2/config/mynteye/mynteye_config.yaml>`__ 更新。

在 MYNT® EYE 上运行 VINS-Mono
-----------------------------

.. code-block:: bash

  cd ~/catkin_ws
  roslaunch mynt_eye_ros_wrapper mynteye.launch
  roslaunch vins_estimator mynteye.launch

.. note::

  如果使用鱼眼相机模型，点击 `这里 <https://github.com/slightech/MYNT-EYE-VINS-Sample/tree/sdk2/calibration_images>`_ 。
