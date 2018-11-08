.. _save_params:

保存设备信息和参数
====================

SDK 提供了保存信息和参数的工具 ``save_all_infos`` 。工具详情可见 `tools/README.md <https://github.com/slightech/MYNT-EYE-S-SDK/tree/master/tools>`_ 。

参考运行命令：

.. code-block:: bash

  ./tools/_output/bin/writer/save_all_infos

  # Windows
  .\tools\_output\bin\writer\save_all_infos.bat

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./tools/_output/bin/writer/save_all_infos
  I0512 21:40:08.687088  4092 utils.cc:26] Detecting MYNT EYE devices
  I0512 21:40:09.366693  4092 utils.cc:33] MYNT EYE devices:
  I0512 21:40:09.366734  4092 utils.cc:37]   index: 0, name: MYNT-EYE-S1000
  I0512 21:40:09.366757  4092 utils.cc:43] Only one MYNT EYE device, select index: 0
  I0512 21:40:09.367609  4092 save_all_infos.cc:38] Save all infos to "config/SN0610243700090720"

默认会保存进 ``<workdir>/config`` 目录。你也可以加参数，指定保存到其他目录。

保存内容如下：

.. code-block:: none

  <workdir>/
  └─config/
     └─SN0610243700090720/
        ├─device.info
        ├─img.params
        └─imu.params
