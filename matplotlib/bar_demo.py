import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

N = 5
inMeans = (20, 25, 30, 35, 27)
outMeans = (25, 35, 34, 20, 25)
inStd = (2, 3, 4, 1, 2)
outStd = (3, 5, 2, 3, 3)
ind = np.arange(N)  # Bar坐标位置
width = 0.5  # Bar的宽度
p1 = plt.bar(ind, inMeans, width, yerr=inStd)
p2 = plt.bar(ind, outMeans, width, bottom=inMeans, yerr=outStd)
plt.ylabel('分值')
plt.title('不同组用户下国内外用户分值')
plt.xticks(ind, ('组1', '组2', '组3', '组4', '组5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('国内', '国外'))
plt.show()
