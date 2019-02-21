.. _auto_exposure:

启用自动曝光及其调节
======================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

启用自动曝光，就是设定 ``Option::EXPOSURE_MODE`` 为 ``0`` 。

以s1030为例，自动曝光时，可调节的设定有：

* ``Option::MAX_GAIN`` 最大增益。
* ``Option::MAX_EXPOSURE_TIME`` 最大曝光时间。
* ``Option::DESIRED_BRIGHTNESS`` 期望亮度。

以s2100/s210a为例，自动曝光可调节的设定有：

* ``Option::MAX_GAIN`` 最大增益。
* ``Option::MAX_EXPOSURE_TIME`` 最大曝光时间。
* ``Option::DESIRED_BRIGHTNESS`` 期望亮度。
* ``Option::MIN_EXPOSURE_TIME`` 最小曝光时间。

参考代码片段：

s1030：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // auto-exposure: 0
  api->SetOptionValue(Option::EXPOSURE_MODE, 0);

  // max_gain: range [0,48], default 48
  api->SetOptionValue(Option::MAX_GAIN, 48);
  // max_exposure_time: range [0,240], default 240
  api->SetOptionValue(Option::MAX_EXPOSURE_TIME, 240);
  // desired_brightness: range [0,255], default 192
  api->SetOptionValue(Option::DESIRED_BRIGHTNESS, 192);

  LOG(INFO) << "Enable auto-exposure";
  LOG(INFO) << "Set MAX_GAIN to " << api->GetOptionValue(Option::MAX_GAIN);
  LOG(INFO) << "Set MAX_EXPOSURE_TIME to "
            << api->GetOptionValue(Option::MAX_EXPOSURE_TIME);
  LOG(INFO) << "Set DESIRED_BRIGHTNESS to "
            << api->GetOptionValue(Option::DESIRED_BRIGHTNESS);

s2100/s210a：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  bool ok;
  auto &&request = api->SelectStreamRequest(&ok);
  if (!ok) return 1;
  api->ConfigStreamRequest(request);

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
  LOG(INFO) << "Set EXPOSURE_MODE to "
            << api->GetOptionValue(Option::EXPOSURE_MODE);
  LOG(INFO) << "Set MAX_GAIN to " << api->GetOptionValue(Option::MAX_GAIN);
  LOG(INFO) << "Set MAX_EXPOSURE_TIME to "
            << api->GetOptionValue(Option::MAX_EXPOSURE_TIME);
  LOG(INFO) << "Set DESIRED_BRIGHTNESS to "
            << api->GetOptionValue(Option::DESIRED_BRIGHTNESS);
  LOG(INFO) << "Set MIN_EXPOSURE_TIME to "
            << api->GetOptionValue(Option::MIN_EXPOSURE_TIME);


参考运行结果，于 Linux 上：

s1030：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_auto_exposure
  I0513 14:07:57.963943 31845 utils.cc:26] Detecting MYNT EYE devices
  I0513 14:07:58.457536 31845 utils.cc:33] MYNT EYE devices:
  I0513 14:07:58.457563 31845 utils.cc:37]   index: 0, name: MYNT-EYE-S1000
  I0513 14:07:58.457567 31845 utils.cc:43] Only one MYNT EYE device, select index: 0
  I0513 14:07:58.474916 31845 auto_exposure.cc:37] Enable auto-exposure
  I0513 14:07:58.491058 31845 auto_exposure.cc:38] Set MAX_GAIN to 48
  I0513 14:07:58.505131 31845 auto_exposure.cc:39] Set MAX_EXPOSURE_TIME to 240
  I0513 14:07:58.521375 31845 auto_exposure.cc:41] Set DESIRED_BRIGHTNESS to 192


s2100/s210a：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_auto_exposure 
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C41A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/utils.cc:79 MYNT EYE devices:
  I/utils.cc:82   index: 0, request: width: 1280, height: 400, format: Format::BGR888, fps: 10
  I/utils.cc:82   index: 1, request: width: 1280, height: 400, format: Format::BGR888, fps: 20
  I/utils.cc:82   index: 2, request: width: 1280, height: 400, format: Format::BGR888, fps: 30
  I/utils.cc:82   index: 3, request: width: 1280, height: 400, format: Format::BGR888, fps: 60
  I/utils.cc:82   index: 4, request: width: 2560, height: 800, format: Format::BGR888, fps: 10
  I/utils.cc:82   index: 5, request: width: 2560, height: 800, format: Format::BGR888, fps: 20
  I/utils.cc:82   index: 6, request: width: 2560, height: 800, format: Format::BGR888, fps: 30
  I/utils.cc:93 There are 7 stream requests, select index: 
  3
  I/auto_exposure.cc:72 Enable auto-exposure
  I/auto_exposure.cc:73 Set EXPOSURE_MODE to 0
  I/auto_exposure.cc:75 Set MAX_GAIN to 8
  I/auto_exposure.cc:76 Set MAX_EXPOSURE_TIME to 333
  I/auto_exposure.cc:78 Set DESIRED_BRIGHTNESS to 122
  I/auto_exposure.cc:80 Set MIN_EXPOSURE_TIME to 0


样例程序会显示图像，左上角有真实曝光时间，单位毫秒。

完整代码样例，请见 `auto_exposure.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/auto_exposure.cc>`_ 。
