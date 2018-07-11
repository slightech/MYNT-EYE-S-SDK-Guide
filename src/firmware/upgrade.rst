.. _firmware_upgrade:

固件如何进行升级
==================

固件升级，需要使用我们提供的固件升级程序：MYNT EYE TOOL。

固件及MYNT EYE TOOL的安装包，都在 `MYNTEYE_BOX <http://files.slightech.com/dfiles/downfiles>`_ 的 ``Firmwares`` 目录内。文件结构如下：

.. code-block:: none

  Firmwares/
  ├─Checksum.txt                 # file checksum
  ├─MYNTEYE_S_2.0.0_rc0.img      # firmware
  ├─...
  └─setup.zip                    # MYNTEYE TOOL zip

固件升级程序，目前仅支持 Windows ，所以需要你在 Windows 下进行操作。步骤如下：

下载准备
--------

* 下载并解压 ``setup.zip``。
* 下载固件，如 ``MYNTEYE_S_2.0.0_rc0.img`` 。

  * 请见 :ref:`firmware_applicable` 选择适合当前 SDK 版本的固件。
  * 请见 ``Checksum.txt`` 找到下载固件的校验码，如下获取并比对：

    * 命令提示符（CMD）里运行 ``certutil -hashfile <*.img> MD5`` 。
    * 校验码不正确的话，说明下载有误，请重新下载！

安装MYNT EYE TOOL
-----------------

* 双击 ``setup.msi`` 安装固件升级程序。

升级固件
--------

* USB3.0 口插上 MYNT® EYE 设备。

* 打开MYNT EYE TOOL，选择 ``Options/FirmwareUpdate`` 。

.. image:: ../../images/firmware_update_option.png

* 点击 ``Update`` 。

.. image:: ../../images/firmware_update.png
   :width: 60%

* 弹出警告对话框，直接 ``确定`` 即可。

  * 由于该操作会擦除固件，所以弹出警告。详情见 README 。

    * 通常在升级过程中，MYNT EYE TOOL会自动安装驱动。
    * 如果升级遇到问题，参考 README 解决。

.. image:: ../../images/firmware_update_warning.png
   :width: 60%

.. image:: ../../images/firmware_update_dir.png
   :width: 60%

* 在打开的文件选择框里，选择要升级的固件，开始升级。

.. image:: ../../images/firmware_update_select.png

* 升级完成后，状态变为 ``Succeeded`` 。

.. image:: ../../images/firmware_update_success.png
   :width: 60%

* 关闭MYNT EYE TOOL，结束。

.. warning::

  固件升级后，初次打开 MYNT® EYE 设备时，请静置 3 秒，其会有一个零漂补偿过程。或者，请主动调用控制接口 ``RunOptionAction(Option::ZERO_DRIFT_CALIBRATION)`` 来进行零漂补偿。

.. ::

  .. image:: ../../images/firmware_update_driver.png
  .. image:: ../../images/firmware_update_driver_install.png
