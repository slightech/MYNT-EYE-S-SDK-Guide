.. _analytics_stamp:

分析时间戳
============

SDK 提供了时间戳分析的脚本 ``stamp_analytics.py`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-S-SDK/tree/master/tools>`_ 。

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

.. tip::

  录制数据集时建议 ``record.cc`` 里注释显示图像 ``cv::imshow()``， ``dataset.cc`` 里注释存储图像 ``cv::imwrite()`` 。因为此些操作都比较耗时，可能会导致丢弃图像。换句话说就是消费赶不上生产，所以丢弃了部分图像。 ``record.cc`` 里用的 ``GetStreamDatas()`` 仅缓存最新的 4 张图像。
