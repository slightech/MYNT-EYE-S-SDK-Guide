.. _manual_exposure:

启用手动曝光及其调节
======================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

启用手动曝光，就是设定 ``Option::EXPOSURE_MODE`` 为 ``1`` 。手动曝光时，可调节的设定有：

* ``Option::GAIN`` 增益。
* ``Option::BRIGHTNESS`` 亮度，或者说曝光时间。
* ``Option::CONTRAST`` 对比度，或者说黑电平校准。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // manual-exposure: 1
  api->SetOptionValue(Option::EXPOSURE_MODE, 1);

  // gain: range [0,48], default 24
  api->SetOptionValue(Option::GAIN, 24);
  // brightness/exposure_time: range [0,240], default 120
  api->SetOptionValue(Option::BRIGHTNESS, 120);
  // contrast/black_level_calibration: range [0,255], default 127
  api->SetOptionValue(Option::CONTRAST, 127);

  LOG(INFO) << "Enable manual-exposure";
  LOG(INFO) << "Set GAIN to " << api->GetOptionValue(Option::GAIN);
  LOG(INFO) << "Set BRIGHTNESS to " << api->GetOptionValue(Option::BRIGHTNESS);
  LOG(INFO) << "Set CONTRAST to " << api->GetOptionValue(Option::CONTRAST);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_manual_exposure
  I0513 14:09:17.104431 31908 utils.cc:26] Detecting MYNT EYE devices
  I0513 14:09:17.501519 31908 utils.cc:33] MYNT EYE devices:
  I0513 14:09:17.501551 31908 utils.cc:37]   index: 0, name: MYNT-EYE-S1000
  I0513 14:09:17.501562 31908 utils.cc:43] Only one MYNT EYE device, select index: 0
  I0513 14:09:17.552918 31908 manual_exposure.cc:37] Enable manual-exposure
  I0513 14:09:17.552953 31908 manual_exposure.cc:38] Set GAIN to 24
  I0513 14:09:17.552958 31908 manual_exposure.cc:39] Set BRIGHTNESS to 120
  I0513 14:09:17.552963 31908 manual_exposure.cc:40] Set CONTRAST to 127

样例程序会显示图像，左上角有真实曝光时间，单位毫秒。

完整代码样例，请见 `manual_exposure.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/control/manual_exposure.cc>`_ 。
