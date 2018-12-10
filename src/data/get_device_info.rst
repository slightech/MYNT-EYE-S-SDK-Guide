.. _get_device_info:

获取设备信息
==============

通过 API 的 ``GetInfo()`` 函数，就可以获取当前打开设备的各类信息值。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  LOG(INFO) << "Device name: " << api->GetInfo(Info::DEVICE_NAME);
  LOG(INFO) << "Serial number: " << api->GetInfo(Info::SERIAL_NUMBER);
  LOG(INFO) << "Firmware version: " << api->GetInfo(Info::FIRMWARE_VERSION);
  LOG(INFO) << "Hardware version: " << api->GetInfo(Info::HARDWARE_VERSION);
  LOG(INFO) << "Spec version: " << api->GetInfo(Info::SPEC_VERSION);
  LOG(INFO) << "Lens type: " << api->GetInfo(Info::LENS_TYPE);
  LOG(INFO) << "IMU type: " << api->GetInfo(Info::IMU_TYPE);
  LOG(INFO) << "Nominal baseline: " << api->GetInfo(Info::NOMINAL_BASELINE);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/get_device_info
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/get_device_info.cc:24 Device name: MYNT-EYE-S210A
  I/get_device_info.cc:25 Serial number: 07C60A190009071F
  I/get_device_info.cc:26 Firmware version: 1.0
  I/get_device_info.cc:27 Hardware version: 1.0
  I/get_device_info.cc:28 Spec version: 1.1
  I/get_device_info.cc:29 Lens type: 0001
  I/get_device_info.cc:30 IMU type: 0001
  I/get_device_info.cc:31 Nominal baseline: 80

完整代码样例，请见 `get_device_info.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_device_info.cc>`_ 。
