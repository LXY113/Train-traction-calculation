import matplotlib.pyplot as plt
import numpy as np

# 定义x轴和y轴数据
x_values = [0, 10, 20, 30, 40, 50, 60, 75, 84, 90, 100,110,120,130]
y_values = [8.14, 7.75, 7.34, 6.90, 6.43, 5.94, 5.39, 4.59, 4.06, 3.70, 2.26,1.64,1.05,0.35]

# 将列表转换为numpy数组
x = np.array(x_values)
y = np.array(y_values)

# 选择多项式的阶数，例如二次（2），三次（3），等等
degree = 9  # 多项式拟合的阶数

# 多项式拟合
coefficients = np.polyfit(x, y, degree)

# 打印多项式系数
print("Polynomial coefficients:", coefficients)

# 根据系数创建多项式方程
# 系数从最高次项到常数项，例如：ax^2 + bx + c
equation = "y = " + " + ".join(f"{coef}x^{i}" for i, coef in enumerate(coefficients[::-1]))

# 打印多项式方程
print("Polynomial equation:", equation)

# 绘制原始数据点
plt.scatter(x, y, label='Data points')

# 绘制拟合曲线
polynomial = np.poly1d(coefficients)
x_fit = np.linspace(min(x), max(x), 100)  # 生成用于绘制的x值
y_fit = polynomial(x_fit)
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: {equation}')

# 在每个数据点旁边添加数值标签
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.text(xi, yi, f'{yi:.2f}', ha='center', va='bottom')

# 添加图例、标题和坐标轴标签
plt.legend()
plt.title('Polynomial Fit with Equation')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示网格
plt.grid(True)

# 显示图形
plt.show()