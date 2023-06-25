import numpy as np
import cv2 as cv
import os

IMAGE_SIZE = (50, 50)

PCA_NUM = 20
# 1、加载训练集中的脸，转为一个M行N列矩阵T
def load_data(path):
    # 查看路径下所有文件
    train_file_path = os.listdir(path)
    # 计算有几个文件（图片命名都是以 序号.jpg方式）减去Thumbs.db
    file_number = len(train_file_path) - 1
    T = []
    # 把所有图片转为1-D并存入T中
    for i in range(1, file_number + 1):
        image = cv.imread(path + '/' + str(i) + '.jpg', cv.IMREAD_GRAYSCALE)
        image = cv.resize(image, IMAGE_SIZE)
        # 转为1-D
        image = image.reshape(image.size, 1)
        T.append(image)
    T = np.array(T)
    # 不能直接T.reshape(T.shape[1],T.shape[0]) 这样会打乱顺序，
    T = T.reshape(T.shape[0], T.shape[1])
    return np.mat(T).T


def PCA(T):
    # 2、对T进行0均值化
    # 把均值变为0 axis = 1代表对各行求均值
    m = T.mean(axis=1)
    A = T - m


    # 计算 A.T(转置) * A 的特征向量和特征值, 其中 V 是特征值，D 是特征向量
    L = (A.T) * (A)
    # L = (A) * (A.T)
    # print("T:", T.shape)
    # print("A:", A.shape)
    # print("m:", m.shape)
    V, D = np.linalg.eig(L)  # 特征分解
    idx = V.argsort()[::-1]
    V = V[idx]
    D = D[:,idx]

    # 计算 A *AT的特征向量
    eigenface = A * D
    eigenface = eigenface[:,:PCA_NUM]
    return eigenface, m, A


def recognize(testImage, eigenface, m, A):
    _, trainNumber = np.shape(A)
    # 4、计算投影后的矩阵P
    # 投影到特征脸后的
    projectedImage = eigenface.T * (A)
    # 可解决中文路径不能打开问题
    testImageArray = cv.imdecode(np.fromfile(testImage, dtype=np.uint8), cv.IMREAD_GRAYSCALE)
    # 转为1-D
    testImageArray = cv.resize(testImageArray, IMAGE_SIZE)
    testImageArray = testImageArray.reshape(testImageArray.size, 1)
    testImageArray = np.mat(np.array(testImageArray))
    differenceTestImage = testImageArray - m

    projectedTestImage = eigenface.T * (differenceTestImage)
    distance = []
    # 6、计算test_P和P中每个样本的距离，选出最近的那个即可
    for i in range(0, trainNumber):
        q = projectedImage[:, i]
        temp = np.linalg.norm(projectedTestImage - q)
        distance.append(temp)

    minDistance = min(distance)
    index = distance.index(minDistance)
    print('similar index is ', index + 1)
    cv.imshow("test data", cv.imread(testImage, cv.IMREAD_GRAYSCALE))

    cv.imshow("recognize result", cv.imread('../data/TrainDatabase' + '/' + str(index + 1) + '.jpg', cv.IMREAD_GRAYSCALE))
    cv.waitKey()
    return index + 1


# 进行人脸识别主程序
def example(filename):
    T = load_data('data/TrainDatabase')
    eigenface, m, A = PCA(T)
    testimage = filename
    print(testimage)
    print(recognize(testimage, eigenface, m, A))


if __name__ == '__main__':
    example('data/TestDatabase/4.jpg')
