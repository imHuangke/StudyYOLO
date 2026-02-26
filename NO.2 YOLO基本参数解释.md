# YOLOV12预测参数介绍

- YOLOV12文档：https://docs.ultralytics.com
-  YOLOGithub主页：https://github.com/ultralytics/ultralytics
- 预测参数文档：https://docs.ultralytics.com/usage/cfg/#predict
- 所有模型：https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models



## 几个比较重要的预测参数

### 基础参数

| 参数    | 描述                                                   |
| ------- | ------------------------------------------------------ |
| source  | 输入模型预测的图像、视频、文件夹路径                   |
| device  | 计算设备（device=0 或 device=0,1,2,3 或 device='cpu'） |
| verbose | 是否在命令行输出每一帧的预测结果，默认为True           |

### 后处理参数

| 参数         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| conf         | 目标检测置信度，默认0.25                                     |
| iou          | 目标检测非极大值抑制（NMS）的IOU阈值，默认0.7，越小，NMS越强 |
| agnostic_nms | 对所有类的框，而不仅仅对同类框，做目标检测非极大值抑制（NMS） |
| classes      | 只显示哪个或哪些类别的预测结果（class=0 或 class=[0,2,3]）   |

### 可视化参数

| 参数         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| show         | 是否将预测结果显示在屏幕上，默认为False。摄像头实时预测时，建议开启 |
| show_labels  | 是否显示目标检测框类别文字，默认为True                       |
| show_conf    | 是否显示目标检测框置信度，默认为True                         |
| line_width   | 目标检测框线宽，默认为3                                      |
| max_det      | 一张图像最多预测多少个框，默认为300                          |
| boxes        | 是否在实例分割预测结果中显示目标检测框                       |
| visualize    | 可视化模型特征                                               |
| retina_masks | 是否显示高分辨率实例分割mask，默认为False                    |

### 保存结果参数

| 参数      | 描述                                              |
| --------- | ------------------------------------------------- |
| save      | 保存预测结果可视化图像，默认为False               |
| save_txt  | 将预测结果保存为txt文件，默认为False              |
| save_conf | 保存的预测结果中，包含置信度，默认为False         |
| save_crop | 保存的预测结果可视化图像中，是否裁切，默认为False |

###  **其它参数**

| 参数 | 描述                                |
| ---- | ----------------------------------- |
| half | 是否开启半精度（FP16），默认为False |



- ​
