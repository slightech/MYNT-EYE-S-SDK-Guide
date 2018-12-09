.. _auto_exposure:

启用自动曝光及其调节
======================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

启用自动曝光，就是设定 ``Option::EXPOSURE_MODE`` 为 ``0`` 。自动曝光时，可调节的设定有：

* ``Option::MAX_GAIN`` 最大增益。
* ``Option::MAX_EXPOSURE_TIME`` 最大曝光时间。
* ``Option::DESIRED_BRIGHTNESS`` 期望亮度。
* ``Option::MIN_EXPOSURE_TIME`` 最小曝光时间。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);
  if (!api)
    return 1;
  api->SetStreamRequest(Format::BGR888, FrameRate::RATE_30_FPS);

  // auto-exposure: 0
  api->SetOptionValue(Option::EXPOSURE_MODE, 0);

  // max_gain: range [0,255], default 8
  api->SetOptionValue(Option::MAX_GAIN, 8);
  // max_exposure_time: range [0,1000], default 333
  api->SetOptionValue(Option::MAX_EXPOSURE_TIME, 333);
  // desired_brightness: range [1,255], default 122
  api->SetOptionValue(Option::DESIRED_BRIGHTNESS, 122);
  // min_exposure_time: range [0,1000], default 0
  api->SetOptionValue(Option::MIN_EXPOSURE_TIME, 0);

  LOG(INFO) << "Enable auto-exposure";
  LOG(INFO) << "Set MAX_GAIN to " << api->GetOptionValue(Option::MAX_GAIN);
  LOG(INFO) << "Set MAX_EXPOSURE_TIME to "
            << api->GetOptionValue(Option::MAX_EXPOSURE_TIME);
  LOG(INFO) << "Set DESIRED_BRIGHTNESS to "
            << api->GetOptionValue(Option::DESIRED_BRIGHTNESS);
  LOG(INFO) << "Set MIN_EXPOSURE_TIME to "
            << api->GetOptionValue(Option::MIN_EXPOSURE_TIME);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_auto_exposure
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/auto_exposure.cc:41 Enable auto-exposure
  I/auto_exposure.cc:42 Set MAX_GAIN to 8
  I/auto_exposure.cc:43 Set MAX_EXPOSURE_TIME to 333
  I/auto_exposure.cc:45 Set DESIRED_BRIGHTNESS to 122
  I/auto_exposure.cc:47 Set MIN_EXPOSURE_TIME to 0

样例程序会显示图像，左上角有真实曝光时间，单位毫秒。

完整代码样例，请见 `auto_exposure.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/auto_exposure.cc>`_ 。
