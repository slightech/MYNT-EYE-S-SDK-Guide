.. _framerate:

设定图像帧率和 IMU 频率
=========================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

设定图像帧率和 IMU 频率，就是设定 ``Option::FRAME_RATE`` 和 ``Option::IMU_FREQUENCY`` 。

.. Attention::

  * 图像帧率和 IMU 频率必须同时设定才能生效。
  * 图像帧率有效值： 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 。
  * IMU 频率有效值： 100, 200, 250, 333, 500 。

参考代码片段：

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

参考运行结果，于 Linux 上：

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

样例程序按 ``ESC/Q`` 结束运行后，会输出计算得的图像帧率和 IMU 频率。

完整代码样例，请见 `framerate.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/control/framerate.cc>`_ 。
