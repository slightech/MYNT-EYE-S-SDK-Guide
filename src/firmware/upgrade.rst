.. _firmware_upgrade:

固件如何进行升级
==================

固件升级，需要使用我们提供的固件升级程序：MYNT EYE TOOL。

固件及MYNT EYE TOOL的安装包，都在 `MYNTEYE_BOX <http://doc.myntai.com/mynteye/s/download>`_ 的 ``Firmwares`` 目录内。文件结构如下：

.. code-block:: none

  Firmwares/
  ├─Checksum.txt                 # file checksum
  ├─MYNTEYE_S_2.2.0.img      # firmware
  ├─...
  └─setup.zip                    # MYNTEYE TOOL zip

固件升级程序，目前仅支持 Windows ，所以需要你在 Windows 下进行操作。步骤如下：

下载准备
--------

* 下载并解压 ``setup.zip``。
* 下载固件，如 ``MYNTEYE_S_2.2.0.img`` 。

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


.. attention::
  如果在设备管理器中同时找不到MYNT图像设备、 ``WestBridge_driver`` 以及 ``Cypress USB BootLoader`` 则尝试换一台电脑执行以上操作。如果还是不能升级成功，请及时联系我们。


手动更新驱动
------------

* 如果应用提示您升级失败，则可能是自动安装驱动失败，您可以尝试手动安装驱动然后重新升级。以下为手动安装驱动的步骤。

* 打开设备管理器，找到 ``WestBridge_driver`` 设备，然后右键更新驱动，选择 ``[应用安装目录]\WestBridge_driver\[对应系统文件夹](win7以上选择wlh)\[系统对应位数]`` 。

.. image:: ../../images/firmware_update_westbridge.png

* 以win 10 64位默认安装路径为例，需要选择的文件夹为 ``C:\Program Files (x86)\slightech\MYNT EYE Camera Tool\wlh\x64`` 。

* 安装驱动成功之后，可以在设备管理器中找到 ``Cypress USB BootLoader`` 设备。

.. image:: ../../images/firmware_update_cypressUSB.png

* 然后拔插摄像头，再次打开该应用进行升级。

.. warning::

  固件升级后，初次打开 MYNT® EYE 设备时，请静置 3 秒，其会有一个零漂补偿过程。或者，请主动调用控制接口 ``RunOptionAction(Option::ZERO_DRIFT_CALIBRATION)`` 来进行零漂补偿。

.. ::

  .. image:: ../../images/firmware_update_driver.png
  .. image:: ../../images/firmware_update_driver_install.png
