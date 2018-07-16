.. _get_with_plugin:

使用插件获取数据
==================

API 提供了 ``EnablePlugin()`` 函数，以启用某路径下的插件。

官方目前提供了些计算双目视差的插件，在 `MYNTEYE_BOX <http://www.myntai.com/mynteye/s/download>`_ 的 ``Plugins`` 目录内。

.. code-block:: none

  Plugins/
  ├─linux-x86_64/
  │  ├─libplugin_b_ocl1.2_opencv3.4.0.so
  │  ├─libplugin_g_cuda9.1_opencv2.4.13.5.so
  │  ├─libplugin_g_cuda9.1_opencv3.3.1.so
  │  └─libplugin_g_cuda9.1_opencv3.4.0.so
  ├─tegra-armv8/
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

.. tip::

  如果没有启用插件的话， ``api->Start(Source::VIDEO_STREAMING);`` 时会自动在 ``<sdk>/plugins/<platform>`` 目录里找合适的插件去加载。

  换句话说，可以把当前平台的插件目录整个搬进 ``<sdk>/plugins`` 目录内。安装好对应的 ``CUDA`` ``OpenCV`` 等插件依赖后重编译，此后运行 ``API`` 层接口程序，就会自动加载官方插件了。

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

.. tip::

  Linux 上也可以把依赖库路径加入系统环境，编译出的程序就可以直接运行了（不需要于终端里 ``export LD_LIBRARY_PATH`` 再运行）。

  * 新建 ``/etc/ld.so.conf.d/libmynteye.conf`` 文件，写入依赖库路径。
  * 终端里执行 ``sudo /sbin/ldconfig`` 命令，刷新缓存。

  .. literalinclude:: ../../files/libmynteye.conf
    :caption: e.g. libmynteye.conf
