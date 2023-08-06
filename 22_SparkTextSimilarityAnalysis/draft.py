# # def extract_lines(input_file, output_file, num_lines):
# #     with open(input_file, 'r', encoding='utf-8') as f_input:
# #         lines = f_input.readlines()[:num_lines]
# #
# #     with open(output_file, 'w', encoding='utf-8') as f_output:
# #         f_output.writelines(lines)
# #
# # input_file = './abcnews-date-text.txt'  # 输入文件路径
# # output_file = 'abcnews-9w-text.txt'  # 输出文件路径
# # num_lines = 90000  # 需要提取的行数
#
# # extract_lines(input_file, output_file, num_lines)
#
# # import time
# #
# # def format_time(seconds):
# #     # Convert seconds to hours, minutes, and seconds
# #     hours = int(seconds // 3600)
# #     minutes = int((seconds % 3600) // 60)
# #     remaining_seconds = int(seconds % 60)
# #
# #     return "{} hours {} minutes {} seconds".format(hours, minutes, remaining_seconds)
# #
# # start_time = time.time()
# # print("开始执行...")
# # # 暂停3秒
# # # time.sleep(3)
# # read_time = time.time() - start_time
# # print("Finished extracting title and date information, time elapsed: {}".format(format_time(read_time)))
# #
# # start_time = time.time()
# # print("开始执行...")
# # # 暂停3秒
# # # time.sleep(10)
# # print("继续执行...")
# # aa = time.time() - start_time
# # print("Finished extracting title and date information, time elapsed: {}".format(format_time(aa)))
#
#
# # 读取原始文件并加载数据到内存中
# # def sort_deduplication(file_path):
# #     # f = file_path + '/part-00000'
# #     f = 'a'
# #     data = []
# #     with open(f, 'r') as file:
# #         for line in file:
# #             parts = line.strip().split('\t')
# #             key1, key2 = eval(parts[0])
# #             value = float(parts[1])
# #             data.append(((key1, key2), value))
# #
# #     # 使用集合去重
# #     unique_data = list(set(data))
# #
# #     # 对数据进行排序
# #     sorted_data = sorted(unique_data)
# #
# #     # 将排序后的结果写入原始文件中
# #     with open(f, 'w') as file:
# #         for item in sorted_data:
# #             line = "({}, {})\t{}\n".format(item[0][0], item[0][1], item[1])
# #             file.write(line)
# # a = 1
# # sort_deduplication(a)
#
# #################### 找出不同的元素 ###########
# def find_extra_data(file_a, file_b):
#     with open(file_a, 'r') as file_a:
#         content_a = set(file_a.readlines())
#
#     with open(file_b, 'r') as file_b:
#         content_b = set(file_b.readlines())
#
#     extra_data = content_b - content_a
#
#     for data in extra_data:
#         print(data.strip())
#
# # 示例用法
# file_a_path = 'project3_out-25w_part-00000 (2)'
# file_b_path = 'out/project3_out-25w_part-00000 (1)'
#
# find_extra_data(file_a_path, file_b_path)


##################### 读取指定行的内容 ##############

# def read_lines_from_file(file_path, line_numbers):
#     lines = []
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line_number, line in enumerate(file):
#             if line_number in line_numbers:
#                 lines.append(line.strip())
#     return lines
#
# line_numbers = [52854,93798]
# file_path = 'data/abcnews-date-text.txt'  # 修改为实际的文件路径
# lines = read_lines_from_file(file_path, line_numbers)
# print(lines)

################# 分析标题长度 #################
import matplotlib.pyplot as plt


# def count_titles_by_length(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     title_counts = {}
#
#     for line in lines:
#         _, title = line.strip().split(',', 1)  # 将每行数据按逗号分割，获取标题部分
#         words = title.split()  # 使用默认分隔符将标题拆分为单词列表
#
#         word_count = len(words)  # 计算单词数
#
#         if word_count not in title_counts:
#             title_counts[word_count] = 0
#
#         title_counts[word_count] += 1
#
#     return title_counts
#
#
# filename = 'abcnews-date-text.txt'
# title_counts = count_titles_by_length(filename)
#
# # 按长度对标题数量进行排序
# sorted_counts = sorted(title_counts.items(), key=lambda x: x[0])
#
# # 提取长度和数量信息
# lengths = [count[0] for count in sorted_counts]
# counts = [count[1] for count in sorted_counts]
#
# # 打印标题长度及其对应的数量
# for length, count in zip(lengths, counts):
#     print("标题长度为", length, "的数量：", count)
#
# # 绘制柱状图
# plt. bar(lengths, counts)
# plt.xlabel('title length')
# plt.ylabel('quantity')
# plt.title('title length and quantity relationship')
# plt. show()

import matplotlib.pyplot as plt

# 数据
workers = ['2workers', '3workers']
time = [28*60+42, 20*60+17]  # 将时间转换为秒

# 转换时间为分秒形式
time = [divmod(t, 60) for t in time]

# 提取分钟和秒的值
minutes = [t[0] for t in time]
seconds = [t[1] for t in time]

# 绘制柱状图
plt.bar(workers, minutes, width=0.5)

# 添加柱子上的数值标签
for i in range(len(workers)):
    plt.text(workers[i], minutes[i] + seconds[i]/60 + 0.5, '{:02d}min{:02d}sec'.format(minutes[i], seconds[i]), ha='center')

# 设置坐标轴标签
plt.xlabel('Number of Workers')
plt.ylabel('Time (minutes:seconds)')

# 设置标题
plt.title('Execution Time vs Number of Workers')

# 调整边界框高度
plt.ylim(0, max(minutes) + 7)

# 显示图形
plt.savefig('out/Runtime.jpg')

