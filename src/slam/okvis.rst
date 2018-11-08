.. _slam_okvis:

`OKVIS <https://github.com/ethz-asl/okvis>`_ 如何整合
=============================================================

在 MYNT® EYE 上运行 OKVIS ，请依照这些步骤：
----------------------------------------------

1. 下载 `MYNT-EYE-S-SDK <https://github.com/slightech/MYNT-EYE-S-SDK.git>`_ 并安装。
2. 安装依赖，按照原始 OKVIS 步骤安装 MYNT-EYE-OKVIS-Sample 。
3. 更新相机参数到 ``<OKVIS>/config/config_mynteye.yaml``。
4. 在 MYNT® EYE 上运行 OKVIS 。

安装 MYNT® EYE OKVIS
---------------------

首先安装原始 OKVIS 及依赖：

.. code-block:: bash

  git clone -b mynteye-s https://github.com/slightech/MYNT-EYE-OKVIS-Sample.git
  mkdir build && cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make -j4

获取相机校准参数
-----------------

通过 `MYNT-EYE-S-SDK <https://github.com/slightech/MYNT-EYE-S-SDK.git>`_ API 的 ``GetIntrinsics()`` 函数和 ``GetExtrinsics()`` 函数，可以获得当前工作设备的图像校准参数：

.. code-block:: bat

  cd MYNT-EYE-S-SDK
  ./samples/_output/bin/tutorials/get_img_params

这时，可以获得针孔模型下的 ``distortion_parameters`` 和 ``projection_parameters`` 参数，然后在 `这里 <https://github.com/slightech/MYNT-EYE-OKVIS-Sample/blob/mynteye-s/config/config_mynteye.yaml>`_ 更新。

运行 MYNT® EYE OKVIS
---------------------

在 ``MYNT-EYE-OKVIS-Sample/build`` 中运行 ``okvis_app_mynteye_s`` :

.. code-block:: bash

  cd MYNT-EYE-OKVIS-Sample/build
  ./okvis_app_mynteye_s ../config/config_mynteye.yaml
