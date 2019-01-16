.. _how_to_use_kalibr:

如何用 kalibr 标定 MYNTEYE
================================

标定目标
------------

* 标定左右目之间的位姿关系

* 标定相机（左目）和IMU坐标系之间的位姿关系


准备工作
------------

* **安装kalibr**： 参考 `kalibr wiki <https://github.com/ethz-asl/kalibr/wiki/installation>`_ ，按步骤安装

* **标定板**： kalibr支持 ``chessbord`` , ``circlegrid`` , ``aprilgrid`` ， 这里选择 ``aprilgrid`` ,标定板文件可以通过直接 `下载 <https://github.com/ethz-asl/kalibr/wiki/downloads>`_ ，或者通过kalibr工具生成标定板:

.. code-block:: bash

  $ kalibr_create_target_pdf --type 'apriltag' --nx 6 --ny 6 --tsize 0.08 --tspace 0.3

通过该命令查看kalibr_create_target_pdf参数意义：

.. code-block:: bash

  $ kalibr_create_target_pdf --h
  usage:
      Example Aprilgrid:
          kalibr_create_target_pdf --type apriltag --nx 6 --ny 6 --tsize 0.08 --tspace 0.3
      Example Checkerboard:
          kalibr_create_target_pdf --type checkerboard --nx 6 --ny 6 -csx 0.05 --csy 0.1


  Generate PDFs of calibration patterns.

  optional arguments:
    -h, --help           show this help message and exit

  Output options:
    output               Output filename
    --eps                Also output an EPS file

  Generic grid options:
    --type GRIDTYPE      The grid pattern type. ('apriltag' or 'checkerboard')
    --nx N_COLS          The number of tags in x direction (default: 6)
    --ny N_ROWS          The number of tags in y direction (default: 7)

  Apriltag arguments:
    --tsize TSIZE        The size of one tag [m] (default: 0.08)
    --tspace TAGSPACING  The space between the tags in fraction of the edge size
                        [0..1] (default: 0.3)
    --tfam TAGFAMILIY    Familiy of April tags ['t16h5', 't25h9', 't25h7',
                        't36h11'] (default: t36h11)

  Checkerboard arguments:
    --csx CHESSSZX       The size of one chessboard square in x direction [m]
                        (default: 0.05)
    --csy CHESSSZY       The size of one chessboard square in y direction [m]
                        (default: 0.05)

* **标定imu内参** ：kalibr默认情况下要求imu数据是经过内参标定的。内参标定工具使用 `imu-tk <https://github.com/Kyle-ak/imu_tk.git>`_ .

* **imu 统计数据参数**：
    * noise density
    * bias random walk

我们使用 Allan分析工具 `imu_utils <https://github.com/gaowenliang/imu_utils>`_ 得到上面的imu统计数据特性，并以 如下 ``imu.yaml`` 格式化输出：

.. code-block:: bash

  #Accelerometers
  accelerometer_noise_density: 0.02680146180736048   #Noise density (continuous-time)
  accelerometer_random_walk:   0.0026296086159332804   #Bias random walk

  #Gyroscopes
  gyroscope_noise_density:     0.008882328296710996   #Noise density (continuous-time)
  gyroscope_random_walk:       0.00037956578292701033   #Bias random walk

  rostopic:                    /mynteye/imu/data_raw      #the IMU ROS topic
  update_rate:                 200.0      #Hz (for discretization of the values above)

标定左右目之间的位姿关系
------------------------

* 收集标定图像：kalibr支持通过 ``rosbag`` 和采集离线图像两种方式收集所需要的标定图像，这里使用更加方便的 ``rosbag`` 的方式，采集图像的方式 `参考链接 <https://github.com/ethz-asl/kalibr/wiki/bag-format>`_ .
* 通过 ``rosbag`` 采集图像的方法：固定小觅相机，在相机视野中移动 ``aprilgrid`` 标定板.
* 为了避免采集数据的冗余，增加标定的时间， 应尽量使用更低帧率的图像采集数据，kalibr推荐使用 ``4Hz`` 图像帧率,这里使用 ``10hz`` .
* 小觅相机s系列提供最低10hz的图像，可以使用 `topic_tools <http://wiki.ros.org/topic_tools/throttle>`_ 修改发布频率,因为使用10hz需要更多的标定时间.
* 录制 ``static.bag`` : 固定好小觅相机后，启动 `wrapper <https://github.com/slightech/MYNT-EYE-S-SDK>`_ ,录制左右图像的topic到 ``static.bag`` .

.. code-block:: bash

  $ source wrappers/ros/devel/setup.bash
  $ roslaunch mynt_eye_ros_wrapper display.launch
  $ cd ~
  $ mkdir -p bag
  $ cd bag
  $ rosbag record -O static_10hz /mynteye/left/image_raw /mynteye/right/image_raw #建议使用10hz,你也可以使用topic_tools发布4hz.

* kalibr标定：

.. code-block:: bash

  $ kalibr_calibrate_cameras --target aprilgrid.yaml --bag ~/bag/static_10hz.bag --models pinhole-radtan pinhole-radtan --topics /mynteye/left/image_raw /mynteye/right/image_raw

通过该命令帮助查看kalibr_calibrate_cameras参数意义：

.. code-block:: bash

  $ kalibr_calibrate_cameras --h

  Calibrate the intrinsics and extrinsics of a camera system with non-shared
  overlapping field of view.

  usage:
    Example usage to calibrate a camera system with two cameras using an aprilgrid.

    cam0: omnidirection model with radial-tangential distortion
    cam1: pinhole model with equidistant distortion

    kalibr_calibrate_cameras --models omni-radtan pinhole-equi --target aprilgrid.yaml \
              --bag MYROSBAG.bag --topics /cam0/image_raw /cam1/image_raw

    example aprilgrid.yaml:
        target_type: 'aprilgrid'
        tagCols: 6
        tagRows: 6
        tagSize: 0.088  #m
        tagSpacing: 0.3 #percent of tagSize

  optional arguments:
  -h, --help            show this help message and exit
  --models MODELS [MODELS ...]
                        The camera model ['pinhole-radtan', 'pinhole-equi',
                        'omni-radtan', 'pinhole-fov'] to estimate

  Data source:
  --bag BAGFILE         The bag file with the data
  --topics TOPICS [TOPICS ...]
                        The list of image topics
  --bag-from-to bag_from_to bag_from_to
                        Use the bag data starting from up to this time [s]

  Calibration target configuration:
  --target TARGETYAML   Calibration target configuration as yaml file

  Image synchronization:
  --approx-sync MAX_DELTA_APPROXSYNC
                        Time tolerance for approximate image synchronization
                        [s] (default: 0.02)

  Calibrator settings:
  --qr-tol QRTOL        The tolerance on the factors of the QR decomposition
                        (default: 0.02)
  --mi-tol MITOL        The tolerance on the mutual information for adding an
                        image. Higher means fewer images will be added. Use -1
                        to force all images. (default: 0.2)
  --no-shuffle          Do not shuffle the dataset processing order

  Outlier filtering options:
  --no-outliers-removal
                        Disable corner outlier filtering
  --no-final-filtering  Disable filtering after all views have been processed.
  --min-views-outlier MINVIEWOUTLIER
                        Number of raw views to initialize statistics (default:
                        20)
  --use-blakezisserman  Enable the Blake-Zisserman m-estimator
  --plot-outliers       Plot the detect outliers during extraction (this could
                        be slow)

  Output options:
  --verbose             Enable (really) verbose output (disables plots)
  --show-extraction     Show the calibration target extraction. (disables
                        plots)
  --plot                Plot during calibration (this could be slow).
  --dont-show-report    Do not show the report on screen after calibration.

标定完成后输出下面3个文件:

  * ``camchain-homezhangsbagstatic_10hz.yaml``
  * ``report-cam-homezhangsbagstatic_10hz.pdf``
  * ``results-cam-homezhangsbagstatic_10hz.txt``

.. tip::

  如果您在vins中使用相机参数，选择pinhole-equi 模型 或者 omni-radtan模型效果会更好, 如果您在maplab中使用相机参数，请选择pinhole-equi模型

标定相机和IMU坐标系之间的位姿关系
---------------------------------

* **收集标定数据**：跟上面标定相机之间的位姿关系一样，kalibr支持两种收集数据的方法,这里仍然使用 ``rosbag`` 的方式.
    * 采集图像的方法： 固定 ``apilgrid`` 标定板,移动相机
    * 保证采集数据是良好的： 标定板亮度要适宜，太亮或太暗不能保证数据的质量, 同时也不要晃动太快，避免图像出现模糊.
    * 设置imu发布频率为200Hz, 图像的发布频率为20hz（kalibr推荐）
    * 充分激励imu的每个轴，例如可以在每个轴上3个动作，然后在“８字型”运动

* 录制相机与imu的bag为 ``dynamic.bag``

.. code-block:: bash

  $ roslaunch mynt_eye_ros_wrapper display.launch
  $ cd bag
  $ rosbag record -O dynamic /mynteye/left/image_raw /mynteye/right/image_raw /mynteye/imu/data_raw #注意设置图像发布频率为20hz, imu发布频率为200hz

* kalibr 标定：

.. code-block:: bash

  $ kalibr_calibrate_imu_camera --cam camchain-homezhangsbagstatic_10hz.yaml --target aprilgrid.yaml --imu imu.yaml --time-calibration　--bag ~/bag/dynamic.bag

通过该命令帮助查看kalibr_calibrate_imu_camera参数意义：

.. code-block:: bash

  $ kalibr_calibrate_imu_camera --h

  Calibrate the spatial and temporal parameters of an IMU to a camera chain.

  usage:
      Example usage to calibrate a camera system against an IMU using an aprilgrid
      with temporal calibration enabled.

      kalibr_calibrate_imu_camera --bag MYROSBAG.bag --cam camchain.yaml --imu imu.yaml \
              --target aprilgrid.yaml --time-calibration

      camchain.yaml: is the camera-system calibration output of the multiple-camera
                    calibratin tool (kalibr_calibrate_cameras)

      example aprilgrid.yaml:       |  example imu.yaml: (ADIS16448)
          target_type: 'aprilgrid'  |      accelerometer_noise_density: 0.006
          tagCols: 6                |      accelerometer_random_walk: 0.0002
          tagRows: 6                |      gyroscope_noise_density: 0.0004
          tagSize: 0.088            |      gyroscope_random_walk: 4.0e-06
          tagSpacing: 0.3           |      update_rate: 200.0

  optional arguments:
    -h, --help            show this help message and exit

  Dataset source:
    --bag BAGFILE         Ros bag file containing image and imu data (rostopics
                          specified in the yamls)
    --bag-from-to bag_from_to bag_from_to
                          Use the bag data starting from up to this time [s]
    --perform-synchronization
                          Perform a clock synchronization according to 'Clock
                          synchronization algorithms for network measurements'
                          by Zhang et al. (2002).

  Camera system configuration:
    --cams CHAIN_YAML     Camera system configuration as yaml file
    --recompute-camera-chain-extrinsics
                          Recompute the camera chain extrinsics. This option is
                          exclusively recommended for debugging purposes in
                          order to identify problems with the camera chain
                          extrinsics.
    --reprojection-sigma REPROJECTION_SIGMA
                          Standard deviation of the distribution of reprojected
                          corner points [px]. (default: 1.0)

  IMU configuration:
    --imu IMU_YAMLS [IMU_YAMLS ...]
                          Yaml files holding the IMU noise parameters. The first
                          IMU will be the reference IMU.
    --imu-delay-by-correlation
                          Estimate the delay between multiple IMUs by
                          correlation. By default, no temporal calibration
                          between IMUs will be performed.
    --imu-models IMU_MODELS [IMU_MODELS ...]
                          The IMU models to estimate. Currently supported are
                          'calibrated', 'scale-misalignment' and 'scale-
                          misalignment-size-effect'.

  Calibration target:
    --target TARGET_YAML  Calibration target configuration as yaml file

  Optimization options:
    --time-calibration    Enable the temporal calibration
    --max-iter MAX_ITER   Max. iterations (default: 30)
    --recover-covariance  Recover the covariance of the design variables.
    --timeoffset-padding TIMEOFFSET_PADDING
                          Maximum range in which the timeoffset may change
                          during estimation [s] (default: 0.01)

  Output options:
    --show-extraction     Show the calibration target extraction. (disables
                          plots)
    --extraction-stepping
                          Show each image during calibration target extraction
                          (disables plots)
    --verbose             Verbose output (disables plots)
    --dont-show-report    Do not show the report on screen after calibration.

标定完成后输出下面4个文件：
  * ``camchain-imucam-homezhangsbagdynamic.yaml``
  * ``imu-homezhangsbagdynamatic.yaml``
  * ``report-imucam-homezhangsbagdynamic.pdf``
  * ``results-imucam-homezhangsbagdynamic.yaml``