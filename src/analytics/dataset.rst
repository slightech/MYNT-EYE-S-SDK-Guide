.. _dataset:

录制数据集
============

SDK 提供了录制数据集的工具 ``record`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-S-SDK/tree/master/tools>`_ 。

参考运行命令：

.. code-block:: bash

  ./tools/_output/bin/dataset/record2

参考运行结果，于 Linux 上：

.. code-block:: bash

  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/channels.cc:140 Option::BRIGHTNESS: min=0, max=255, def=192, cur=120
  I/channels.cc:140 Option::EXPOSURE_MODE: min=0, max=1, def=0, cur=0
  I/channels.cc:140 Option::MAX_GAIN: min=0, max=255, def=8, cur=8
  I/channels.cc:140 Option::MAX_EXPOSURE_TIME: min=0, max=1000, def=333, cur=333
  I/channels.cc:140 Option::DESIRED_BRIGHTNESS: min=1, max=255, def=122, cur=122
  I/channels.cc:140 Option::MIN_EXPOSURE_TIME: min=0, max=1000, def=0, cur=0
  I/channels.cc:140 Option::ACCELEROMETER_RANGE: min=6, max=48, def=12, cur=12
  I/channels.cc:140 Option::GYROSCOPE_RANGE: min=250, max=4000, def=1000, cur=1000
  I/channels.cc:140 Option::ACCELEROMETER_LOW_PASS_FILTER: min=0, max=2, def=2, cur=2
  I/channels.cc:140 Option::GYROSCOPE_LOW_PASS_FILTER: min=23, max=64, def=64, cur=64
  Saved 1024 imgs, 13799 imus to ./dataset
  I/record2.cc:128 Time beg: 2018-12-10 19:21:25.971245, end: 2018-12-10 19:22:00.090891, cost: 34119.6ms
  I/record2.cc:131 Img count: 1024, fps: 30.012
  I/record2.cc:133 Imu count: 13799, hz: 404.43

录制内容如下：

.. code-block:: none

  <workdir>/
  └─dataset/
     ├─left/
     │  ├─stream.txt  # Image infomation
     │  ├─000000.png  # Image，index 0
     │  └─...
     ├─right/
     │  ├─stream.txt  # Image information
     │  ├─000000.png  # Image，index 0
     │  └─...
     └─motion.txt  # IMU information
