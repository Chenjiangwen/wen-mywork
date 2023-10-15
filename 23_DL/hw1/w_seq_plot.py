"""
   seq_plot.py
   COMP9444, CSE, UNSW
"""

import argparse
import sys
import torch
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import matplotlib.lines as mlines
from seq_models import SRN_model, LSTM_model
from anb2n import lang_anb2n

parser = argparse.ArgumentParser()
parser.add_argument('--lang', type=str, default='anb2n', help='anb2n or anb2nc3n')
parser.add_argument('--length', type=int, default=0, help='max number of As')
# network options
parser.add_argument('--model', type=str, default='srn', help='srn or lstm')
parser.add_argument('--hid', type=int, default=0, help='number of hidden units')
# visualization options
parser.add_argument('--epoch', type=int, default=100, help='epoch to load from')
parser.add_argument('--num_plot', type=int, default=10, help='number of plots')
args = parser.parse_args()

if args.lang == 'anb2n':
    num_class = 2
    hid_default = 2
    epoch_default = 100
elif args.lang == 'anb2nc3n':
    num_class = 3
    if args.model == 'lstm':
        hid_default = 3
        epoch_default = 100
    else:  # srn
        hid_default = 4
        epoch_default = 200

if args.length == 0:
    args.length = 4
lang = lang_anb2n(num_class, args.length)
max_state = args.length

if args.hid == 0:
    args.hid = hid_default

if args.model == 'srn':
    net = SRN_model(num_class, args.hid, num_class)
elif args.model == 'lstm':
    net = LSTM_model(num_class, args.hid, num_class)

path = './net/'
net.load_state_dict(torch.load(path + '%s_%s%d_%d.pth'
                               % (args.lang, args.model, args.hid, args.epoch)))

np.set_printoptions(suppress=True, precision=2)

for weight in net.parameters():
    print(weight.data.numpy())

with torch.no_grad():
    net.eval()

    all_hid = []
    all_state = []
    for epoch in range(args.num_plot):
        input, seq, target, state = lang.get_sequence()
        label = seq[1:]

        net.init_hidden()
        hidden_seq, output = net(input)

        hidden = hidden_seq.squeeze()

        all_hid.append(hidden)
        all_state = all_state + state[1:]

        lang.print_outputs(epoch, seq, state, hidden, target, output)
        sys.stdout.flush()

    all_hidden = torch.cat(all_hid, dim=0)
    for k in range(args.hid):
        for j in range(k):
            fig, ax = plt.subplots()

            # 绘制散点图
            sc = ax.scatter(all_hidden[:, j], all_hidden[:, k], c=all_state,
                            cmap='jet', vmin=0, vmax=max_state)

            # 绘制边界
            for i in range(max_state):
                indices = np.where(all_state == i)[0]
                if len(indices) > 0:
                    min_j, max_j = np.min(all_hidden[indices, j]), np.max(all_hidden[indices, j])
                    min_k, max_k = np.min(all_hidden[indices, k]), np.max(all_hidden[indices, k])
                    rect = patches.Rectangle((min_j, min_k), max_j - min_j, max_k - min_k,
                                             linewidth=1, edgecolor='black', facecolor='none')
                    ax.add_patch(rect)

            # 绘制箭头
            for i in range(len(all_state) - 1):
                if all_state[i] != all_state[i + 1]:
                    arrow = mlines.Line2D([all_hidden[i, j], all_hidden[i + 1, j]],
                                          [all_hidden[i, k], all_hidden[i + 1, k]],
                                          linestyle='dashed', alpha=0.6, color='black')
                    arrow_head = patches.FancyArrowPatch((all_hidden[i + 1, j], all_hidden[i + 1, k]),
                                                         (all_hidden[i, j], all_hidden[i, k]), arrowstyle='->',
                                                         alpha=0.6, color='black')
                    ax.add_line(arrow)
                    ax.add_patch(arrow_head)

            # 绘制初始状态的十字标记
            # initial_state = np.where(all_state == 0)[0][0]
            # ax.plot(all_hidden[initial_state, j], all_hidden[initial_state, k], 'kx')

            fig.colorbar(sc)
            plt.savefig('./plot/www_%s_%s%d_%d%d.jpg' % (args.lang, args.model, args.hid, j, k))
            plt.show()

    import numpy as np

    unique_states = np.unique(all_state)
    num_states = len(unique_states)

    state_counts = []
    for state in unique_states:
        state_idxs = np.where(all_state == state)[0]
        state_count = len(state_idxs)
        state_counts.append(state_count)

    print("不同状态的数量:", num_states)
    print("每个状态对应的数据点数目:", state_counts)

    import matplotlib.pyplot as plt
    import numpy as np

    # 绘制散点图和颜色映射
    scatter = plt.scatter(all_hidden[:, 0], all_hidden[:, 1], c=all_state, cmap='jet', vmin=0, vmax=max_state)

    # 创建图例标签
    unique_states = np.unique(all_state)
    num_states = len(unique_states)
    state_counts = [len(np.where(all_state == state)[0]) for state in unique_states]
    legend_labels = [f'State {state} ({count})' for state, count in zip(unique_states, state_counts)]

    # 添加图例
    plt.legend(handles=scatter.legend_elements()[0], labels=legend_labels)

    # 显示图像
    plt.show()

    if args.hid >= 3:
        fig = plt.figure()
        ax = Axes3D(fig)

        # 绘制散点图
        sc = ax.scatter(all_hidden[:, 0], all_hidden[:, 1], all_hidden[:, 2],
                        c=all_state, cmap='jet', vmin=0, vmax=max_state)

        # 绘制初始状态的十字标记
        initial_state = np.where(all_state == 0)[0][0]
        ax.plot([all_hidden[initial_state, 0]], [all_hidden[initial_state, 1]], [all_hidden[initial_state, 2]], 'kx')

        fig.colorbar(sc)
        plt.show()
