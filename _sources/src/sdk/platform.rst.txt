.. _sdk_platform:

支持平台
==========

SDK 是基于 CMake 构建的，用以跨 Linux, Windows, macOS 等多个平台。而从源码编译安装，也可以适配您的平台架构，并应用本地优化。

已测试可用的平台有：

* Windows 10
* Ubuntu 16.04 / 14.04
* Jetson TX2

.. warning::

  由于硬件传输速率要求，务必使用 USB 3.0 接口。另外，虚拟机因其大多存在 USB 驱动兼容性问题，不建议使用。
