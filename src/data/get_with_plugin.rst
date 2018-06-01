.. _get_with_plugin:

使用插件获取数据
==================

API 提供了 ``EnablePlugin()`` 函数，以启用某路径下的插件。

官方目前提供了些计算双目视差的插件，在 `Google Drive <https://drive.google.com/drive/folders/1tdFCcTBMNcImEGZ39tdOZmlX2SHKCr2f>`_ 或 `百度网盘 <https://pan.baidu.com/s/1yPQDp2r0x4jvNwn2UjlMUQ>`_ 的 ``Plugins`` 目录内。

.. code-block:: none

  Plugins/
  ├─linux-x86_64/
  │  ├─libplugin_b_ocl1.2_opencv3.4.0.so
  │  ├─libplugin_g_cuda9.1_opencv2.4.13.5.so
  │  ├─libplugin_g_cuda9.1_opencv3.3.1.so
  │  └─libplugin_g_cuda9.1_opencv3.4.0.so
  └─win-x86_64/

* 目录 ``linux-x86_64`` 表明了系统和架构。

  * 可从系统信息或 ``uname -a`` 得知你的 CPU 架构。

* 库名 ``libplugin_*`` 表明了插件标识和第三方依赖。

  * ``b`` ``g`` 是插件标识，说明用了不同算法。
  * ``ocl1.2`` 表明依赖了 ``OpenCL 1.2`` ，如果存在。
  * ``cuda9.1`` 表明依赖了 ``CUDA 9.1`` ，如果存在。
  * ``opencv3.4.0`` 表明依赖了 ``OpenCV 3.4.0`` ，如果存在。
  * ``mynteye2.0.0`` 表明依赖了 ``MYNT EYE SDK 2.0.0`` ，如果存在。

首先，根据具体情况，选择你想测试使用的插件。如果依赖了第三方，那么请安装一致的版本。

然后，参考如下代码启用插件：

.. code-block:: c++

  auto &&api = API::Create(argc, argv);

  api->EnablePlugin("plugins/linux-x86_64/libplugin_g_cuda9.1_opencv3.4.0.so");

路径可以是绝对路径，也可以是相对路径（相对于当前工作目录）。

最终，和之前一样调用 API 获取数据就行了。

运行前，请执行如下命令，以确保能搜索到插件的依赖库：

.. code-block:: bash

  # Linux
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  # /usr/local/lib 指依赖库所在路径

  # macOS
  export DYLD_LIBRARY_PATH=/usr/local/lib:$DYLD_LIBRARY_PATH
  # /usr/local/lib 指依赖库所在路径

  # Windows
  set PATH=C:\opencv\x64\vc14\bin;%PATH%
  # 或者，添加进系统环境变量 Path 里。

此外，可执行如下命令，检查是否能搜索到插件的依赖库：

.. code-block:: bash

  # Linux
  ldd *.so
  # *.so 指具体插件路径

  # macOS
  otool -L *.dylib
  # *.dylib 指具体插件路径

  # Windows
  # 请下载如 Dependency Walker ，打开 DLL 。

如果找不到插件的依赖库，加载时将会报错 "Open plugin failed" 。

完整代码样例，请见 `get_with_plugin.cc <https://github.com/slightech/MYNT-EYE-SDK-2/blob/master/samples/tutorials/data/get_with_plugin.cc>`_ 。
