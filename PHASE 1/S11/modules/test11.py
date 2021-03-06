# -*- coding: utf-8 -*-
"""test10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mc5l9vvaC3yxqVUB1nyB9RusbEfKdmIq
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
from tqdm import tqdm

test_losses = []
test_acc = []
misclassified = []
correct_pics = []
def test(model, device, test_loader, loss_func, last_epoch):
    model.eval()
    correct = 0
    test_loss = 0                                   
    with torch.no_grad():
        for data, target in test_loader:
            img_batch = data
            data, target = data.to(device), target.to(device)  # Get samples
            output = model(data)  # Get trained model output
            test_loss += loss_func(output, target).item()  # Sum up batch loss
            pred = output.argmax(dim=1, keepdim=False)  # Get the index of the max log-probability
            result = pred.eq(target.view_as(pred))

            if last_epoch:
              for i in range(len(list(result))):
                if not list(result)[i] and len(misclassified) < 25:
                  misclassified.append({
                      'prediction': list(pred)[i],
                      'label': list(target.view_as(pred))[i],
                      'image': img_batch[i]})
                
                elif list(result)[i] and len(correct_pics) < 25:
                  correct_pics.append({
                      'prediction': list(pred)[i],
                      'label': list(target.view_as(pred))[i],
                      'image': img_batch[i]

                        })


            correct += result.sum().item()

            
          

    test_loss /= len(test_loader.dataset)
    test_losses.append(test_loss)

    test_acc.append(100. * correct / len(test_loader.dataset))
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
    
    


def test_class_performance(model, device, test_loader, classes):
    class_correct = list(0. for i in range(10))
    class_total = list(0. for i in range(10))
    with torch.no_grad():
        pbar = tqdm(test_loader)
        for i, (data, target) in enumerate(pbar):
            data, target = data.to(device), target.to(device)
            outputs = model(data)
            _, predicted = torch.max(outputs, 1)
            c = (predicted == target).squeeze()
            for i in range(4):
                label = target[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1


    for i in range(10):
        print('Accuracy of %5s : %2d %%' % (classes[i], 100 * class_correct[i] / class_total[i]))