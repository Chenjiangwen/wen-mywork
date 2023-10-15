"""
   kuzu.py
   COMP9444, CSE, UNSW
"""

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F


class NetLin(nn.Module):
    # linear function followed by log_softmax
    def __init__(self):
        super(NetLin, self).__init__()
        self.lin_layer = nn.Linear(784, 10)  #28*28 = 784.

    def forward(self, x):
        x = x.view(x.shape[0], -1)   #flattening the inputs.
        x = F.log_softmax(self.lin_layer(x), dim=1)
        return x


class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        self.fc_layer_1 = nn.Linear(784, 256)
        self.fc_layer_2 = nn.Linear(256, 10)

    def forward(self, x):
        x = x.view(x.shape[0], -1)
        x = torch.tanh(self.fc_layer_1(x))
        x = self.fc_layer_2(x)
        x = torch.log_softmax(x, dim=1)
        return x



class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        self.conv1=nn.Conv2d(in_channels = 1, out_channels = 64,kernel_size = 5, padding=2)
        self.max_pool=nn.MaxPool2d(2,2)
        self.conv2=nn.Conv2d(in_channels =64,out_channels = 24,kernel_size = 5, padding=2)
        self.fc_layer_1=nn.Linear(1176,159)
        self.fc_layer_2=nn.Linear(159,10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.max_pool(x)
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)
        x = x.view(x.size(0), -1)  #flattening the inputs.
        x = F.relu(self.fc_layer_1(x))
        x = self.fc_layer_2(x)
        x = F.log_softmax(x, dim=1)
        return x

print('=======================================================')
model1 = NetLin()
for name, param in model1.named_parameters():
    if param.requires_grad:
        print(name, param.numel())
print("The total number of parameters in the NetLin is {}".format(sum(x.numel() for x in model1.parameters())))


print('=======================================================')
model2 = NetFull()
for name, param in model2.named_parameters():
    if param.requires_grad:
        print(name, param.numel())
print("The total number of parameters in the NetFull is {}".format(sum(x.numel() for x in model2.parameters())))


print('=======================================================')
model3 = NetConv()
for name, param in model3.named_parameters():
    if param.requires_grad:
        print(name, param.numel())
print("The total number of parameters in the NetConv is {}".format(sum(x.numel() for x in model3.parameters())))