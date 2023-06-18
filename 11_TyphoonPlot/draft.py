import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# 读取数据
df = pd.read_csv('Cb06.txt', delim_whitespace=True, header=None, names=['year', 'id', 'category', 'start_time', 'end_time', 'name'])
df['name'] = df['name'].astype(str)

# 按照类别分类，并计算每年的台风数量
tc_counts_by_category = {}
for category in range(1, 7):
    tc_counts_by_year = {}
    for _, row in df[df['category'] == category].iterrows():
        year = row['year']
        if year not in tc_counts_by_year:
            tc_counts_by_year[year] = 0
        tc_counts_by_year[year] += 1
    tc_counts_by_category[category] = tc_counts_by_year

# 绘制每个类别的趋势折线图，并计算趋势值和P值
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 12))
fig.suptitle('Typhoon Frequency Trend by Category', fontsize=20)

for idx, ax in enumerate(axes.flatten()):
    category = idx + 1
    tc_counts = sorted(tc_counts_by_category[category].items())
    time = np.array([x[0] for x in tc_counts])
    tc_frequency = np.array([x[1] for x in tc_counts])
    slope, intercept, r_value, p_value, std_err = stats.linregress(time, tc_frequency)
    ax.plot(time, tc_frequency, 'k-')
    ax.plot(time, intercept + slope * time, 'r-', label=f'slope={slope:.3f}, P={p_value:.3f}')
    ax.set_ylim([0, max(tc_frequency) * 1.2])
    ax.legend(loc='upper left')
    ax.set_title(f'C {category}')
    ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('out.jpg')
plt.show()
