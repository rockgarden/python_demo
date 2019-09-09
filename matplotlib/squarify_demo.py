import matplotlib.pyplot as plt
import squarify

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

squarify.plot(sizes=[20, 10, 30, 40], label=["组A(20%)", "组B(10%)", "组C(30%)", "组D(40%)"],
              color=["red", "green", "blue", "grey"], alpha=.4)
plt.axis('off')
plt.title('不同组用户比例')
plt.show()
