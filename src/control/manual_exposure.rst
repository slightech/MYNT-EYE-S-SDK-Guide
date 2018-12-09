.. _manual_exposure:

启用手动曝光及其调节
======================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

启用手动曝光，就是设定 ``Option::EXPOSURE_MODE`` 为 ``1`` 。手动曝光时，可调节的设定有：

* ``Option::BRIGHTNESS`` 亮度，或者说期望亮度。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // manual-exposure: 1
  api->SetOptionValue(Option::EXPOSURE_MODE, 1);

  // brightness/exposure_time: range [0,240], default 120
  api->SetOptionValue(Option::BRIGHTNESS, 120);

  LOG(INFO) << "Enable manual-exposure";
  LOG(INFO) << "Set BRIGHTNESS to " << api->GetOptionValue(Option::BRIGHTNESS);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_manual_exposure
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/manual_exposure.cc:35 Enable manual-exposure
  I/manual_exposure.cc:36 Set BRIGHTNESS to 120

样例程序会显示图像，左上角有真实曝光时间，单位毫秒。

完整代码样例，请见 `manual_exposure.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/manual_exposure.cc>`_ 。
