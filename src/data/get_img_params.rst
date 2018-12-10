.. _get_img_params:

获取图像标定参数
==================

通过 API 的 ``GetIntrinsics()`` ``GetExtrinsics()`` 函数，就可以获取当前打开设备的图像标定参数。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  LOG(INFO) << "Intrinsics left: {" << api->GetIntrinsics(Stream::LEFT) << "}";
  LOG(INFO) << "Intrinsics right: {" << api->GetIntrinsics(Stream::RIGHT)
            << "}";
  LOG(INFO) << "Extrinsics left to right: {"
            << api->GetExtrinsics(Stream::LEFT, Stream::RIGHT) << "}";

参考运行结果，于 Linux 上：

.. code-block:: bash

  $ ./samples/_output/bin/tutorials/get_img_params
  I/utils.cc:30 Detecting MYNT EYE devices
  I/utils.cc:40 MYNT EYE devices:
  I/utils.cc:43   index: 0, name: MYNT-EYE-S210A, sn: 07C60A190009071F
  I/utils.cc:51 Only one MYNT EYE device, select index: 0
  I/get_img_params.cc:24 Intrinsics left: {width: 640, height: 400, fx: 197.39641213416058463, fy: 197.72337597617189431, cx: 326.11983633916327108, cy: 199.86969132833945650, model: 0, coeffs: [0.12135236310725651, -0.08544277604917704, 0.00249148986319835, -0.00377520636582569, 0.00000000000000000]}
  I/get_img_params.cc:25 Intrinsics right: {width: 640, height: 400, fx: 203.35498653655989187, fy: 204.53858622699007697, cx: 315.89962248180813731, cy: 218.71688038954812328, model: 0, coeffs: [0.02290433055924156, -0.02956199007997184, 0.00397259427609815, -0.00396890732149456, 0.00000000000000000]}
  I/get_img_params.cc:27 Extrinsics right to left: {rotation: [0.99998850083695123, 0.00181660606427100, 0.00443825824777764, -0.00192636787222994, 0.99968925981619028, 0.02485302627404664, -0.00439173094434902, -0.02486129020314243, 0.99968126367795229], translation: [82.27020089055552887, 1.95351443600690589, -2.25880343444823684]}

完整代码样例，请见 `get_img_params.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_img_params.cc>`_ 。
