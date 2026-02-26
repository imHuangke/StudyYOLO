from ultralytics import YOLO

modle = YOLO('yolov12.pt')

img = 'img/1.jpg'

results = modle.(

)