.. _save_params:

保存设备信息和参数
====================

SDK 提供了保存信息和参数的工具 ``save_all_infos`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-S-SDK/tree/master/tools>`_ 。

参考运行命令：

.. code-block:: bash

  ./tools/_output/bin/writer/save_all_infos

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./tools/_output/bin/writer/save_all_infos
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/save_all_infos.cc:39 Save all infos to "config/SN07C60A190009071F"

默认会保存进 ``<workdir>/config`` 目录。你也可以加参数，指定保存到其他目录。

保存内容如下：

.. code-block:: none

  <workdir>/
  └─config/
     └─SN07C60A190009071F/
        ├─device.info
        ├─img.params
        └─imu.params
