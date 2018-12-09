.. _framerate:

设定图像分辨率，格式与帧率
============================

设置图像分辨率需要在创建API时通过``Create()``设置，例如API::Create(Resolution::RES_1280x400)。
图像格式和帧率需要在视频请求之前通过``SetStreamRequest()``设置，例如SetStreamRequest(Format::BGR888, FrameRate::RATE_30_FPS)。


.. Attention::

  * 相机支持的格式：BGR888。
  * 相机支持的分辨率(左右目叠加)： RES_1280x400，RES_2560x800。
  * 相机支持的帧率： RATE_10_FPS, RATE_20_FPS, RATE_30_FPS, RATE_60_FPS（仅1280x400支持）。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(Resolution::RES_1280x400);
  // auto &&api = API::Create(argc, argv);
  if (!api)
    return 1;
  api->SetStreamRequest(Format::BGR888, FrameRate::RATE_30_FPS);

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/ctrl_framerate
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/framerate.cc:65 Time beg: 2018-12-08 14:03:30.233115, end: 2018-12-08 14:03:36.758260, cost: 6525.14ms
  I/framerate.cc:68 Img count: 197, fps: 30.1909


样例程序按 ``ESC/Q`` 结束运行后，会输出计算得的图像帧率。

完整代码样例，请见 `framerate.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/control/framerate.cc>`_ 。
