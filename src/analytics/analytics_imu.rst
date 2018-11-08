.. _analytics_imu:

分析 IMU
==========

SDK 提供了 IMU 分析的脚本 ``imu_analytics.py`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-S-SDK/tree/master/tools>`_ 。

参考运行命令及结果，于 Linux 上：

.. code-block:: bash

  $ python tools/analytics/imu_analytics.py -i dataset -c tools/config/mynteye/mynteye_config.yaml -al=-1.2,1.2 -gl= -gdu=d -gsu=d -kl=
  imu analytics ...
    input: dataset
    outdir: dataset
    gyro_limits: None
    accel_limits: [(-1.2, 1.2), (-1.2, 1.2), (-1.2, 1.2), (-1.2, 1.2)]
    time_unit: None
    time_limits: None
    auto: False
    gyro_show_unit: d
    gyro_data_unit: d
    temp_limits: None
  open dataset ...
    imu: 20040, temp: 20040
    timebeg: 4.384450, timeend: 44.615550, duration: 40.231100
  save figure to:
    dataset/imu_analytics.png
  imu analytics done

分析结果图会保存进数据集目录，参考如下：

.. image:: ../../images/imu_analytics.png

另外，脚本具体选项可执行 ``-h`` 了解：

.. code-block:: bash

  $ python tools/analytics/imu_analytics.py -h
