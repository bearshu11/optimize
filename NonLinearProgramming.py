import math
import numpy as np
from utilmath import *
from abc import ABCMeta, abstractmethod
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# 非線形計画法の手法の抽象クラス
class NonLinearMethod(metaclass=ABCMeta):

    def __init__(self, function):
        self.function = function

        # 収束する過程で出てくる解の範囲を保存しておくためのリスト
        self.errorRanges = []

        # 収束かどうかを判定するための値
        self.errorRangeLimit = 0.001

    def setErrorRangeLimit(self, val):
        self.errorRangeLimit = val

    # 収束過程をグラフ化し、画像として保存する
    def printErrorRangeGraph(self,fileName='ErrorRange.png'):
        plt.figure()
        plt.plot(self.errorRanges)
        plt.savefig(fileName)

    # 収束過程をグラフ化(対数を取って直線化)し、画像として保存する
    def printErrorRangeGraphByLog(self,fileName='ErrorRangeByLog.png'):
        plt.figure()
        npErrorRanges = np.array(self.errorRanges)
        plt.plot(np.log(npErrorRanges))
        plt.savefig(fileName)

    # 収束過程の直線化したグラフの傾きを求める
    def getGradientOfRangeErrorGraph(self):
        npErrorRanges = np.array(self.errorRanges)
        return np.gradient(np.log(npErrorRanges))

    # 収束するまで再起を用いて解を求める。
    @abstractmethod
    def solve(self):
        pass

    # 次の評価点を求める(solveの再起の時に使う)
    @abstractmethod
    def getNextX(self):
        pass

    # 最適解とそのときの目的関数の値を求める
    @abstractmethod
    def getAnswer(self):
        pass

# 黄金分割法
# function 対象の関数
# lowLimit 解の下限値
# upLimit 解の上限値
class GoldenSectionMethod(NonLinearMethod):
    def __init__(self, function, lowLimit, upLimit):
        super().__init__(function)
        self.lowLimit = lowLimit
        self.upLimit = upLimit
        # 黄金比
        self.goldenRatio = (math.sqrt(5) - 1) / 2.0

    def solve(self):
        errorRange = self.upLimit - self.lowLimit
        # 現在の解の範囲を保存
        self.errorRanges.append(errorRange)

        # 収束していないときの処理
        if errorRange > self.errorRangeLimit:
            x1, x2 = self.getNextX()
            f1 = self.function(x1)
            f2 = self.function(x2)
            if f2 > f1:
                self.upLimit = x2
            else:
                self.lowLimit = x1

            self.solve()

    def getNextX(self):
        distance = self.upLimit - self.lowLimit
        distanceX2 = distance * self.goldenRatio
        x2 = self.lowLimit + distanceX2
        distanceX1 = distanceX2 * self.goldenRatio
        x1 = self.lowLimit + distanceX1
        return x1, x2

    def getAnswer(self):
        optX = (self.upLimit + self.lowLimit) / 2.0
        optA = self.function(optX)
        return optX, optA

# 二分割法
# function 対象の関数
# lowLimit 解の下限値
# upLimit 解の上限値
class BisectionMethod(NonLinearMethod):
    def __init__(self, function, lowLimit, upLimit):
        super().__init__(function)
        self.lowLimit = lowLimit
        self.upLimit = upLimit

    def solve(self):
        errorRange = self.upLimit - self.lowLimit

        # 現在の解の範囲を保存
        self.errorRanges.append(errorRange)

        # 収束していないときの処理
        if errorRange > self.errorRangeLimit:
            x = self.getNextX()
            fd = differentiate(self.function, x)
            if fd > 0:
                self.upLimit = x
            else:
                self.lowLimit = x

            self.solve()

    def getNextX(self):
        nextX = (self.upLimit + self.lowLimit) / 2.0
        return nextX

    def getAnswer(self):
        optX = (self.upLimit + self.lowLimit) / 2.0
        optA = self.function(optX)
        return optX, optA

# ニュートン法
# function 対象の関数
# x 初めの評価点
class NewtonMethod(NonLinearMethod):
    def __init__(self, function, x):
        super().__init__(function)
        self.x = x
        self.nextX = self.getNextX()

    def solve(self):
        errorRange = math.fabs(self.nextX - self.x)
        # 現在の評価点の値と次の評価点の値の差を保存
        self.errorRanges.append(errorRange)

        # 次の評価点がinfまたはnanのときエラー表示をする
        if self.nextX == (float("inf") or float("-inf")):
            print("Error Inf : x does not converge")
            return
        elif math.isnan(self.nextX):
            print("Error Nan : x does not converge")
            return

        # 収束していないときの処理
        if errorRange > self.errorRangeLimit:
            self.x = self.nextX
            self.nextX = self.getNextX()
            self.solve()

    def getNextX(self):
        nextX = self.x - differentiate(self.function, self.x) / differentiate2(self.function, self.x)
        return nextX

    def getAnswer(self):
        optX = self.nextX
        optA = self.function(optX)
        return optX, optA
