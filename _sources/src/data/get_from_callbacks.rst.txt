.. _get_from_callbacks:

从回调接口获取数据
====================

API 提供了 ``SetStreamCallback()`` ``SetMotionCallback()`` 函数，来设定各类数据的回调。

.. attention::

  一定不要阻塞回调。如果需要长时间处理数据，请将回调作为数据生产者。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // Attention: must not block the callbacks.

  // Get left image from callback
  std::atomic_uint left_count(0);
  api->SetStreamCallback(
      Stream::LEFT, [&left_count](const api::StreamData &data) {
        CHECK_NOTNULL(data.img);
        ++left_count;
      });

  // Get depth image from callback
  api->EnableStreamData(Stream::DEPTH);
  std::atomic_uint depth_count(0);
  cv::Mat depth;
  std::mutex depth_mtx;
  api->SetStreamCallback(
      Stream::DEPTH,
      [&depth_count, &depth, &depth_mtx](const api::StreamData &data) {
        UNUSED(data)
        ++depth_count;
        {
          std::lock_guard<std::mutex> _(depth_mtx);
          depth = data.frame;
        }
      });

  // Get motion data from callback
  std::atomic_uint imu_count(0);
  std::shared_ptr<mynteye::ImuData> imu;
  std::mutex imu_mtx;
  api->SetMotionCallback(
      [&imu_count, &imu, &imu_mtx](const api::MotionData &data) {
        CHECK_NOTNULL(data.imu);
        ++imu_count;
        {
          std::lock_guard<std::mutex> _(imu_mtx);
          imu = data.imu;
        }
      });

  api->Start(Source::ALL);

  CVPainter painter;

  cv::namedWindow("frame");
  cv::namedWindow("depth");

  unsigned int depth_num = 0;
  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    // Concat left and right as img
    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);

    // Draw img data and size
    painter.DrawImgData(img, *left_data.img);

    // Draw imu data
    if (imu) {
      std::lock_guard<std::mutex> _(imu_mtx);
      painter.DrawImuData(img, *imu);
    }

    // Draw counts
    std::ostringstream ss;
    ss << "left: " << left_count << ", depth: " << depth_count
       << ", imu: " << imu_count;
    painter.DrawText(img, ss.str(), CVPainter::BOTTOM_RIGHT);

    // Show img
    cv::imshow("frame", img);

    // Show depth
    if (!depth.empty()) {
      // Is the depth a new one?
      if (depth_num != depth_count || depth_num == 0) {
        std::lock_guard<std::mutex> _(depth_mtx);
        depth_num = depth_count;
        // LOG(INFO) << "depth_num: " << depth_num;
        ss.str("");
        ss.clear();
        ss << "depth: " << depth_count;
        painter.DrawText(depth, ss.str());
        cv::imshow("depth", depth);  // CV_16UC1
      }
    }

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::ALL);

上述代码，用了 OpenCV 来显示图像和数据。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_from_callbacks.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_from_callbacks.cc>`_ 。
