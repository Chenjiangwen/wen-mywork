import streamlit as st
import torch
import torch.nn as nn
import torchvision.transforms.functional as TF
from PIL import Image
import torchvision.models as models

# 定义 CIFAR-10 数据集的类别名称
class_names = ['飞机', '汽车', '鸟', '猫', '鹿',
               '狗', '青蛙', '马', '船', '卡车']

# 载入预训练的 ResNet-18 模型
net = models.resnet18(pretrained=True)
num_ftrs = net.fc.in_features
net.fc = nn.Linear(num_ftrs, 10)
device = torch.device("cpu")

PATH = 'data/cifar_net.pth'

net.load_state_dict(torch.load(PATH))
net.eval()
net.to(device)

# 创建函数来预测输入图像的标签
def predict(images):
    predicted_labels = []
    for image in images:
        img = Image.open(image)
        img = TF.resize(img, (224, 224))
        img = TF.to_tensor(img)
        img = TF.normalize(img, mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        with torch.no_grad():
            img = img.unsqueeze(0)
            img = img.to(device)
            outputs = net(img)
            _, predicted = torch.max(outputs.data, 1)
            predicted_label = class_names[predicted[0]]
            predicted_labels.append(predicted_label)
    return predicted_labels


st.title("图像分类应用")
st.write("上传图片，我们将尝试预测它们的类别！")
num_images = st.select_slider('选择要上传的图片数量：', options=[1, 2, 3])

uploaded_files = st.file_uploader(f"选择 {num_images} 张图片...", accept_multiple_files=True)

if uploaded_files is not None:
    if len(uploaded_files) == num_images:
        try:
            predicted_labels = predict(uploaded_files)
            for i, img in enumerate(uploaded_files):
                st.image(img, caption=f"预测标签：{predicted_labels[i]}", use_column_width=True)
        except Exception as e:
            print(e)
            st.write("处理图像时出错。请重试。")
    else:
        st.write(f"请上传恰好 {num_images} 张图片。")
