import numpy as np
from scipy.integrate import quad

# 定义被积函数
def c(x):
    return (8.139845349685578 * (x**0) +
            0.1328532863554136 * (x**1) -
            0.044370452329027046 * (x**2) +
            0.00450530267787368 * (x**3) -
            0.0002418479879469376 * (x**4) +
            7.66924851972472e-06 * (x**5) -
            1.5081701789967263e-07 * (x**6) +
            1.8563164450661327e-09 * (x**7) -
            1.3891386770874718e-11 * (x**8) +
            5.769608703690977e-14 * (x**9) -
            1.0185281834710351e-16 * (x**10))

# 定义被积函数
def integrand(x):
    return x / (120 * c(x))

# 定义积分的下限和上限
lower_limit = 91.6
upper_limit = 99.87

# 计算积分
result, error = quad(integrand, lower_limit, upper_limit)

print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")
print(f"The error estimate is: {error}")

# 定义被积函数
def cc(y):
    return (-65.05999538619501 * 1 +  # 对于x=0时的特殊情况处理
            2.2948489428254444 * y -
            0.0872530119847595 * y**2 +
            0.0028711815804349375 * y**3 -
            7.535323778198846e-05 * y**4 +
            1.4808206943005465e-06 * y**5 -
            2.0873689579607042e-08 * y**6 +
            2.0239092465902265e-10 * y**7 -
            1.2716953881394252e-12 * y**8 +
            4.6365441769758436e-15 * y**9 +
            -7.416627700899087e-18 * y**10)

# 定义被积函数
def integrand(y):
    return y / (120 * cc(y))

# 定义积分的下限和上限
lower_limit = 0
upper_limit = 99.87

# 计算从0到99.8的积分
rresult, error = quad(integrand, lower_limit, upper_limit)

# 由于我们需要从99.8到0的积分，因此取结果的相反数
final_result = -rresult

print(f"The result of the integral from 99.8 to 0 is: {final_result}")
print(f"The error estimate is: {error}")

print(result+final_result)