.. _get_imu_params:

获取 IMU 标定参数
====================

通过 API 的 ``GetMotionIntrinsics()`` ``GetMotionExtrinsics()`` 函数，就可以获取当前打开设备的 IMU 标定参数。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  LOG(INFO) << "Motion intrinsics: {" << api->GetMotionIntrinsics() << "}";
  LOG(INFO) << "Motion extrinsics left to imu: {"
            << api->GetMotionExtrinsics(Stream::LEFT) << "}";

完整代码样例，请见 `get_imu_params.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/data/get_imu_params.cc>`_ 。
