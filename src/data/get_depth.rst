.. _get_depth:

获取深度图像
==============

深度图像，属于上层合成数据。需要事先 ``EnableStreamData()`` 启用，然后 ``GetStreamData()`` 获取。另外，判断不为空后再使用。

详细流程说明，请参阅 :ref:`get_stereo` :ref:`get_stereo_rectified` 。

另外，推荐使用插件计算深度：深度图效果会更好，并且运算速度更快。具体请参阅 :ref:`get_with_plugin` 。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  api->EnableStreamData(Stream::DEPTH);

  api->Start(Source::VIDEO_STREAMING);

  cv::namedWindow("frame");
  cv::namedWindow("depth");

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);
    cv::imshow("frame", img);

    auto &&depth_data = api->GetStreamData(Stream::DEPTH);
    if (!depth_data.frame.empty()) {
      cv::imshow("depth", depth_data.frame);  // CV_16UC1
    }

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::VIDEO_STREAMING);

上述代码，用了 OpenCV 来显示图像。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_depth.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_depth.cc>`_ 。

.. tip::

  预览深度图某区域的值，请见 `get_depth_with_region.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/api/get_depth_with_region.cc>`_ 。
