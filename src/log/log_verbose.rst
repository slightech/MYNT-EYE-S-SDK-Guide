.. _log_verbose:

启用详细级别
==============

日志的通用配置，在头文件 `glog_init.h <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/include/mynteye/glog_init.h>`_ 里 。

取消注释的 ``FLAGS_v = 2;`` 重新编译，即可启用详细级别，指 ``VLOG(n)`` 打印的日志。

关于如何使用日志库，即如何配置、打印等，请如下打开其文档进行了解：

.. code-block:: bash

  $ ./scripts/open.sh third_party/glog/doc/glog.html
