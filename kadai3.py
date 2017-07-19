import numpy as np
from NonLinearProgramming import SteepestDecentMethod,FletcherReeves,BFGS

def f1(x):
    A = np.array([[9,12,-6,-3],
                  [12,41,2,11],
                  [-6,2,24,-8],
                  [-3,11,-8,62]])
    b = np.array([-27,-42,32,-23])
    c = 163
    return 0.5 * np.dot(np.dot(x,A), x) + np.dot(b,x) + c

def dif_f1(x):
    A = np.array([[9,12,-6,-3],
                  [12,41,2,11],
                  [-6,2,24,-8],
                  [-3,11,-8,62]])
    b = np.array([-27,-42,32,-23])
    return np.dot(A,x) + b

def f2(x):
    A = np.array([[16,8,12,-12],
                  [8,29,16,9],
                  [12,16,29,-19],
                  [-12,9,-19,35]])
    b = np.array([7,5,-2,9])
    c = 5
    return 0.5 * np.dot(np.dot(x,A), x) + np.dot(b,x) + c

def dif_f2(x):
    A = np.array([[16,8,12,-12],
                  [8,29,16,9],
                  [12,16,29,-19],
                  [-12,9,-19,35]])
    b = np.array([7,5,-2,9])
    return np.dot(A,x) + b

def f3(x):
    return (x[0] - 1.0) ** 2 + 10 * (x[0] ** 2.0 -x[1]) ** 2

def dif_f3(x):
    return np.array([(2*(x[0]-1.0) + 40 * (x[0] ** 2 - x[1]) * x[0]), (20.0*(x[0] ** 2 - x[1]))])


print("***(1)***")
print("***再急降下法***")
method = SteepestDecentMethod(f1,dif_f1,np.array([1,1,1,1]))
method.solve()
method.printErrorRangeGraph("steepest1.png")
x,a = method.getAnswer()
print("最適解: ", x)
print("最適値: ", a)

print("***共役勾配法***")
method = FletcherReeves(f1,dif_f1,np.array([1,1,1,1]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("flether1.png")
print("最適解: ", x)
print("最適値: ", a)

print("***準ニュートン法***")
method = BFGS(f1,dif_f1,np.array([1,1,1,1]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("bfgs1.png")
print("最適解: ", x)
print("最適値: ", a)

print()
print("***(2)***")
print("***再急降下法***")
method = SteepestDecentMethod(f2,dif_f2,np.array([-10,-10,-10,-10]))
method.solve()
method.printErrorRangeGraph("steepest2.png")
x,a = method.getAnswer()
print("最適解: ", x)
print("最適値: ", a)

print("***共役勾配法***")
method = FletcherReeves(f2,dif_f2,np.array([1,1,1,1]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("flether2.png")
print("最適解: ", x)
print("最適値: ", a)

print("***準ニュートン法***")
method = BFGS(f2,dif_f2,np.array([1,1,1,1]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("bfgs2.png")
print("最適解: ", x)
print("最適値: ", a)

print()
print("***(3)***")
print("***再急降下法***")
method = SteepestDecentMethod(f3,dif_f3,np.array([2,2]))
method.solve()
method.printErrorRangeGraph("steepest3.png")
x,a = method.getAnswer()
print("最適解: ", x)
print("最適値: ", a)

print("***共役勾配法***")
method = FletcherReeves(f3,dif_f3,np.array([2,2]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("flether3.png")
print("最適解: ", x)
print("最適値: ", a)

print("***準ニュートン法***")
method = BFGS(f3,dif_f3,np.array([0.1,0.1]))
method.solve()
x,a = method.getAnswer()
method.printErrorRangeGraph("bfgs3.png")
print("最適解: ", x)
print("最適値: ", a)
