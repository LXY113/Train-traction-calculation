from scipy.integrate import quad

# 定义被积函数
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
upper_limit = 99.3

# 计算积分
result, error = quad(integrand, lower_limit, upper_limit)

print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")
print(f"The error estimate is: {error}")