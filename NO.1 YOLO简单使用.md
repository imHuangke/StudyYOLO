# YOLO使用教程

## 什么是YOLO？

YOLO（You Only Look Once） 是一种实时目标检测算法，特点是：

🚀 速度快（单阶段检测）

🎯 精度高（持续版本迭代）

🧠 易上手（Ultralytics YOLOv12）

本教程以 Ultralytics YOLO（v12 思路通用） 为例。

官方文档地址：https://docs.ultralytics.com/zh/models/yolo12/

### YOLO的特点：
- **精度高**：在保持速度的同时具有较高的检测精度
- **端到端训练**：单一网络完成所有检测任务

## 安装YOLO

### 环境要求
- Python 3.7+
- PyTorch 1.7+
- CUDA（可选，用于GPU加速）

### 安装步骤

**下载YOLO**：

```python
# 使用 pip 安装软件包
pip install -U ultralytics
```
## 基本使用

### 1. 使用预训练模型进行推理

```python
from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov12n.pt')

# 图片路径
img = 'img/1.jpg'

# 进行推理
results = model(
	source = img, 	# 输入模型预测的图像、视频、文件夹路径
	device = 'cpu', # 计算设备（device=0 或 device=0,1,2,3(多GPU) 或 device='cpu'）
	show = True, 	# 是否将预测结果显示在屏幕上，默认为False。摄像头实时预测时，建议开启
    save = True,	# 是否保存结果
)
```

- ​
