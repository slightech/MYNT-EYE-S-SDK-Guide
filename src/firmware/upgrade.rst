.. _firmware_upgrade:

固件如何进行升级 ✓
==================

固件升级，需要使用我们提供的固件升级程序。

固件及其升级程序，都在 `Google Drive <https://drive.google.com/drive/folders/1tdFCcTBMNcImEGZ39tdOZmlX2SHKCr2f>`_ 或 `百度网盘 <https://pan.baidu.com/s/1yPQDp2r0x4jvNwn2UjlMUQ>`_ 的 ``Firmwares`` 目录内。文件结构如下：

.. code-block:: none

  Firmwares/
  ├─Checksum.txt                 # 文件校验码
  ├─MYNTEYE_S_2.0.0_rc0.img      # 固件文件
  ├─...
  └─upgrader-setup.exe           # 固件升级程序

固件升级程序，目前仅支持 Windows ，所以需要你在 Windows 下进行操作。步骤如下：

下载准备
--------

* 下载固件升级程序 ``upgrader-setup.exe`` 。
* 下载固件，如 ``MYNTEYE_S_2.0.0_rc0.img`` 。

  * 请见 :ref:`firmware_applicable` 选择适合当前 SDK 版本的固件。
  * 请见 ``Checksum.txt`` 找到下载固件的校验码，如下获取并比对：

    * 命令提示符（CMD）里运行 ``certutil -hashfile <*.img> MD5`` 。
    * 校验码不正确的话，说明下载有误，请重新下载！

安装程序
--------

* 双击 ``upgrader-setup.exe`` 安装固件升级程序。完成后，桌面会有程序快捷。

升级固件
--------

* USB 口插上 MYNT® EYE 设备。

* 打开固件升级程序，选择 ``Options/FirmwareUpdate`` 。

.. image:: ../../images/firmware_update_option.png

* 打开窗口里，``Device`` 选中 ``MYNTEYE`` ，然后点击 ``Update`` 。

.. image:: ../../images/firmware_update.png
   :width: 60%

* 弹出警告对话框，直接 ``是`` 即可。

  * 其提示为初次使用时确保安装了驱动程序，详情见 README 。

    * 驱动程序在安装升级程序时，正常情况都会安装好的。
    * 如果升级遇到问题，一般都是驱动未安装好，可见 README 解决。

.. image:: ../../images/firmware_update_warning.png
   :width: 60%

.. image:: ../../images/firmware_update_dir.png
   :width: 60%

* 在打开的文件选择框里，选择要升级的固件，开始升级。

.. image:: ../../images/firmware_update_select.png

* 升级完成时，会有提示音“嘀”，同时状态变为 ``Succeeded`` 。

.. image:: ../../images/firmware_update_success.png
   :width: 60%

* 关闭升级程序，结束。

.. warning::

  固件升级后，初次打开 MYNT® EYE 设备时，请先放置于桌面静止 3 秒，其会有一个零漂补偿过程。或者，请主动调用控制接口 ``RunOptionAction(Option::ZERO_DRIFT_CALIBRATION)`` 来进行零漂补偿。

.. ::

  .. image:: ../../images/firmware_update_driver.png
  .. image:: ../../images/firmware_update_driver_install.png
