# 1. Here is the code to create and train a neural network with size [3072, 30, 10] on the CIFAR-10 dataset using PyTorch:
#
#
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
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

logger.info('================================1、=============================================')

# Check if GPU is available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))


# Define the neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3072, 30)
        self.fc2 = nn.Linear(30, 10)

    def forward(self, x):
        x = x.view(-1, 3072)  # Flatten the input tensor
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Load the CIFAR-10 dataset and apply data augmentation
transform = transforms.Compose(
    [transforms.RandomHorizontalFlip(),
     transforms.RandomCrop(32, padding=4),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=4)

testset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=4)

# Move the model to the GPU
# net = Net().to(device)
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.SGD(net.parameters(), lr=0.1)
#
# accuracy_list = []
# for epoch in range(20):
#     running_loss = 0.0
#     for i, data in enumerate(trainloader, 0):
#         inputs, labels = data
#         # Move the tensor to the GPU
#         inputs, labels = inputs.to(device), labels.to(device)
#
#         optimizer.zero_grad()
#         outputs = net(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()
#
#         running_loss += loss.item()
#         if i % 200 == 199:
#             print('part_1 [epoch:%d, %5d] loss: %.3f' %
#                   (epoch + 1, i + 1, running_loss / 200))
#             running_loss = 0.0
#
#     # Test the network
#     correct = 0
#     total = 0
#     with torch.no_grad():
#         for data in testloader:
#             images, labels = data
#             images, labels = images.to(device), labels.to(device)
#             outputs = net(images)
#             _, predicted = torch.max(outputs.data, 1)
#             total += labels.size(0)
#             correct += (predicted == labels).sum().item()
#
#     accuracy = 100 * correct / total
#     accuracy_list.append(accuracy)
#     print('LR = 0.1,batch_size = 4, Accuracy of the network on the %d test images: %d %%' % (total, accuracy))
#     logger.info('LR = 0.1,batch_size = 4, Accuracy of the network on the %d test images: %d %%' % (total, accuracy))
#
# # Plot the accuracy vs epoch graph
# plt.plot(range(1, 21), accuracy_list)
# plt.xlabel('Epoch')
# plt.ylabel('Test accuracy (%)')
# plt.title('Test accuracy vs epoch')
# plt.savefig('data/pic/accuracy_vs_epoch.png')
# plt.show()
#
# # Print the maximum accuracy achieved
# print('Maximum accuracy achieved: %d %%' % max(accuracy_list))
# logger.info('LR = 0.1,batch_size = 4, Maximum accuracy achieved: %d %%' % max(accuracy_list))
# #
# # 2. Here is the code to train a new neural network with different learning rates and plot the test accuracy vs epoch graph for each:
# # 学习率过高、损失迅速增长到非常大的值，可能会超出浮点数的范围。而在后面的训练中，损失呈现为 NaN 的状态，这说明模型已经崩溃，并无法进行下去
# # ```

# logger.info('================================2、=============================================')
# learning_rates = [0.001, 0.01, 1.0, 10.0, 100.0]
# accuracy_lists = []
#
# for lr in learning_rates:
#     # Create a new neural network
#     net = Net().to(device)
#     criterion = nn.CrossEntropyLoss()
#     optimizer = optim.SGD(net.parameters(), lr=lr)
#
#     # Train the neural network
#     accuracy_list = []
#     for epoch in range(20):
#         running_loss = 0.0
#         for i, data in enumerate(trainloader, 0):
#             inputs, labels = data
#             inputs, labels = inputs.to(device), labels.to(device)
#             optimizer.zero_grad()
#             outputs = net(inputs)
#             loss = criterion(outputs, labels)
#             loss.backward()
#             optimizer.step()
#
#             running_loss += loss.item()
#             if i % 200 == 199:
#                 print('part_2 [lr=%.3f,epoch:%d, %5d] loss: %.3f' %
#                       (lr, epoch + 1, i + 1, running_loss / 200))
#                 running_loss = 0.0
#
#         # Test the network
#         correct = 0
#         total = 0
#         with torch.no_grad():
#             for data in testloader:
#                 images, labels = data
#                 images, labels = images.to(device), labels.to(device)
#                 outputs = net(images)
#                 _, predicted = torch.max(outputs.data, 1)
#                 total += labels.size(0)
#                 correct += (predicted == labels).sum().item()
#
#         accuracy = 100 * correct / total
#         accuracy_list.append(accuracy)
#         print('LR = ' + str(lr) + ' Accuracy of the network on the %d test images: %d %%' % (total, accuracy))
#         logger.info('LR = ' + str(lr) + ' Accuracy of the network on the %d test images: %d %%' % (total, accuracy))
#
#     accuracy_lists.append(accuracy_list)
#
# # Plot the accuracy vs epoch graph for each learning rate
# for i, lr in enumerate(learning_rates):
#     plt.plot(range(1, 21), accuracy_lists[i], label='LR = ' + str(lr))
#     plt.legend()
#     plt.xlabel('Epoch')
#     plt.ylabel('Test accuracy (%)')
#     plt.title('Test accuracy vs epoch for different learning rates')
#     plt.savefig('data/pic/accuracy_vs_epoch_lr=' + str(lr) + '.png')
#     # plt.show()
#
# # Print the maximum accuracy achieved for each learning rate
# for i, lr in enumerate(learning_rates):
#     print('Maximum accuracy achieved with LR = %.3f: %d %%' % (lr, max(accuracy_lists[i])))
#     logger.info('Maximum accuracy achieved with LR = %.3f: %d %%' % (lr, max(accuracy_lists[i])))
# ```
#
# 3. Here is the code to train new neural networks with different mini-batch sizes and plot the maximum test accuracy vs mini-batch size:
#
# ```
logger.info('================================3、=============================================')
batch_sizes = [1, 5, 20, 100, 300]
accuracy_lists = []

for batch_size in batch_sizes:
    accuracy_list = []  # The definition of accuracy_list has been moved inside the for loop, ensuring a new, empty list is used every loop.

    # Create a new neural network
    net = Net().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001)

    # Train the neural network
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=4)

    for epoch in range(20):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 200 == 199:
                print('part_3 [batch_size: %d epoch: %d, %5d] loss: %.3f' %
                      (batch_size, epoch + 1, i + 1, running_loss / 200))
                running_loss = 0.0


    # Test the network
    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    accuracy_list.append(accuracy)
    accuracy_lists.append(accuracy_list)  #将accuracy_list添加到accuracy_lists中

    print('Batch Size = ' + str(batch_size) + ' Accuracy of the network with batch size %d: %d %%' % (batch_size, accuracy))
    logger.info('Batch Size = ' + str(batch_size) + ' Accuracy of the network with batch size %d: %d %%' % (batch_size, accuracy))


# Plot the maximum test accuracy vs mini-batch size
max_accuracy = max([max(l) for l in accuracy_lists])
max_batch_size = batch_sizes [[max(l) for l in accuracy_lists].index(max_accuracy)]
print(f"Maximum test accuracy: {max_accuracy:.4f} achieved with mini-batch size of {max_batch_size}.")
logger.info(f"Maximum test accuracy: {max_accuracy:.4f} achieved with mini-batch size of {max_batch_size}.")


# 在循环完成后，使用绘图库的功能将所有数据绘制到一个图形中。
# Note that this is only one way to plot the data; other methods are possible.
plt.figure(figsize=(10, 5))
for i in range(len(accuracy_lists)):
    if len(accuracy_lists[i]) > 0:
        plt.plot(range(1, len(accuracy_lists[i])+1), accuracy_lists[i], label='Batch Size = ' + str(batch_sizes[i]))
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.legend()
plt.savefig('data/pic/accuracy_vs_epoch_Batch_Size.png')
plt.show()



