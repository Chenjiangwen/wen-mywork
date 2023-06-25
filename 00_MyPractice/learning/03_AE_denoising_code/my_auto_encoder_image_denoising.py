import os

import numpy as np
from os import listdir
from PIL import Image
import torch
import matplotlib.pyplot as plt
import time
import math
from torch import nn, optim
from torchvision.datasets import MNIST
from torchvision.transforms import ToPILImage
from skimage.metrics import peak_signal_noise_ratio as psnr
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class AutoEncoder(nn.Module):
    def __init__(self):
        super(AutoEncoder, self).__init__()
        # 编码
        self.encoder = nn.Sequential(
            # 输入通道 1，输出通道 32，卷积核 3x3，卷积步长 1
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.ReLU()
        )
        # 解码
        self.decoder = nn.Sequential(

            nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Upsample(scale_factor=2, mode="nearest"),

            nn.Conv2d(64, 32, kernel_size=3, stride=1, padding=1),
            nn.Conv2d(32, 1, kernel_size=3, stride=1, padding=1),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.encoder(x)
        return self.decoder(x)

class Trainer:
    def __init__(self, batch_size, epochs):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("device: {}".format(self.device))
        self.net = AutoEncoder().to(self.device)
        self.loss_fn = nn.MSELoss()
        self.opt = torch.optim.Adam(self.net.parameters())
        self.BATCH_SIZE = batch_size
        self.EPOCHS = epochs

    def get_train_data(self):
        train_set = MNIST(root="./data", train=True)
        origin_x = train_set.data.float()
        train_x = torch.clamp(origin_x + torch.randn(60000, 28, 28) * 100, 0, 255) / 255.
        train_y = origin_x / 255.

        return train_x.unsqueeze(1), train_y.unsqueeze(1)

    def get_test_data(self):
        test_set = MNIST(root="./data", train=False)
        origin_x = test_set.data.float()
        test_x = torch.clamp(origin_x + torch.randn(10000, 28, 28) * 100, 0, 255) / 255.
        test_y = origin_x / 255.
        return test_x.unsqueeze(1), test_y.unsqueeze(1)

    def train(self):
        train_x, train_y = self.get_train_data()
        train_x = train_x.to(self.device)
        train_y = train_y.to(self.device)

        # 打乱数据
        index = torch.randperm(train_x.shape[0])
        train_x = train_x[index]
        train_y = train_y[index]

        sample_count = train_x.shape[0]
        batch_count = int(math.ceil(train_x.shape[0] / self.BATCH_SIZE))
        # batch_count /= 2
        print("samples: {}, batches : {}, epochs: {}".format(sample_count, batch_count, self.EPOCHS))
        losses = []
        count = 0
        batchnum = 0
        tic = time.time()
        for i in range(self.EPOCHS):
            epoch_tic = time.time()
            batchnum = 0
            for j in range(0, train_x.shape[0], self.BATCH_SIZE):

                batchnum += 1
                # if batchnum <= batch_count:
                print("batchnum: {} / batch_count: {}".format(batchnum, batch_count))
                x = train_x[j: j + self.BATCH_SIZE]
                y = train_y[j: j + self.BATCH_SIZE]

                out = self.net(x)
                loss = self.loss_fn(out, y)
                lossval = loss.item()
                if j % 10 == 0:
                    losses.append(lossval)
                    if j % 100 == 0:
                        # if j%1 == 0:
                        print("epoch: {} / {}, batch: {} / {}, loss: {}".format(
                            i + 1,
                            self.EPOCHS,
                            int(j / self.BATCH_SIZE) + 1,
                            batch_count,
                            loss.float()
                        ))
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

            epoch_toc = time.time()

            plt.clf()
            fig = plt.gcf()
            plt.title("loss")
            plt.plot(losses)

            count += 1
            fig.savefig("./imgs/My_loss/loss_{}.jpg".format(count))
            print("epoch {} time cost: {}s".format(i + 1, epoch_toc - epoch_tic))
            print("*" * 20)
        toc = time.time()
        print("train time cost: {}s".format(toc - tic))
        torch.save(self.net, "./models/my_removenoise.pth")

    def predictModel(self):
        net = torch.load("./models/my_removenoise.pth")
        test_x, test_y = self.get_test_data()
        test_x = test_x.to(self.device)

        toPIL = ToPILImage("L")
        fig_count = 0

        for i in range(0, test_x.shape[0], self.BATCH_SIZE):
            x = test_x[i:i + self.BATCH_SIZE]
            y = test_y[i:i + self.BATCH_SIZE]

            tic = time.time()
            out = net(x)
            out = torch.sigmoid(out)
            toc = time.time()
            print("batch predict time cost: {}s".format(toc - tic))
            # 每个 batch 输出一次图像
            for j in range(0, 1):
                plt.imsave('./imgs/pic_group/Origin_Image/Origin_{}.jpg'.format(fig_count), toPIL(y[j]))
                plt.imsave('./imgs/pic_group/My_Out_Image/MyOut_{}.jpg'.format(fig_count), toPIL(out[j].cpu()))
                fig_count += 1

    def calculate_psnr(self):
        psnr_arr = []

        path1 = 'imgs/pic_group/Origin_Image/'
        path2 = 'imgs/pic_group/My_Out_Image/'

        Origin_Image_list = [Image.open(path1 + fn) for fn in listdir(path1) if fn.endswith('.jpg')]
        Out_Image_list = [Image.open(path2 + fn) for fn in listdir(path2) if fn.endswith('.jpg')]

        for i in range(len(Origin_Image_list)):
            psnr_t = psnr(np.uint8(Origin_Image_list[i]), np.uint8(Out_Image_list[i]))
            print(i, 'psnr:', psnr_t)
            psnr_arr.append(psnr_t)

            plt.clf()
            fig = plt.gcf()
            plt.subplot(1, 2, 1)
            plt.title("Origin Image")
            plt.axis("off")
            plt.imshow(Origin_Image_list[i])
            plt.text(14, 33, ' PSNR:' + str(psnr_arr[i]),
                     bbox=dict(facecolor='yellow', alpha=0.5), fontsize=15)

            plt.subplot(1, 2, 2)
            plt.title("My Out Image")
            plt.axis("off")
            plt.imshow(Out_Image_list[i])

            fig.savefig("./imgs/pic_group/My_Image_psnr/My_psnr_{}.jpg".format(i))
            plt.pause(0.2)

        print('psnr_average:', np.average(np.array(psnr_arr)))


def demo(batch_size=512, epochs=50, train=True):
    t = Trainer(batch_size, epochs)
    if train:
        t.train()
    t.predictModel()
    t.calculate_psnr()

if __name__ == '__main__':
    batch_size = 512
    epochs = 3
    # train 决定是否重新训练
    demo(batch_size, epochs, train=False)