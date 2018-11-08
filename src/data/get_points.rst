.. _get_points:

获取点云图像
==============

点云图像，属于上层合成数据。需要事先 ``EnableStreamData()`` 启用，然后 ``GetStreamData()`` 获取。另外，判断不为空后再使用。

详细流程说明，请参阅 :ref:`get_stereo` :ref:`get_stereo_rectified` 。

另外，推荐使用插件计算深度：深度图效果会更好，并且运算速度更快。具体请参阅 :ref:`get_with_plugin` 。

参考代码片段：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  api->EnableStreamData(Stream::POINTS);

  api->Start(Source::VIDEO_STREAMING);

  cv::namedWindow("frame");
  PCViewer pcviewer;

  while (true) {
    api->WaitForStreams();

    auto &&left_data = api->GetStreamData(Stream::LEFT);
    auto &&right_data = api->GetStreamData(Stream::RIGHT);

    cv::Mat img;
    cv::hconcat(left_data.frame, right_data.frame, img);
    cv::imshow("frame", img);

    auto &&points_data = api->GetStreamData(Stream::POINTS);
    if (!points_data.frame.empty()) {
      pcviewer.Update(points_data.frame);
    }

    char key = static_cast<char>(cv::waitKey(1));
    if (key == 27 || key == 'q' || key == 'Q') {  // ESC/Q
      break;
    }
    if (pcviewer.WasStopped()) {
      break;
    }
  }

  api->Stop(Source::VIDEO_STREAMING);

上述代码，用了 `PCL <https://github.com/PointCloudLibrary/pcl>`_ 来显示点云。关闭点云窗口时，也会结束程序。

完整代码样例，请见 `get_points.cc <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/data/get_points.cc>`_ 。

.. attention::

  准备好了 `PCL <https://github.com/PointCloudLibrary/pcl>`_ 库，编译教程样例时才会有此例子。如果 `PCL <https://github.com/PointCloudLibrary/pcl>`_ 库安装到了自定义目录，那么请打开 `tutorials/CMakeLists.txt <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/samples/tutorials/CMakeLists.txt>`_ ，找到 ``find_package(PCL)`` ，把 ``PCLConfig.cmake`` 所在目录添加进 ``CMAKE_PREFIX_PATH`` 。
