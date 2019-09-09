import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = range(21, 26)
y = [[10, 4, 6, 5, 3], [12, 2, 7, 10, 1], [8, 18, 5, 7, 6], [1, 8, 3, 5, 9]]
labels = ['组A', '组B', '组C', '组D']
pal = sns.color_palette("Set1")
plt.stackplot(x, y, labels=labels, colors=pal, alpha=0.7)
plt.ylabel('分值')
plt.xlabel('年龄')
plt.title('不同组用户区间分值比较')
plt.legend(loc='upper right')
plt.show()

# -------
# HeatMap

import pandas as pd
import numpy as np

people = np.repeat(("组1", "组2", "组3", "组4", "组5"), 6)
# feature=('周一','周二','周三','周四','周五','周六')*5
feature = ('1', '2', '3', '4', '5', '6') * 5
value = np.random.random(30)
df = pd.DataFrame({'工作日': feature, '团队': people, 'value': value})
print(df)
df_wide = df.pivot_table(index='团队', columns='工作日', values='value')
print(df_wide.head())
p2 = sns.heatmap(df_wide).set_title("各小组工作日表现比较")
plt.show()
