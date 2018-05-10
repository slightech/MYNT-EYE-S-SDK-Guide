.. _get_stereo_rectified:

获取双目纠正图像 ✓
==================

API 提供的 ``GetStreamData()`` 默认仅能获取到硬件的原始数据，例如双目原始图像。

而双目纠正图像，属于上层合成数据。此类数据，需要事先 ``EnableStreamData()`` 启用，然后 ``GetStreamData()`` 才能获取到。

另外，``WaitForStreams()`` 等待的是关键原始数据。刚开始时，合成数据可能还在处理，取出的是空值，所以需要判断下不为空。

.. tip::

  如果想要合成数据一生成就立即获取到，请参阅 :ref:`get_from_callbacks` 。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  api->EnableStreamData(Stream::LEFT_RECTIFIED);
  api->EnableStreamData(Stream::RIGHT_RECTIFIED);

  api->Start(Source::VIDEO_STREAMING);

  cv::namedWindow("frame");

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT_RECTIFIED);
    auto &&right_data = api->GetStreamData(Stream::RIGHT_RECTIFIED);

    if (!left_data.frame.empty() && !right_data.frame.empty()) {
      cv::Mat img;
      cv::hconcat(left_data.frame, right_data.frame, img);
      cv::imshow("frame", img);
    }

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::VIDEO_STREAMING);

上述代码，用了 OpenCV 来显示图像。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_stereo_rectified.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/data/get_stereo_rectified.cc>`_ 。
