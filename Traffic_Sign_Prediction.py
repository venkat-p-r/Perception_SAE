#!python -m pip install --upgrade pip

#!pip install tensorflow==2.3.1 

#!pip install tensorboard==2.4.1
#!pip install torch

import torch
import os
from IPython.display import Image
from random import choice
import shutil



from google.colab import drive
drive.mount('/content/gdrive')



#os.chdir('gdrive/My Drive/TrafficDetection')




#pwd




#!git clone https://github.com/ultralytics/yolov5




#cd 'yolov5'




#!python train.py --img 415 --batch 16 --epochs 30 --data dataset.yaml --weights yolov5s.pt --cache




%load_ext tensorboard
%tensorboard --logdir runs




Image(filename='runs/train/exp2/train_batch0.jpg', width=416)




Image(filename='runs/train/exp2/val_batch0_pred.jpg', width=416)




!python detect.py --source runs/detect/exp/ --weights runs/train/exp3/weights/best.pt --conf 0.25


