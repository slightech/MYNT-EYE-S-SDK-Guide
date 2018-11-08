.. _get_stereo:

获取双目原始图像
==================

API 提供了 ``Start()`` ``Stop()`` 函数，用于开始或停止捕获数据。如果只捕获图像数据的话，参数用 ``Source::VIDEO_STREAMING`` 即可。

开始捕获数据后，首先调用 ``WaitForStreams()`` 函数，等待捕获到数据。接着，通过 ``GetStreamData()`` 函数，就能获取想要的数据了。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  api->Start(Source::VIDEO_STREAMING);

  cv::namedWindow("frame");

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);
    cv::imshow("frame", img);

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::VIDEO_STREAMING);

上述代码，用了 OpenCV 来显示图像。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_stereo.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_stereo.cc>`_ 。
