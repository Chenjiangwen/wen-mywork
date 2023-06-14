import random
import torch.nn as nn
import pandas as pd
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
from boto import sns
from tqdm import tqdm
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from apyori import apriori
import seaborn as sns
import matplotlib.pyplot as plt
#
# # trainset = datasets.CIFAR10(root='./data', train=True, download=True)
# # testset = datasets.CIFAR10(root='./data', train=False, download=True)
#
# # dog_indices = [i for i in range(len(trainset.targets)) if trainset.targets[i] == 5]
# #
# # # 随机选择10张非狗类图像的索引
# # other_indices = []
# # for class_index in range(10):
# #     if class_index != 5:
# #         class_indices = [i for i in range(len(trainset.targets)) if trainset.targets[i] == class_index]
# #         other_indices += random.sample(class_indices, 20)
# #
# # # 合并索引，并随机排列
# # train_indices = dog_indices[:20] + other_indices
# # random.shuffle(train_indices)
#
# # dog_train_indices = [i for i in range(len(trainset.targets)) if trainset.targets[i] == 5]
# # dog_train_indices = [i for i in range(len(trainset.targets)) if trainset.targets[i] == 5][:100]
# # dog_test_indices = [i for i in range(len(testset.targets)) if testset.targets[i] == 5][:100]
#
# # trainset.data = trainset.data[train_indices]
# # trainset.targets = [0] * len(train_indices)
#
# # testset.data = testset.data[dog_test_indices]
# # testset.targets = [0] * len(dog_test_indices)
#
# # 设置随机种子
# random.seed(42)
#
# 加载 CIFAR-10 训练集
trainset = datasets.CIFAR10(root='./data', train=True, download=True)

# 从 CIFAR-10 训练集中随机选择 10000 张图片的索引
train_indices = random.sample(range(len(trainset)), 1000)
trainset.data = trainset.data[train_indices]
# print(trainset.targets)

print('trainset length:', len(trainset))
# print('testset length:', len(testset))

transform = transforms.Compose([
    transforms.Resize((32, 32)),  # 调整图像尺寸
    transforms.ToTensor(),  # 将图像转换为张量
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # 归一化
])
#
trainset.transform = transform
# testset.transform = transform
class ResNet50(nn.Module):
    def __init__(self):
        super(ResNet50, self).__init__()
        self.conv = nn.Conv2d(3, 3, kernel_size=3, stride=1, padding=1, bias=False)
        self.resnet = models.resnet50(pretrained=True)
        # self.resnet.fc = nn.Linear(2048, 2)

    def forward(self, x):
        x = self.conv(x)
        x = self.resnet(x)
        return x


resnet50 = ResNet50()
# resnet50 = models.resnet50(pretrained=True)
modules = list(resnet50.children())[:-1]
resnet50 = torch.nn.Sequential(*modules)
# #
# # # 修改第一层卷积核大小
resnet50.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
#
#
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
resnet50.to(device)
#
#
def get_features(dataset):
    features = []
    for i in tqdm(range(len(dataset))):
        data, _ = dataset[i]
        data = data.to(device)
        feature = resnet50(data.unsqueeze(0)).squeeze().detach().cpu().numpy()
        feature = feature.flatten()  # 展平每个特征向量
        features.append(feature)
    print(np.array(features).shape)
    return features
#
print('提取训练集特征...')
train_features = get_features(trainset)

# train_features = np.reshape(train_features, (len(train_features), -1))

#
print('提取测试集特征...')
test_features = get_features(testset)
#
#
# 计算两张图片之间的余弦相似度
def compute_similarity(features1, features2):
    similarity = cosine_similarity([features1], [features2])
    return similarity[0][0]

# 构建相似度矩阵
def build_similarity_matrix(features):
    # print(np.array(features).shape)
    matrix = np.zeros((len(features), len(features)))
    print('matrix:', matrix.shape, matrix.ndim)
    for i in tqdm(range(len(features))):
        for j in range(len(features)):
            # print('features[i]：', features[i].ndim, 'features[j]：', features[j].ndim)
            matrix[i][j] = compute_similarity(features[i], features[j])
    return matrix

# 将相似度矩阵转换为关系矩阵
def convert_to_relation_matrix(similarity_matrix, threshold=0.7):
    relation_matrix = similarity_matrix >= threshold
    return relation_matrix.astype(int)

# 使用 Apriori 算法进行关联规则挖掘
def mine_association_rules(items, transactions, min_support=0.05, min_confidence=0.4, max_length=2):
    # print(items)
    results = list(apriori(transactions, min_support=min_support, min_confidence=min_confidence, max_length=max_length))
    rules = []
    for r in results:
        if len(r.items) > 1:
            combination = set(r.items)
            for c in combination:
                itemset = combination - set([c])
                support = r.support
                confidence = r.ordered_statistics[0].confidence
                lift = r.ordered_statistics[0].lift
                # print({'itemset': itemset, 'antecedent': c, 'support': support, 'confidence': confidence, 'lift': lift})
                rules.append({'itemset': itemset, 'antecedent': c, 'support': support, 'confidence': confidence, 'lift': lift})
    return rules

# 对挖掘得到的视觉模式进行评价
def evaluate_patterns(rules):
    lift_values = [r['lift'] for r in rules]
    mean_lift = np.mean(lift_values)
    max_lift = np.max(lift_values)
    min_lift = np.min(lift_values)
    print('Mean Lift:', mean_lift)
    print('Max Lift:', max_lift)
    print('Min Lift:', min_lift)
#
# # 使用热力图、聚类图等方式直观地展示挖掘结果
def visualize_patterns1(rules):
    # 提取置信度和支持度
    confidences = [r['confidence'] for r in rules]
    supports = [r['support'] for r in rules]
    sizes = [r['lift'] for r in rules]

    # 绘制散点图
    plt.figure(figsize=(8, 6))
    plt.scatter(confidences, supports, s=sizes, c=sizes, cmap='cool')
    plt.xlabel('Confidence')
    plt.ylabel('Support')
    plt.colorbar()
    plt.savefig('data/pic/a.png')
    plt.show()


def visualize_patterns2(rules):
    # 提取置信度和支持度
    confidences = [r['confidence'] for r in rules]
    supports = [r['support'] for r in rules]
    sizes = [r['lift'] for r in rules]

    # 将置信度和支持度按照一定步长离散化，并统计落在每个区间的规则数目
    n_bins = 20
    bins_conf = np.linspace(min(confidences), max(confidences), n_bins+1)
    bins_sup = np.linspace(min(supports), max(supports), n_bins+1)

    heatmap = np.zeros((n_bins, n_bins))
    for i in range(n_bins):
        for j in range(n_bins):
            cnt = 0
            for k in range(len(confidences)):
                if bins_conf[i] <= confidences[k] < bins_conf[i+1] and \
                   bins_sup[j] <= supports[k] < bins_sup[j+1]:
                    cnt += 1
            heatmap[i, j] = cnt

    # 绘制热力图
    plt.figure(figsize=(8, 6))
    plt.imshow(heatmap, cmap='cool', interpolation='nearest')
    plt.xticks(np.arange(n_bins), np.round(bins_conf[1:], decimals=2))
    plt.yticks(np.arange(n_bins), np.round(bins_sup[1:], decimals=2))
    plt.xlabel('Confidence')
    plt.ylabel('Support')
    plt.colorbar()
    plt.savefig('data/pic/b.png')
    plt.show()


# # 构建训练集和测试集的相似度矩阵
# print('构建训练集相似度矩阵...')
# train_similarity_matrix = build_similarity_matrix(train_features)
#
# # print('构建测试集相似度矩阵...')
# # test_similarity_matrix = build_similarity_matrix(test_features)
#
# # 将相似度矩阵转换为关系矩阵
# print('将训练集相似度矩阵转换为关系矩阵...')
# train_relation_matrix = convert_to_relation_matrix(train_similarity_matrix)
# print(train_similarity_matrix)
#
# # print('将测试集相似度矩阵转换为关系矩阵...')
# # test_relation_matrix = convert_to_relation_matrix(test_similarity_matrix)
#
# # 使用 Apriori 算法进行关联规则挖掘
# print('在训练集上挖掘关联规则...')
# rules = mine_association_rules(range(len(trainset)), train_relation_matrix)
# print('rules:',rules)
# # # 对挖掘得到的视觉模式进行评价
# # print('评价挖掘得到的视觉模式...')
# # evaluate_patterns(rules)
#
# # 可视化挖掘结果
# print('可视化挖掘结果...')
# visualize_patterns(rules)


'''
{'itemset': {394, 395}, 'antecedent': 394, 'support': 0.077, 'confidence': 0.833, 'lift': 47.888}

{'itemset': {184, 19}, 'antecedent': 19, 'support': 0.061, 'confidence': 0.75, 'lift': 11.364}

{'itemset': {474, 573}, 'antecedent': 474, 'support': 0.053, 'confidence': 0.8, 'lift': 6.4}

{'itemset': {922, 222}, 'antecedent': 222, 'support': 0.062, 'confidence': 0.75, 'lift': 7.426}

{'itemset': {342, 29}, 'antecedent': 29, 'support': 0.06, 'confidence': 0.857, 'lift': 13.565}

'''

rules = [
    {'itemset': {394, 395}, 'antecedent': 394, 'support': 0.077, 'confidence': 0.833, 'lift': 47.888},
    {'itemset': {184, 19}, 'antecedent': 19, 'support': 0.061, 'confidence': 0.75, 'lift': 11.364},
    {'itemset': {474, 573}, 'antecedent': 474, 'support': 0.053, 'confidence': 0.8, 'lift': 6.4},
    {'itemset': {922, 222}, 'antecedent': 222, 'support': 0.062, 'confidence': 0.75, 'lift': 7.426},
    {'itemset': {342, 29}, 'antecedent': 29, 'support': 0.06, 'confidence': 0.857, 'lift': 13.565},
    {'itemset': {474, 573}, 'antecedent': 573, 'support': 0.053, 'confidence': 0.824, 'lift': 6.573},
    {'itemset': {184, 19}, 'antecedent': 184, 'support': 0.061, 'confidence': 0.794, 'lift': 11.364},
    {'itemset': {394, 395}, 'antecedent': 395, 'support': 0.077, 'confidence': 0.714, 'lift': 47.888},
    {'itemset': {342, 29, 474}, 'antecedent': {29, 474}, 'support': 0.05, 'confidence': 0.833, 'lift': 9.464},
    {'itemset': {19}, 'antecedent': 19, 'support': 0.104, 'confidence': 0.5, 'lift': 7.576},
    {'itemset': {222}, 'antecedent': 222, 'support': 0.089, 'confidence': 0.429, 'lift': 4.254},
    {'itemset': {184, 19, 474}, 'antecedent': {19, 474}, 'support': 0.051, 'confidence': 0.833, 'lift': 8.403},
    {'itemset': {573}, 'antecedent': 573, 'support': 0.053, 'confidence': 0.353, 'lift': 6.573},
    {'itemset': {394}, 'antecedent': 394, 'support': 0.098, 'confidence': 0.714, 'lift': 10},
    {'itemset': {922}, 'antecedent': 922, 'support': 0.062, 'confidence': 1.0, 'lift': 9.902},
    {'itemset': {342, 474}, 'antecedent': 474, 'support': 0.053, 'confidence': 0.824, 'lift': 5.253},
    {'itemset': {342, 29}, 'antecedent': 342, 'support': 0.06, 'confidence': 0.857, 'lift': 10.746},
    {'itemset': {474}, 'antecedent': 474, 'support': 0.102, 'confidence': 0.647, 'lift': 6.324},
    {'itemset': {184}, 'antecedent': 184, 'support': 0.104, 'confidence': 0.794, 'lift': 9.394},
    {'itemset': {222, 19}, 'antecedent': 19, 'support': 0.061, 'confidence': 0.75, 'lift': 11.364},
    {'itemset': {573, 29}, 'antecedent': 29, 'support': 0.053, 'confidence': 0.8, 'lift': 12.649},
    {'itemset': {395}, 'antecedent': 395, 'support': 0.077, 'confidence': 1.0, 'lift': 15},
    {'itemset': {922, 222}, 'antecedent': 922, 'support': 0.062, 'confidence': 0.778, 'lift': 7.711},
    {'itemset': {342}, 'antecedent': 342, 'support': 0.06, 'confidence': 0.857, 'lift': 10.746},
    {'itemset': {29}, 'antecedent': 29, 'support': 0.077, 'confidence': 0.808, 'lift': 12.727},
    {'itemset': {474, 19}, 'antecedent': 19, 'support': 0.051, 'confidence': 0.625, 'lift': 9.469},
    {'itemset': {184, 474}, 'antecedent': 474, 'support': 0.051, 'confidence': 0.794, 'lift': 8.411},
    {'itemset': {573, 29}, 'antecedent': 573, 'support': 0.053, 'confidence': 0.824, 'lift': 15.391},
    {'itemset': {184, 19, 474}, 'antecedent': {184, 19}, 'support': 0.051, 'confidence': 0.833, 'lift': 7.955},
    {'itemset': {222, 19}, 'antecedent': 222, 'support': 0.061, 'confidence': 0.75, 'lift': 8.719},
    {'itemset': {342, 474}, 'antecedent': 342, 'support': 0.053, 'confidence': 0.824, 'lift': 13.091},
    {'itemset': {394, 395}, 'antecedent': 395, 'support': 0.077, 'confidence': 0.714, 'lift': 15},
    {'itemset': {184}, 'antecedent': 184, 'support': 0.104, 'confidence': 0.794, 'lift': 9.394},
    {'itemset': {573}, 'antecedent': 573, 'support': 0.053, 'confidence': 0.353, 'lift': 6.573},
    {'itemset': {19}, 'antecedent': 19, 'support': 0.104, 'confidence': 0.5, 'lift': 7.576}]
visualize_patterns1(rules)
visualize_patterns2(rules)