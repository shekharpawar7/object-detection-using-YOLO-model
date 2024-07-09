
## Overview
description: |
 Default YOLO Objects: Predefined YOLO models (like YOLOv5 or YOLOv4) come with a set of objects they can detect based on the dataset they were trained on (e.g., COCO dataset includes objects like persons, motorcycles, cars, etc.).

Custom Object Detection:

Collect Data: Gather images and annotate them with the objects you want to detect (e.g., persons, motorcycles).
Train Model: Use a YOLO training pipeline (with frameworks like Ultralytics YOLO or Darknet) to train a model with your custom dataset.
Use Model: After training, you can use this custom model to detect the objects it was trained on.
Implementation with Ultralytics YOLO:

Install: Ensure you have the ultralytics library installed. You can do this with pip install ultralytics.
Prepare Data: Format your dataset in the YOLO format and create a configuration file that defines your classes (e.g., person, motorcycle).
Train: Run the training script to create a model that can detect your specified objects.
Detect Objects: Use the trained model to make predictions on new images.

## Datasets pre bulid 
  - person
  - bird
  - cat
  - cow
  - dog
  - horse
  - sheep
  - aeroplane
  - bicycle
  - boat
  - bus
  - car
  - motorbike
  - train
  - bottle
  - chair
  - dining table
  - potted plant
  - sofa
  - tv/monitor

COCO_Classes:
  - person
  - bicycle
  - car
  - motorbike
  - aeroplane
  - bus
  - train
  - truck
  - boat
  - traffic light
  - fire hydrant
  - stop sign
  - parking meter
  - bench
  - cat
  - dog
  - horse
  - sheep
  - cow
  - elephant
  - bear
  - zebra
  - giraffe
  - backpack
  - umbrella
  - handbag
  - tie
  - suitcase
  - frisbee
  - skis
  - snowboard
  - sports ball
  - kite
  - baseball bat
  - baseball glove
  - skateboard
  - surfboard
  - tennis racket
  - bottle
  - wine glass
  - cup
  - fork
  - knife
  - spoon
  - bowl
  - banana
  - apple
  - sandwich
  - orange
  - broccoli
  - carrot
  - hot dog
  - pizza
  - donut
  - cake
  - chair
  - sofa
  - pottedplant
  - bed
  - diningtable
  - toilet
  - tvmonitor
  - laptop
  - mouse
  - remote
  - keyboard
  - cell phone
  - microwave
  - oven
  - toaster
  - sink
  - refrigerator
  - book
  - clock
  - vase
  - scissors
  - teddy bear
  - hair drier
  - toothbrush

    ![output](https://github.com/shekharpawar7/object-detection-using-YOLO-model/blob/main/1_Ic-ME4SgJeIgRDZvZu0ivw.jpg)


## Installation

### Dependencies
- ROS: [Installation Guide](http://wiki.ros.org)
- OpenCV: [Website](http://opencv.org/)


