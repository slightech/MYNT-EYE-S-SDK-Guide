.. _write_imu_params:

写入 IMU 标定参数 ✓
===================

SDK 提供了写入 IMU 标定参数的工具 ``imu_params_writer`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-SDK-2/tree/master/tools>`_ 。

有关如何获取，请阅读 :ref:`get_imu_params` 。

参考运行命令：

.. code-block:: bash

  ./tools/_output/bin/writer/imu_params_writer tools/writer/config/imu.params

  # Windows
  .\tools\_output\bin\writer\imu_params_writer.bat tools\writer\config\imu.params

其中， `tools/writer/config/imu.params <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/tools/writer/config/imu.params>`_ 是参数文件路径。如果你自己标定了参数，可以编辑此文件，然后执行上述命令写入设备。

.. warning::

  请不要随意覆写参数。另外 ``save_all_infos`` 工具可帮你备份参数。
