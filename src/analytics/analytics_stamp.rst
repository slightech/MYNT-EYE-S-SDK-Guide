.. _analytics_stamp:

分析时间戳 ✓
============

SDK 提供了时间戳分析的脚本 ``stamp_analytics.py`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-SDK-2/tree/master/tools>`_ 。

参考运行命令及结果，于 Linux 上：

.. code-block:: bash

  $ python tools/analytics/stamp_analytics.py -i dataset -c tools/config/mynteye/mynteye_config.yaml
  stamp analytics ...
    input: dataset
    outdir: dataset
  open dataset ...
  save to binary files ...
    binimg: dataset/stamp_analytics_img.bin
    binimu: dataset/stamp_analytics_imu.bin
    img: 1007, imu: 20040

  rate (Hz)
    img: 25, imu: 500
  sample period (s)
    img: 0.04, imu: 0.002

  diff count
    imgs: 1007, imus: 20040
    imgs_t_diff: 1006, imus_t_diff: 20039

  diff where (factor=0.1)
    imgs where diff > 0.04*1.1 (0)
    imgs where diff < 0.04*0.9 (0)
    imus where diff > 0.002*1.1 (0)
    imus where diff < 0.002*0.9 (0)

  image timestamp duplicates: 0

  save figure to:
    dataset/stamp_analytics.png
  stamp analytics done

分析结果图会保存进数据集目录，参考如下：

.. image:: ../../images/stamp_analytics.png

另外，脚本具体选项可执行 ``-h`` 了解：

.. code-block:: bash

  $ python tools/analytics/stamp_analytics.py -h
