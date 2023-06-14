import numpy as np
from matplotlib import pyplot as plt
import logging
import datetime

# 创建一个logger对象
logger = logging.getLogger('net')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于将日志信息输出到文件
file_handler = logging.FileHandler('data/' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log')
file_handler.setLevel(logging.INFO)

# 定义日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将handler添加到logger对象中
logger.addHandler(file_handler)
#
# Load CIFAR-10 dataset
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

dataset_path = 'data/cifar-10-batches-py'
train_data, train_labels = [], []
for i in range(1, 6):
    filename = dataset_path + '/data_batch_{}'.format(i)
    data_dict = unpickle(filename)
    train_data.append(data_dict[b'data'])
    train_labels += data_dict[b'labels']
train_data = np.concatenate(train_data, axis=0)
train_labels = np.array(train_labels)

test_data_dict = unpickle(dataset_path + '/test_batch')
test_data = test_data_dict[b'data']
test_labels = np.array(test_data_dict[b'labels'])

# Preprocess data
train_data = train_data.astype('float32') / 255.0
test_data = test_data.astype('float32') / 255.0
num_classes = 10
train_labels = np.eye(num_classes)[train_labels]

# Define hyperparameters
input_size = 3072 # 32x32x3
hidden_size = 100
output_size = num_classes
learning_rate = 0.1
batch_size = 100
epochs = 20

def train_network(learning_rate):
    # 定义 sigmoid 函数
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    # 定义交叉熵代价函数
    def cross_entropy_cost(y_pred, y_true):
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    # 定义随机梯度下降优化器
    def update_weights(weights, biases, dw, db, learning_rate):
        weights -= learning_rate * dw / batch_size
        biases -= learning_rate * db / batch_size
        return weights, biases

    # 初始化网络参数
    W1 = np.random.randn(hidden_size, input_size)
    b1 = np.zeros((hidden_size, 1))
    W2 = np.random.randn(output_size, hidden_size)
    b2 = np.zeros((output_size, 1))

    accuracy_list = []
    for epoch in range(epochs):
        for i in range(0, len(train_data), batch_size):
            # 获取一批数据和标签
            X = train_data[i:i+batch_size].T
            y = train_labels[i:i+batch_size].T

            # 前向传播
            Z1 = np.dot(W1, X) + b1
            A1 = sigmoid(Z1)
            Z2 = np.dot(W2, A1) + b2
            y_pred = sigmoid(Z2)

            # 反向传播
            dZ2 = y_pred - y
            dW2 = np.dot(dZ2, A1.T)
            db2 = np.sum(dZ2, axis=1, keepdims=True)
            dZ1 = np.dot(W2.T, dZ2) * (A1 * (1 - A1))
            dW1 = np.dot(dZ1, X.T)
            db1 = np.sum(dZ1, axis=1, keepdims=True)

            # 更新权重和偏置项
            W2, b2 = update_weights(W2, b2, dW2, db2, learning_rate)
            W1, b1 = update_weights(W1, b1, dW1, db1, learning_rate)

        # 在测试集上评估性能
        Z1 = np.dot(W1, test_data.T) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(W2, A1) + b2
        y_pred = np.argmax(sigmoid(Z2), axis=0)
        accuracy = 100 * np.mean(y_pred == test_labels)
        accuracy_list.append(accuracy)

        print('Epoch %d, Batch_Size %d, lr %f: Test Accuracy = %.2f%%' % (epoch+1, batch_size, learning_rate, accuracy))
        logger.info('Epoch %d, Batch_Size %d, lr %f: Test Accuracy = %.2f%%' % (epoch+1, batch_size, learning_rate, accuracy))

    return accuracy_list

logger.info('================================1、=============================================')

# 1. 在测试数据集上测试模型，并绘制测试准确率 vs epoch 的图像，并打印出最高准确率
accuracy_list = train_network(learning_rate=0.1)

plt.plot(accuracy_list)
plt.xlabel('Epochs')
plt.ylabel('Test Accuracy (%)')
plt.title('Accuracy Curve')

plt.savefig("data/pic/accuracy_3_1.png") # 保存图像

plt.show()

max_accuracy = max(accuracy_list)
print("Maximum accuracy achieved:", max_accuracy)
logger.info("Maximum accuracy achieved:%f", max_accuracy)

logger.info('================================2、=============================================')
# 2. 使用相同的设置训练新的神经网络，但使用不同的学习率（0.001、0.01、1.0、10、100），绘制每个学习率的测试准确率 vs epoch 的图像。每次创建一个新的神经网络，因此它从零开始学习。并打印出每种学习率所达到的最高准确率。
learning_rates = [0.001, 0.01, 1.0, 10, 100]
colors = ['r', 'g', 'b', 'm', 'k']

plt.figure()
for i, lr in enumerate(learning_rates):
    accuracy_list = train_network(learning_rate=lr)
    plt.plot(accuracy_list, color=colors[i], label=f'lr={lr}')

    max_accuracy = max(accuracy_list)
    print(f"Maximum accuracy (lr={lr}) achieved:", max_accuracy)
    logger.info(f"Maximum accuracy (lr=%f achieved:%f",lr, max_accuracy)

plt.xlabel('Epochs')
plt.ylabel('Test Accuracy (%)')
plt.title('Accuracy Curve (Different Learning Rates)')
plt.legend(loc='lower right')

plt.savefig("data/pic/accuracy_3_2.png") # 保存图像

plt.show()

logger.info('================================3、=============================================')
# 3. 使用与 (1.) 相同的设置训练新的神经网络，但使用不同的 mini-batch size（1、5、20、100、300），绘制最大测试准确率 vs mini-batch size 的图像。哪一个达到了最大测试准确率？哪一个最慢？
batch_sizes = [1, 5, 20, 100, 300]
max_accuracy_list = []
for batch_size in batch_sizes:
    accuracy_list = train_network(learning_rate=0.1)

    max_accuracy = max(accuracy_list)
    max_accuracy_list.append(max_accuracy)

    print(f"Maximum accuracy (batch_size={batch_size}) achieved:", max_accuracy)
    logger.info("Maximum accuracy (batch_size=%d) achieved:%s", batch_size, max_accuracy)

plt.plot(batch_sizes, max_accuracy_list, 'bo-')
plt.xlabel('Mini-batch Size')
plt.ylabel('Max Test Accuracy (%)')
plt.title('Max Test Accuracy Curve (Different Mini-batch Sizes)')

plt.savefig("data/pic/accuracy_3_3.png") # 保存图像

plt.show()

print("The maximum test accuracy is achieved at mini-batch size =", batch_sizes[np.argmax(max_accuracy_list)])
print("The slowest mini-batch size is", batch_sizes[np.argmin(max_accuracy_list)])

logger.info("The maximum test accuracy is achieved at mini-batch size = %d", batch_sizes[np.argmax(max_accuracy_list)])
logger.info("The slowest mini-batch size is %d", batch_sizes[np.argmin(max_accuracy_list)])

'''
下面代码实现了一个小型神经网络的训练。主要包括以下几个部分：

1. 初始化神经网络：使用initialize_network函数，输入网络的输入、隐藏层和输出的神经元数量，随机生成权重并返回整个神经网络。

2. 前向传播：使用forward_propagate函数，在每一层中计算每个神经元的输出，并将其作为下一层的输入。其中，激活函数采用sigmoid函数。

3. 后向传播：使用backward_propagate_error函数，计算每个神经元的误差，并将误差反向传递回输入层。其中，误差计算采用均方误差，并使用transfer_derivative函数计算梯度。

4. 权重更新：使用update_weights函数，根据误差调整权重。

5. 训练神经网络：使用train_network函数，循环多次对神经网络进行训练，并输出每次迭代后的误差和更新后的权重值。

6. 测试小型神经网络：使用test_small_network函数，对于一个简单的二分类问题，测试训练出来的神经网络在测试数据上的表现。

'''
logger.info('================================4、=============================================')
# 初始化
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights': [np.random.standard_normal() for i in range(n_inputs)] + [0, 0]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [np.random.standard_normal() for i in range(n_hidden)] + [0, 0]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


# 前向传播
def activate(weights, inputs):
    activation = weights[-2]
    for i in range(len(weights) - 2):
        activation += weights[i] * inputs[i]

    return activation


def sigmoid(activation):
    return 1.0 / (1.0 + np.exp(-activation))


def forward_propagate(network, row):
    inputs = row[:-1]
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = sigmoid(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# 后向传播
def transfer_derivative(output):
    return output * (1.0 - output)


def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i == len(network) - 1:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        else:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])


# 权重更新
def update_weights(network, row, learning_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += learning_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-2] += learning_rate * neuron['delta'] * 1.0
            neuron['weights'][-1] += learning_rate * neuron['delta'] * neuron['output']


# 训练神经网络
def train_network(network, train, learning_rate, n_epochs, n_outputs):
    for epoch in range(n_epochs):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, learning_rate)
        print('epoch=%d, learning_rate=%.3f, error=%.3f' % (epoch + 1, learning_rate, sum_error))
        logger.info('epoch=%d, learning_rate=%.3f, error=%.3f' % (epoch + 1, learning_rate, sum_error))

        # 打印更新后的权重
        print("======== Updated Weights: Epoch {} ===============".format(epoch + 1))
        logger.info("======== Updated Weights: Epoch {} ===============".format(epoch + 1))
        weight_list = []
        for layer in network:
            for neuron in layer:
                weight_list.extend(neuron['weights'])
        for i in range(0, len(weight_list), 2):
            if (i + 2) <= len(weight_list):
                print("w{}: {:.15f}\tw{}: {:.15f}".format(i + 1, weight_list[i], i + 2, weight_list[i + 1]))
                logger.info("w{}: {:.15f}\tw{}: {:.15f}".format(i + 1, weight_list[i], i + 2, weight_list[i + 1]))


# 测试小型神经网络
def test_small_network():
    dataset = [[0.1, 0.1, 0], [0.1, 0.2, 1]]
    learning_rate = 0.1
    n_epochs = 1
    n_inputs = 2
    n_outputs = 2
    n_hidden = 2
    network = initialize_network(n_inputs, n_hidden, n_outputs)
    train_network(network, dataset, learning_rate, n_epochs, n_outputs)

test_small_network()