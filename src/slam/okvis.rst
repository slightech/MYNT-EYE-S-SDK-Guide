.. _slam_okvis:

`OKVIS <https://github.com/ethz-asl/okvis>`_ 如何整合 
=============================================================


在MYNT® EYE 上运行 OKVIS ，请依照这些步骤：
----------------------------------------------

* 1. 下载 `MYNT-EYE-SDK-2 <https://github.com/slightech/MYNT-EYE-SDK-2.git>`_ 并安装。
* 2. 添加 MYNT-EYE-SDK 路径到环境变量。打开 ``.bashrc`` 文件，在最后添加：export MYNTEYE_SDK2_ROOT=MYNT-EYE-SDK-2_INSTALL_PATH 。
* 3. 安装依赖，按照原始 OKVIS 步骤安装 MYNT-EYE-OKVIS-Sample。
* 4. 更新相机参数到 ``<OKVIS>/config/config_mynteye.yaml``。
* 5. 在MYNT® EYE 上运行 OKVIS 。

安装 MYNT® EYE OKVIS
---------------------

首先安装原始 OKVIS 及依赖： 

.. code-block:: bat
 
  git clone -b sdk2 https://github.com/slightech/MYNT-EYE-OKVIS-Sample.git
  mkdir build && cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make -j4

获取相机校准参数
-----------------

通过 `MYNT-EYE-SDK-2 <https://github.com/slightech/MYNT-EYE-SDK-2.git>`_ API的 ``GetIntrinsics()`` 函数和 ``GetExtrinsics()`` 函数，可以获得当前工作设备的图像校准参数：

.. code-block:: bat

  cd MYNT-EYE-SDK-2
  ./samples/_output/bin/tutorials/get_img_params

这时，可以获得针孔模型下的 ``distortion_parameters`` 和 ``projection_parameters`` 参数，然后在 `这里 <https://github.com/slightech/MYNT-EYE-OKVIS-Sample/blob/sdk2/config/config_mynteye.yaml>`_ 更新。

运行 MYNT® EYE OKVIS
---------------------

在 ``MYNT-EYE-OKVIS-Sample/build `` 中运行 ``okvis_app_mynteye_sdk2`` :

.. code-block:: bat

  cd MYNT-EYE-OKVIS-Sample/build
  ./okvis_app_mynteye_sdk2 ../config/config_mynteye.yaml


