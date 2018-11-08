.. _log_file:

启用日志文件
==============

日志的通用配置，在头文件 `glog_init.h <https://github.com/slightech/MYNT-EYE-S-SDK/blob/master/include/mynteye/glog_init.h>`_ 里 。

取消注释的 ``FLAGS_log_dir = ".";`` 重新编译，即可保存日志到当前工作目录。例如运行 ``camera_a`` 后，日志文件如下：

.. code-block:: none

  <workdir>/
  ├─camera_a.ERROR
  ├─camera_a.FATAL
  ├─camera_a.INFO
  ├─camera_a.WARNING
  ├─camera_a.john-ubuntu.john.log.ERROR.20180513-141833.519
  ├─camera_a.john-ubuntu.john.log.FATAL.20180513-141833.519
  ├─camera_a.john-ubuntu.john.log.INFO.20180513-141832.519
  └─camera_a.john-ubuntu.john.log.WARNING.20180513-141833.519

``camera_a.INFO`` 表明了哪个程序、什么日志级别。但它只是一个链接，指向真实的日志文件，如 ``camera_a.john-ubuntu.john.log.INFO.20180513-141832.519`` 。运行多次后， ``camera_a.INFO`` 仍只会有一个，指向最新的那个日志文件，便于你查看。

执行 ``make cleanlog`` 可以清理所有日志文件。
