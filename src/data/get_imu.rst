.. _get_imu_data:

获取 IMU 数据 ✓
===============

API 提供了 ``Start()`` ``Stop()`` 函数，用于开始或停止捕获数据。要捕获 IMU 数据的话，参数用 ``Source::MOTION_TRACKING`` 。或者 ``Source::ALL`` 同时捕获图像和 IMU 数据。

开始捕获数据后，需要 ``EnableMotionDatas()`` 启用缓存，才能通过 ``GetMotionDatas()`` 函数获取到 IMU 数据。否则，只能通过回调接口得到 IMU 数据，请参阅 :ref:`get_from_callbacks` 。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // Enable this will cache the motion datas until you get them.
  api->EnableMotionDatas();

  api->Start(Source::ALL);

  CVPainter painter;

  cv::namedWindow("frame");

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);

    auto &&motion_datas = api->GetMotionDatas();
    /*
    for (auto &&data : motion_datas) {
      LOG(INFO) << "Imu frame_id: " << data.imu->frame_id
                << ", timestamp: " << data.imu->timestamp
                << ", accel_x: " << data.imu->accel[0]
                << ", accel_y: " << data.imu->accel[1]
                << ", accel_z: " << data.imu->accel[2]
                << ", gyro_x: " << data.imu->gyro[0]
                << ", gyro_y: " << data.imu->gyro[1]
                << ", gyro_z: " << data.imu->gyro[2]
                << ", temperature: " << data.imu->temperature;
    }
    */

    painter.DrawImgData(img, *left_data.img);
    if (!motion_datas.empty()) {
      painter.DrawImuData(img, *motion_datas[0].imu);
    }

    cv::imshow("frame", img);

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::ALL);

上述代码，用了 OpenCV 来显示图像和数据。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_imu.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/data/get_imu.cc>`_ 。
