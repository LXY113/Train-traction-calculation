from scipy.integrate import quad

# 定义被积函数
def c(x):
    return (-65.05999538619501 * 1 +
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
upper_limit = 0

# 计算积分
result, error = quad(integrand, lower_limit, upper_limit)

print(f"The result of the integral from {lower_limit} to {upper_limit} is: {result}")
print(f"The error estimate is: {error}")