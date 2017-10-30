import math
import numpy as np
from abc import ABCMeta, abstractmethod
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

class NonLinearMethod(metaclass=ABCMeta):

    def __init__(self, function):
        self.function = function

        # 収束かどうかを判定するための値
        self.errorRangeLimit = 0.00001


class SteepestDecentMethod(NonLinearMethod):
    def __init__(self, function, dif_func, x0):
        super().__init__(function)
        self.dif_func = dif_func
        self.x = x0
        self.transition_x0 = []
        self.transition_x1 = []

    def backtrack(self, alpha=0.5, beta=0.8):
        while True:
            self.transition_x0.append(self.x[0])
            self.transition_x1.append(self.x[1])
            dx = 1.0
            while True:
                next_x = self.x - dx * self.dif_func(self.x)
                armijo_rule = self.function(next_x) - self.function(self.x) + alpha * dx * pow(np.linalg.norm(self.dif_func(self.x)), 2)
                if armijo_rule <= 0:
                    break
                else:
                    dx *= beta
            self.nextX = next_x

            errorRange = math.fabs(np.linalg.norm(self.nextX - self.x))

            # 収束したかどうかの判定
            if errorRange > self.errorRangeLimit:
                self.x = self.nextX
            else:
                break

    def getAnswer(self, filename=""):
        if filename != "":
            # グラフの描画
            plt.figure()
            plt.title("Back Tracking Line Search")
            plt.xlabel("x1")
            plt.ylabel("x2")
            plt.xlim([-5,5])
            plt.ylim([-5,5])
            plt.plot(self.transition_x0, self.transition_x1)
            plt.savefig(filename)
        optX = self.nextX
        optA = self.function(optX)
        return optX, optA

# 問題として与えられた関数
def f(x):
    return 10.0 * pow(x[0], 2) + pow(x[1], 2)

# 与えられた関数の１階微分
def dif_f(x):
    return np.array([20.0 * x[0], 2 * x[1]])

if __name__ == "__main__":
    # 初期値
    x0 = np.array([1.0,5.0])

    method = SteepestDecentMethod(f,dif_f,x0)
    method.backtrack()
    x,a = method.getAnswer(filename="./backtrack.png")
    print("最適解: ", x)
    print("最適値: ", a)
