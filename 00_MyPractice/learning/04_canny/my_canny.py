import matplotlib.pyplot as plt
import numpy as np
import cannyClass
import cv2


# 灰度化
# def gray(img):
#     """
#     Calculate function:
#     Gray(i,j) = 0.299 * R(i,j) + 0.587 * G(i,j) + 0.114 * B(i,j)
#     """
#     # 读取图片
#     # img = plt.imread(img_path)
#     # 转换成 RGB 格式
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # 灰度化
#     img_gray = np.dot(img_rgb[..., :3], [0.299, 0.587, 0.114])
#     return img_gray


def edge_detection(img_gray):
    canny = cannyClass.Canny()
    new_gray = canny.smooth(img_gray)
    dx, dy, M, _ = canny.gradients(new_gray)
    NMS = canny.NMS(M, dx, dy)
    DT = canny.double_threshold(NMS)
    return DT


def run(path, pretreatment):
    global hg_img
    img = cv2.imread(path, 0)
    if pretreatment:
        # img = cv2.imread('./image/girl2.png', 0)
        # 一、先均衡 使用cv2.equalizeHist实现像素点的均衡化
        ret = cv2.equalizeHist(img)
        # 使用plt.hist绘制像素直方图
        plt.subplot(121)
        plt.hist(img.ravel(), 256)
        plt.subplot(122)
        plt.hist(ret.ravel(), 256)
        plt.show()

        # 二、矫正 gamma 矫正 gamma=1.5
        ret = ret / 255.
        # hg_img = np.power(ret / float(np.max(ret)), 1 / 1.5)
        hg_img = np.power(ret / float(np.max(ret)), 2.2)
        cv2.imshow('original,equalization,gamma=1/1.5', np.hstack((img/255, ret, hg_img)))
        cv2.imshow('H,Gamma', np.hstack((ret, hg_img)))
        cv2.waitKey(0)
        DT = edge_detection(hg_img)
        plt.figure()
        plt.figure(figsize=(10, 8))
        plt.subplot(122)
        plt.title("Edge Detection")
        plt.imshow(DT, cmap="gray")
        plt.subplot(121)
        plt.title("Original")
        plt.imshow(hg_img, cmap="gray")
        plt.savefig('./image/pretreatment_canny.png')
        plt.pause(0.5)
    else:
        DT = edge_detection(img)
        plt.figure()
        plt.figure(figsize=(10, 8))
        plt.subplot(122)
        plt.title("Edge Detection")
        plt.imshow(DT, cmap="gray")
        plt.subplot(121)
        plt.title("Original")
        plt.imshow(img, cmap="gray")
        plt.savefig('./image/canny.png')
        plt.pause(0.5)


if __name__=="__main__":
    path = './image/girl2.png'
    run(path, pretreatment=True)

