# **Y**ou **O**nly **L**ook **A**t **C**oefficien**T**s
```
    ██╗   ██╗ ██████╗ ██╗      █████╗  ██████╗████████╗
    ╚██╗ ██╔╝██╔═══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝
     ╚████╔╝ ██║   ██║██║     ███████║██║        ██║   
      ╚██╔╝  ██║   ██║██║     ██╔══██║██║        ██║   
       ██║   ╚██████╔╝███████╗██║  ██║╚██████╗   ██║   
       ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝ 
```

A simple, fully convolutional model for real-time instance segmentation. This is the code for [our paper](https://arxiv.org/abs/1904.02689).

## Brief introduction
### 1. Development environment
#### Python version : 3.7.4
#### Framework : Pytorch
#### Hardware : NVIDIA GeForce GTX 1080 Ti 11GB

### 2. How to run the code.
#### (1)Setup the environment.
#### (2)Prepared an imagenet-pretrained model and put it in ./weights
##### Prepared testing images in data/train_images
##### Prepared gound truth file in data/pascal_train.json
##### I use Pretrained on ImageNet dataset and ResNet101 based.
#### (3)Run
```python train.py --config=yolact_base_config --batch_size=5```
##### It will create .pth files in the ./weights every 10000 iterators and after interruption.
#### (4)Resume training, Run.
```python3 train.py --config=yolact_base_config --resume=weights/yolact_base_297_50000.pth --start_iter=-1```
#### (5)Predict one single image
##### Run 
```python3 eval.py --trained_model=weights/res101/yolact_base_297_50000.pth --score_threshold=0.15 --top_k=15 --image=data/test_images/2007_005460.jpg```
#### (6)Create JSON file.
##### Make sure testing images is in data/test_images.
##### Make sure the test.json is in data/
##### Run
```python3 createJSON.py --trained_model=weights/res101/yolact_base_297_50000.pth --score_threshold=0.15```
##### The predict file will create in results/mask_detections.json

## Methodology
#### This model brings a realtime instance segmentation framework that forget localization step.
#### YOLACT breaks up instance segmentation into two parallel tasks:
#### (1) Generating a dictionary of non-local prototype masks over the entire image.
#### (2) Predicting a set of linear combination coefficients per instance.
#### The most advantages is that it is fast: because of its parallel structure and extremely lightweight assembly process.
#### It is the first real-time (> 30 fps) instance segmentation algorithm.

