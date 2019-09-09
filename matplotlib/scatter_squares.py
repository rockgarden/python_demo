# 散点图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x_max = 101
x_values = list(range(1, x_max))
y_values = [x ** 2 for x in x_values]
y_max = (x_max + 1) ** 2  # TODO: 优化取整并增加一个Y轴单位

# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
# 参数 c 定义点颜色，edgecolor 定义点轮廓颜色，s 定义点大小
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
# colormap 颜色映射
# 参考 https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py

# Set chart title, and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, x_max, 0, y_max])

plt.savefig('output/squares_plot.png', bbox_inches='tight')  # 必须在 show 前运行
plt.show()

import numpy as np

# 褐色散点图
N = 40
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
plt.title("随机生成的数字散点")
plt.scatter(x, y, s=100, c='black', alpha=0.8)
plt.ylabel('Y坐标值')
plt.xlabel('X坐标值')
plt.show()

# 生成气泡图
N = 10
x = range(21, 31)
y = np.random.rand(10)
z = np.random.rand(40)
colors = np.random.rand(N)
plt.title("不同年龄下各等级的分值气泡图")
plt.scatter(x, y, c=colors, s=z * 1000, alpha=0.9)
plt.ylabel('等级')
plt.xlabel('年龄')
plt.show()
