import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

np.random.seed(42)
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)
print(spread, center, flier_high, flier_low)
fig7, ax7 = plt.subplots()
ax7.set_title('小组分值分布情况')
ax7.boxplot(data, labels=['组1'])
plt.show()
