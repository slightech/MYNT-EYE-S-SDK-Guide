.. _framerate:

设定图像帧率和 IMU 频率
=========================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

以s1030为例，设定图像帧率和 IMU 频率，就是设定 ``Option::FRAME_RATE`` 和 ``Option::IMU_FREQUENCY`` 。

.. Attention::

  * 图像帧率和 IMU 频率必须同时设定才能生效。
  * 图像帧率有效值： 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 。
  * IMU 频率有效值： 100, 200, 250, 333, 500 。

以s2100/s210a为例,图像帧率需要在运行样例时选择，帧率和分辨率选择如下：

.. code-block:: bash

  index: 0, request: width: 1280, height: 400, format: Format::BGR888, fps: 10
  index: 1, request: width: 1280, height: 400, format: Format::BGR888, fps: 20
  index: 2, request: width: 1280, height: 400, format: Format::BGR888, fps: 30
  index: 3, request: width: 1280, height: 400, format: Format::BGR888, fps: 60
  index: 4, request: width: 2560, height: 800, format: Format::BGR888, fps: 10
  index: 5, request: width: 2560, height: 800, format: Format::BGR888, fps: 20
  index: 6, request: width: 2560, height: 800, format: Format::BGR888, fps: 30


参考代码片段：

s1030：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // Attention: must set FRAME_RATE and IMU_FREQUENCY together, otherwise won't
  // succeed.

  // FRAME_RATE values: 10, 15, 20, 25, 30, 35, 40, 45, 50, 55
  api->SetOptionValue(Option::FRAME_RATE, 25);
  // IMU_FREQUENCY values: 100, 200, 250, 333, 500
  api->SetOptionValue(Option::IMU_FREQUENCY, 500);

  LOG(INFO) << "Set FRAME_RATE to " << api->GetOptionValue(Option::FRAME_RATE);
  LOG(INFO) << "Set IMU_FREQUENCY to "
            << api->GetOptionValue(Option::IMU_FREQUENCY);

s2100/s210a：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);
  if (!api) return 1;
  
  bool ok;
  auto &&request = api->SelectStreamRequest(&ok);
  if (!ok) return 1;
  api->ConfigStreamRequest(request);

  LOG(INFO) << "Please set frame rate by 'SelectStreamRequest()'";



参考运行结果，于 Linux 上：

s1030：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_framerate
  I0513 14:05:57.218222 31813 utils.cc:26] Detecting MYNT EYE devices
  I0513 14:05:57.899404 31813 utils.cc:33] MYNT EYE devices:
  I0513 14:05:57.899430 31813 utils.cc:37]   index: 0, name: MYNT-EYE-S1000
  I0513 14:05:57.899435 31813 utils.cc:43] Only one MYNT EYE device, select index: 0
  I0513 14:05:58.076257 31813 framerate.cc:36] Set FRAME_RATE to 25
  I0513 14:05:58.076836 31813 framerate.cc:37] Set IMU_FREQUENCY to 500
  I0513 14:06:21.702361 31813 framerate.cc:82] Time beg: 2018-05-13 14:05:58.384967, end: 2018-05-13 14:06:21.666115, cost: 23281.1ms
  I0513 14:06:21.702388 31813 framerate.cc:85] Img count: 573, fps: 24.6122
  I0513 14:06:21.702404 31813 framerate.cc:87] Imu count: 11509, hz: 494.348

s2100/s210a：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_framerate 
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
  2
  I/framerate.cc:54 Please set frame rate by 'SelectStreamRequest()'
  I/framerate.cc:99 Time beg: 2018-12-29 10:05:08.203095, end: 2018-12-29 10:08:20.074969, cost: 191872ms
  I/framerate.cc:102 Img count: 5759, fps: 30.0148
  I/framerate.cc:104 Imu count: 77163, hz: 402.159


样例程序按 ``ESC/Q`` 结束运行后，会输出计算得的图像帧率和 IMU 频率。

完整代码样例，请见 `framerate.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/framerate.cc>`_ 。
