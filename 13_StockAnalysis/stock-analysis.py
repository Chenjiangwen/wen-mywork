#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd  # 数据处理，CSV文件输入输出等
import matplotlib.pyplot as plt  # 可视化

# In[4]:

data = pd.read_csv("resource/TSLA.csv")  # 读取数据

data["Date"] = pd.to_datetime(data["Date"])  # 将日期转换为 pandas 的日期类型

years = []  # 用来保存年份
months = []  # 用来保存月份
for index, row in data.iterrows():
    years.append(row.Date.year)  # 获取年份并添加到保存年份的列表中
    months.append(row.Date.month)  # 获取月份并添加到保存月份的列表中

data["Year"] = years  # 添加年份列
data["Month"] = months  # 添加月份列
print()
print(data)  # 展示数据
print()
# In[5]:
print()
print(data.describe())  # 描述数据
print()
# In[6]:
date_unique = data["Date"].unique()  # 获取日期列中的唯一值
high_unique = data["High"].unique()  # 获取最高价列中的唯一值
low_unique = data["Low"].unique()  # 获取最低价列中的唯一值
open_unique = data["Open"].unique()  # 获取开盘价列中的唯一值
close_unique = data["Close"].unique()  # 获取收盘价列中的唯一值
volume_unique = data["Volume"].unique()  # 获取成交量列中的唯一值
adj_unique = data["Adj Close"].unique()  # 获取调整后收盘价列中的唯一值

# In[7]:
grouped = data.groupby(["Year", "Month"])  # 将数据按年份和月份进行分组
group_mean = grouped[["High", "Low", "Open", "Close"]].mean()  # 获取高、低、开、收四种数据的平均值
print(group_mean)

# In[8]:
plot_data = data.set_index("Date")  # 将日期设置为索引
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Stock Prices for Tesla", fontsize=24)  # 设置标题
plt.plot(plot_data["High"])  # 绘制最高价曲线
plt.plot(plot_data["Low"])  # 绘制最低价曲线
plt.plot(plot_data["Open"])  # 绘制开盘价曲线
plt.plot(plot_data["Close"])  # 绘制收盘价曲线
plt.legend(["High", "Low", "Open", "Close"])  # 添加图例
plt.savefig('resource/Stock_Prices_for_Tesla.jpg')  # 将图片保存为 jpg 格式

# In[9]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Stock Volume", fontsize=24)  # 设置标题
plt.plot(plot_data["Volume"])  # 绘制成交量曲线
plt.legend(["Volume"])  # 添加图例
plt.savefig('resource/Stock_Volume.jpg')  # 将图片保存为 jpg 格式

# In[10]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("High vs. Low", fontsize=24)  # 设置标题
plt.plot(plot_data["High"])  # 绘制最高价曲线
plt.plot(plot_data["Low"])  # 绘制最低价曲线
plt.legend(["High", "Low"])  # 添加图例
plt.savefig('resource/High_vs_Low.jpg')  # 将图片保存为 jpg 格式

# In[11]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Open vs. Close", fontsize=24)  # 设置标题
plt.plot(plot_data["Open"])  # 绘制开盘价曲线
plt.plot(plot_data["Close"])  # 绘制收盘价曲线
plt.legend(["Open", "Close"])  # 添加图例
plt.savefig('resource/Open_vs_Close.jpg')  # 将图片保存为 jpg 格式

# In[12]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Close vs Adjusted Close", fontsize=24)  # 设置标题
plt.plot(plot_data["Close"])  # 绘制收盘价曲线
plt.plot(plot_data["Adj Close"])  # 绘制调整后收盘价曲线
plt.legend(["Close", "Adjusted Close"])  # 添加图例
plt.savefig('resource/Close_vs_Adjusted_Close.jpg')  # 将图片保存为 jpg 格式

# In[13]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Open vs. High vs. Close", fontsize=24)  # 设置标题
plt.plot(plot_data["Open"])  # 绘制开盘价曲线
plt.plot(plot_data["High"])  # 绘制最高价曲线
plt.plot(plot_data["Close"])  # 绘制收盘价曲线
plt.legend(["Open", "High", "Close"])  # 添加图例
plt.savefig('resource/Open_vs_High_vs_Close.jpg')  # 将图片保存为 jpg 格式

# In[14]:
plt.figure(figsize=(32, 16))  # 指定图片大小
plt.title("Open vs. Low vs. Close", fontsize=24)  # 设置标题
plt.plot(plot_data["Open"])  # 绘制开盘价曲线
plt.plot(plot_data["Low"])  # 绘制最低价曲线
plt.plot(plot_data["Close"])  # 绘制收盘价曲线
plt.legend(["Open", "Low", "Close"])  # 添加图例
plt.savefig('resource/Open_vs_Low_vs_Close.jpg')  # 将图片保存为 jpg 格式