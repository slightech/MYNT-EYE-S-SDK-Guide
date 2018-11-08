.. _get_disparity:

获取视差图像
==============

视差图像，属于上层合成数据。需要事先 ``EnableStreamData()`` 启用，然后 ``GetStreamData()`` 获取。另外，判断不为空后再使用。

详细流程说明，请参阅 :ref:`get_stereo` :ref:`get_stereo_rectified` 。

另外，推荐使用插件计算深度：深度图效果会更好，并且运算速度更快。具体请参阅 :ref:`get_with_plugin` 。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  // api->EnableStreamData(Stream::DISPARITY);
  api->EnableStreamData(Stream::DISPARITY_NORMALIZED);

  api->Start(Source::VIDEO_STREAMING);

  cv::namedWindow("frame");
  // cv::namedWindow("disparity");
  cv::namedWindow("disparity_normalized");

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);
    cv::imshow("frame", img);

    // auto &&disp_data = api->GetStreamData(Stream::DISPARITY);
    // if (!disp_data.frame.empty()) {
    //   cv::imshow("disparity", disp_data.frame);
    // }

    auto &&disp_norm_data = api->GetStreamData(Stream::DISPARITY_NORMALIZED);
    if (!disp_norm_data.frame.empty()) {
      cv::imshow("disparity_normalized", disp_norm_data.frame);  // CV_8UC1
    }

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
  }

  api->Stop(Source::VIDEO_STREAMING);

上述代码，用了 OpenCV 来显示图像。选中显示窗口时，按 ``ESC/Q`` 就会结束程序。

完整代码样例，请见 `get_disparity.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_disparity.cc>`_ 。
