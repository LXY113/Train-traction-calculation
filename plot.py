import matplotlib.pyplot as plt

# 定义x轴数据
x = [0, 10, 20, 30, 40, 50, 60, 75, 84, 90, 100]

# 定义三个y轴数据
y1 = [8.14, 7.75, 7.34, 6.90, 6.43, 5.94, 5.39, 4.59, 4.06, 3.70, 2.25]
y2 = [-0.92, -0.98, -1.07, -1.19, -1.33, -1.50, -1.70, -2.04, -2.28, -2.47, -2.75]
y3 = [-65.00, -48.59, -39.52, -33.81, -29.92, -27.13, -25.07, -22.87, -21.91, -21.39, -20.69]

# 创建一个包含三个子图的图表
fig, axs = plt.subplots(3, 1, sharex=True)  # 3个子图，1行

# 绘制第一个折线图
for i in range(len(x)):
    axs[0].plot(x[i], y1[i], 'o', color='orange')  # 使用'o'标记数据点
    axs[0].text(x[i], y1[i]+0.2, f'{y1[i]:.2f}', ha='center', color='orange') 
axs[0].plot(x, y1, label='Line 1', color='orange')
axs[0].set_title('QianYin')
axs[0].set_ylabel('Y1')

# 绘制第二个折线图
for i in range(len(x)):
    axs[1].plot(x[i], y2[i], 'o', color='red')
    axs[1].text(x[i], y2[i]+0.2, f'{y2[i]:.2f}', ha='center', color='red')
axs[1].plot(x, y2, label='Line 2', color='red')
axs[1].set_title('DuoXing')
axs[1].set_ylabel('Y2')

# 绘制第三个折线图
for i in range(len(x)):
    axs[2].plot(x[i], y3[i], 'o', color='green')
    axs[2].text(x[i], y3[i]+2, f'{y3[i]:.2f}', ha='center', color='green')
axs[2].plot(x, y3, label='Line 3', color='green')
axs[2].set_title('ZhiDong')
axs[2].set_ylabel('Y3')

# 设置共享的x轴标签
plt.xlabel('X Axis')

# 显示图例
for ax in axs:
    ax.legend()

# 显示图形
plt.tight_layout()  # 调整子图布局以防止标签重叠
plt.show()