import math
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

class FunctionMethod():
    def __init__(self, function, dif_func, x0, c_func, c0, c_interval, errorRangeLimit=0.00001, repeat_limit=100000):
        self.function = function
        self.dif_func = dif_func
        self.x = x0
        self.c = c0
        self.c_func = c_func
        self.c_interval = c_interval
        self.transition_x0 = []
        self.transition_x1 = []

        # 収束かどうかを判定するための値
        self.errorRangeLimit = errorRangeLimit

        self.repeat_limit = repeat_limit

    def solve(self):
        i = 0
        while True:
            self.transition_x0.append(self.x[0])
            self.transition_x1.append(self.x[1])
            solver = SteepestDecentMethod(self.function, self.dif_func, self.x, self.c_func(self.c))
            solver.solve()
            self.next_x = solver.x
            errorRange = math.fabs(np.linalg.norm(self.next_x - self.x))
            if errorRange > self.errorRangeLimit:
                self.x = self.next_x
            else:
                print("finish")
                self.x = self.next_x
                break
            self.c += self.c_interval
            if i > self.repeat_limit:
                break
            i += 1



    def getAnswer(self,title="", filename=""):
        if filename != "":
            # グラフの描画
            plt.figure()
            plt.title(title)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.xlim([0,2])
            plt.ylim([0,2])
            plt.plot(self.transition_x0, self.transition_x1)
            plt.savefig(filename)
        optX = self.x
        optA = self.function(optX, self.c)
        return optX, optA


class SteepestDecentMethod():
    def __init__(self, function, dif_func, x0, c, dx=0.001):
        self.function = function
        self.dif_func = dif_func
        self.x = x0
        self.c = c
        self.dx = dx
        self.errorRangeLimit = 0.00001

    def solve(self):
        while True:
            # 探索方向の決定
            self.s = -self.dif_func(self.x, self.c)
            # 次のxの値を取得
            self.nextX = self.getNextX()

            errorRange = math.fabs(np.linalg.norm(self.nextX - self.x))

            # 収束したかどうかの判定
            if errorRange > self.errorRangeLimit:
                self.x = self.nextX
            else:
                break

    def getNextX(self):
        # ラインサーチ（2次近似法）を用いる
        x1 = self.x + self.dx * self.s
        x2 = self.x + 2.0 * self.dx * self.s
        p = (self.function(x2, self.c) - 2.0 * self.function(x1, self.c) + self.function(self.x, self.c)) / (2 * self.dx ** 2)
        q = (-self.function(x2, self.c) + 4.0 * self.function(x1, self.c) - 3 * self.function(self.x, self.c)) / (2 * self.dx)
        alpha = -q / (2.0 * p)

        nextX = self.x + alpha * self.s
        return nextX
