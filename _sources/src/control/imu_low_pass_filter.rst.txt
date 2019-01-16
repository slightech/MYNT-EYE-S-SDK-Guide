.. _imu_low_pass_filter:

低通滤波
=========

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

设定加速度计低通滤波寄存器值及陀螺仪低通滤波寄存器值，就是设定 ``Option::ACCELEROMETER_LOW_PASS_FILTER`` 和 ``Option::GYROSCOPE_LOW_PASS_FILTER`` 。

.. Attention::
  * s1030不支持此功能

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);
  if (!api) return 1;

  bool ok;
  auto &&request = api->SelectStreamRequest(&ok);
  if (!ok) return 1;
  api->ConfigStreamRequest(request);

  // ACCELEROMETER_RANGE values: 0, 1, 2
  api->SetOptionValue(Option::ACCELEROMETER_LOW_PASS_FILTER, 2);
  // GYROSCOPE_RANGE values: 23, 64
  api->SetOptionValue(Option::GYROSCOPE_LOW_PASS_FILTER, 64);

  LOG(INFO) << "Set ACCELEROMETER_LOW_PASS_FILTER to "
            << api->GetOptionValue(Option::ACCELEROMETER_LOW_PASS_FILTER);
  LOG(INFO) << "Set GYROSCOPE_LOW_PASS_FILTER to "
            << api->GetOptionValue(Option::GYROSCOPE_LOW_PASS_FILTER);


参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_imu_low_pass_filter 
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
  1
  I/imu_low_pass_filter.cc:48 Set ACCELEROMETER_LOW_PASS_FILTER to 2
  I/imu_low_pass_filter.cc:50 Set GYROSCOPE_LOW_PASS_FILTER to 64
  I/imu_low_pass_filter.cc:96 Time beg: 2018-12-29 13:53:42.296299, end: 2018-12-29 14:06:33.295960, cost: 771000ms
  I/imu_low_pass_filter.cc:99 Img count: 15412, fps: 19.9896
  I/imu_low_pass_filter.cc:101 Imu count: 309891, hz: 401.934

样例程序按 ``ESC/Q`` 结束运行后，imu低通滤波设置完成。该结果将固化在硬件内部，不受掉电影响。

完整代码样例，请见 `imu_low_pass_filter.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/imu_low_pass_filter.cc>`_ 。
