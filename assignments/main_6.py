from method_6 import FunctionMethod
import numpy as np
import math

# 問題として与えられた関数
def f(x):
    return 3.0 * pow(x[0], 2) + 2.0 * pow(x[1], 2)

# 障壁法の最適化問題
def f_barrier(x, c):
    return 3.0 * pow(x[0], 2) + 2.0 * pow(x[1], 2) - c * math.log(x[0]+x[1]-1.0)

# f_barrierの１階微分
def dif_f_barrier(x, c):
    return np.array([6.0 * x[0] - (c / (x[0]+x[1]-1.0)), 4.0 * x[1] - (c / (x[0]+x[1]-1.0))])

# 罰則法の最適化問題
def f_penalty(x, c):
    return 3.0 * pow(x[0], 2) + 2.0 * pow(x[1], 2) + c * pow(max(0, 1.0 - x[0] - x[1]) ,2)

# f_penaltyの１階微分
def dif_f_penalty(x, c):
    h = 1.0 - x[0] - x[1]
    if h < 0:
        return np.array([6.0 * x[0], 4.0 * x[1]])
    else:
        return np.array([6.0 * x[0] - 2 * c * h * x[0], 4.0 * x[1] - 2 * c * h * x[1]])

# 障壁法でc_kを定める関数
def c_func_barrier(x):
    return pow(x, 2)

# 罰則法でc_kを定める関数
def c_func_penalty(x):
    return pow(x, 1.1)


if __name__ == "__main__":
    x0 = np.array([1,1])
    c0 = 1.5
    c_interval = -0.001
    method = FunctionMethod(f_barrier, dif_f_barrier, x0, c_func_barrier, c0, c_interval, 0.00003, 1500)
    method.solve()
    x,a = method.getAnswer(title="BarrierMethod", filename="./barrier.png")
    print("最適解: ", x)
    print("最適値: ", f(x))

    x0 = np.array([1,1])
    c0 = 0.5
    c_interval = 0.01
    method = FunctionMethod(f_penalty, dif_f_penalty, x0, c_func_penalty, c0, c_interval)
    method.solve()
    x,a = method.getAnswer(title="PenaltyMethod", filename="./penalty.png")
    print("最適解: ", x)
    print("最適値: ", f(x))
