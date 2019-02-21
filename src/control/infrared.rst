.. _infrared:

启用 IR 及其调节
==================

通过 API 的 ``SetOptionValue()`` 函数，就可以设定当前打开设备的各类控制值。

启用 IR ，就是设定 ``Option::IR_CONTROL`` 大于 0 的值。值越大，强度越高。

.. Attention::
  * s2100/s210a不支持此功能

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // Detect infrared add-ons
  LOG(INFO) << "Support infrared: " << std::boolalpha
            << api->Supports(AddOns::INFRARED);
  LOG(INFO) << "Support infrared2: " << std::boolalpha
            << api->Supports(AddOns::INFRARED2);

  // Get infrared intensity range
  auto &&info = api->GetOptionInfo(Option::IR_CONTROL);
  LOG(INFO) << Option::IR_CONTROL << ": {" << info << "}";

  // Set infrared intensity value
  api->SetOptionValue(Option::IR_CONTROL, 80);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_infrared
  I0504 16:16:28.016624 25848 utils.cc:13] Detecting MYNT EYE devices
  I0504 16:16:28.512462 25848 utils.cc:20] MYNT EYE devices:
  I0504 16:16:28.512473 25848 utils.cc:24]   index: 0, name: MYNT-EYE-S1000
  I0504 16:16:28.512477 25848 utils.cc:30] Only one MYNT EYE device, select index: 0
  I0504 16:16:28.520848 25848 infrared.cc:13] Support infrared: true
  I0504 16:16:28.520869 25848 infrared.cc:15] Support infrared2: true
  I0504 16:16:28.520889 25848 infrared.cc:20] Option::IR_CONTROL: {min: 0, max: 160, def: 0}

此时，如果显示了图像，就能够看到图像上会有 IR 光斑。

.. attention::

  硬件不会记忆 IR 值，断电会忘掉。如果需要保持启用 IR 的话，程序在打开设备后，一定要设定下 IR 值。

完整代码样例，请见 `infrared.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/infrared.cc>`_ 。
