from scipy.integrate import quad
import matplotlib.pyplot as plt

table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for upper_limit in range(0,81,1):
    def c(x):
        return (8.139845349685578 +
                0.1328532863554136 * x -
                0.044370452329027046 * x**2 +
                0.00450530267787368 * x**3 -
                0.0002418479879469376 * x**4 +
                7.66924851972472e-06 * x**5 -
                1.5081701789967263e-07 * x**6 +
                1.8563164450661327e-09 * x**7 -
                1.3891386770874718e-11 * x**8 +
                5.769608703690977e-14 * x**9 -
                1.0185281834710351e-16 * x**10)

    def integrand(v):
        return 60 / (120 * c(v))

    # 定义积分的下限和上限
    lower_limit = 0
    #upper_limit = 81.3

    # 计算积分
    result, error = quad(integrand, lower_limit, upper_limit)
    table1.append(result)
    y1.append(upper_limit)
    print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")

for upper_limit in range(82,99,1):
    def c(x):
        return (8.139845349685578 +
                0.1328532863554136 * x -
                0.044370452329027046 * x**2 +
                0.00450530267787368 * x**3 -
                0.0002418479879469376 * x**4 +
                7.66924851972472e-06 * x**5 -
                1.5081701789967263e-07 * x**6 +
                1.8563164450661327e-09 * x**7 -
                1.3891386770874718e-11 * x**8 +
                5.769608703690977e-14 * x**9 -
                1.0185281834710351e-16 * x**10+2)

    def integrand(v):
        return 60 / (120 * c(v))

    # 定义积分的下限和上限
    lower_limit = 81.3
    #upper_limit = 81.3

    # 计算积分
    result, error = quad(integrand, lower_limit, upper_limit)
    table2.append(result)
    y2.append(upper_limit-1.6)
    print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")

for upper_limit in range(99,91,-1):
    def c(x):
        return (8.139845349685578 +
                0.1328532863554136 * x -
                0.044370452329027046 * x**2 +
                0.00450530267787368 * x**3 -
                0.0002418479879469376 * x**4 +
                7.66924851972472e-06 * x**5 -
                1.5081701789967263e-07 * x**6 +
                1.8563164450661327e-09 * x**7 -
                1.3891386770874718e-11 * x**8 +
                5.769608703690977e-14 * x**9 -
                1.0185281834710351e-16 * x**10-5)

    def integrand(v):
        return 60 / (120 * c(v))

    # 定义积分的下限和上限
    lower_limit = 99.3
    #upper_limit = 81.3

    # 计算积分
    result, error = quad(integrand, lower_limit, upper_limit)
    table3.append(result)
    y3.append(upper_limit-3)
    print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")

for upper_limit in range(92,100,1):
    def c(x):
        return (8.139845349685578 +
                0.1328532863554136 * x -
                0.044370452329027046 * x**2 +
                0.00450530267787368 * x**3 -
                0.0002418479879469376 * x**4 +
                7.66924851972472e-06 * x**5 -
                1.5081701789967263e-07 * x**6 +
                1.8563164450661327e-09 * x**7 -
                1.3891386770874718e-11 * x**8 +
                5.769608703690977e-14 * x**9 -
                1.0185281834710351e-16 * x**10)

    def integrand(v):
        return 60 / (120 * c(v))

    # 定义积分的下限和上限
    lower_limit = 91.6
    #upper_limit = 81.3

    # 计算积分
    result, error = quad(integrand, lower_limit, upper_limit)
    table4.append(result)
    y4.append(upper_limit-3.2)
    print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")

for upper_limit in range(99,-1,-1):
    def c(x):
        return (-65.05999538619501 * 1 +  # 对于x=0时的特殊情况处理
                2.2948489428254444 * x -
                0.0872530119847595 * x**2 +
                0.0028711815804349375 * x**3 -
                7.535323778198846e-05 * x**4 +
                1.4808206943005465e-06 * x**5 -
                2.0873689579607042e-08 * x**6 +
                2.0239092465902265e-10 * x**7 -
                1.2716953881394252e-12 * x**8 +
                4.6365441769758436e-15 * x**9 +
                -7.416627700899087e-18 * x**10)

    def integrand(v):
        return 60 / (120 * c(v))

    # 定义积分的下限和上限
    lower_limit = 99.87
    #upper_limit = 99.87

    # 计算积分
    result, error = quad(integrand, lower_limit, upper_limit)
    table5.append(result)
    y5.append(upper_limit-4)
    print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")

for i in range(len(table2)):
    table2[i] += 6.506
for i in range(len(table3)):
    table3[i] += 8.012
for i in range(len(table4)):
    table4[i] += 9.803
for i in range(len(table5)):
    table5[i] += 11.064
table = table1 + table2 + table3 +table4 + table5
y = y1 + y2 + y3 + y4 + y5

print(table)
print(y)

# 创建一个图形
plt.figure()

# 绘制折线图
plt.plot(table, y, label='Speed Curve')  # 绘制折线图，并添加标签

# 添加标题和标签
plt.title('Train V-T Plot')
plt.xlabel('Time Used(Min)')
plt.ylabel('Train Speed(Km/h)')

# 显示图例
plt.legend()

# 显示图形
plt.show()