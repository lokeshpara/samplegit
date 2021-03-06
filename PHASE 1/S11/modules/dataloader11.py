# -*- coding: utf-8 -*-
"""dataloader11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xugaRhLOi4O8rMQcX0Q0P_E_7uwYxqzR
"""

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
# %matplotlib inline
import matplotlib.pyplot as plt
import torchvision
import numpy as np
import torchvision.transforms as transforms
import albumentations
from albumentations.pytorch import ToTensor
import cv2
class Albumentation():
    def __init__(self):
        self.Albumentation_transform = albumentations.Compose([
                albumentations.PadIfNeeded(40,40,cv2.BORDER_REFLECT,True),
                albumentations.RandomCrop(32,32,True),                                         
                albumentations.HorizontalFlip(p=0.5),
                #albumentations.RandomRotate90(True),
                #albumentations.Rotate(-20,20),
                albumentations.Normalize((0.485, 0.456, 0.406),(0.229, 0.224, 0.225)),
                albumentations.Cutout(1,16,16,True),
                ToTensor(),
            ])
   
         
    def __call__(self,image):
        image_numpy = np.array(image)
        augmented = self.Albumentation_transform(image=image_numpy)
        image = augmented['image']
        return image    

train_transform = transforms.Compose(
    [
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ]
)

test_transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ]
)

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)


# Train set with albumentation
trainset_with_Albumentation = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=Albumentation())


testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transform)

SEED = 1

# CUDA?
cuda = torch.cuda.is_available()
print("CUDA Available?", cuda)

# For reproducibility
torch.manual_seed(SEED)

if cuda:
    torch.cuda.manual_seed(SEED)

dataloader_args = dict(shuffle=True, batch_size=512, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)

dataloader_args_Albumentation = dict(shuffle=True, batch_size=4, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)


# train dataloader
train_loader = torch.utils.data.DataLoader(trainset, **dataloader_args)


train_loader_Albumentation = torch.utils.data.DataLoader(trainset_with_Albumentation, **dataloader_args)

# To view images
train_loader_Alb = torch.utils.data.DataLoader(trainset_with_Albumentation, **dataloader_args_Albumentation)

# test dataloader
test_loader = torch.utils.data.DataLoader(testset, **dataloader_args)

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

