from scipy.integrate import quad

# 定义c关于v的函数关系
def c(v):
    return (8.139845349685578 * (v**0) +
            0.1328532863554136 * (v**1) -
            0.044370452329027046 * (v**2) +
            0.00450530267787368 * (v**3) -
            0.0002418479879469376 * (v**4) +
            7.66924851972472e-06 * (v**5) -
            1.5081701789967263e-07 * (v**6) +
            1.8563164450661327e-09 * (v**7) -
            1.3891386770874718e-11 * (v**8) +
            5.769608703690977e-14 * (v**9) -
            1.0185281834710351e-16 * (v**10)-5)
# 定义被积函数
def integrand(v):
    return v / (120 * c(v))

# 设置积分的下限和目标积分值
v_lower = 99.3
target_integral = 3

# 使用quad函数进行积分，并找到上限v
# 由于我们需要找到使得积分值等于target_integral的上限v，我们可以使用一个简单的搜索算法
# 这里我们使用逐步增加的方式，直到找到满足条件的v
v_upper = v_lower
while True:
    result, error = quad(integrand, v_lower, v_upper)
    if result >= target_integral:
        break
    v_upper -= 0.1  # 逐步增加上限v，这里0.1是步长，可以根据需要调整

# 打印结果
print(f"使得积分结果等于 {target_integral} 的上限 v 是 {v_upper:.2f}")