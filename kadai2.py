from NonLinearProgramming import GoldenSectionMethod, BisectionMethod, NewtonMethod
import math
import sympy as sym
E = sym.S.Exp1

# 問題１
def func1(x):
    return 1.0 / x + E ** x

# 問題２
def func2(x):
    return sym.sin(5.0*x) + (x-5.0) ** 2

print("****黄金分割法****")

# 問題１を黄金分割法で解く
problem = GoldenSectionMethod(func1, 0.0, 2.0)
problem.solve()
# problem.printErrorRangeGraph("GoldenSectionMethod1-1.png")
# problem.printErrorRangeGraphByLog("GoldenSectionMethod1-2.png")
x, ans = problem.getAnswer()
print("問題１：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))


# 問題２を黄金分割法で解く
problem = GoldenSectionMethod(func2, 0.0, 10.0)
problem.solve()
# problem.printErrorRangeGraph("GoldenSectionMethod2-1.png")
# problem.printErrorRangeGraphByLog("GoldenSectionMethod2-2.png")
x, ans = problem.getAnswer()
print("問題２：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))
print("傾き：" + str(problem.getGradientOfRangeErrorGraph()[0]))

print("****二分割法****")

# 問題１を二分割法で解く
problem = BisectionMethod(func1, 0.0, 2.0)
problem.solve()
# problem.printErrorRangeGraph("BisectionMethod1-1.png")
# problem.printErrorRangeGraphByLog("BisectionMethod1-2.png")
x, ans = problem.getAnswer()
print("問題１：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))

# 問題２を二分割法で解く
problem = BisectionMethod(func2, 0.0, 10.0)
problem.solve()
# problem.printErrorRangeGraph("BisectionMethod2-1.png")
# problem.printErrorRangeGraphByLog("BisectionMethod2-2.png")
x, ans = problem.getAnswer()
print("問題２：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))
print("傾き：" + str(problem.getGradientOfRangeErrorGraph()[0]))


print("****ニュートン法****")

# 問題１をニュートン法で解く
problem = NewtonMethod(func1, 1.6)
problem.solve()
# problem.printErrorRangeGraph("NewtonMethod1.png")
x, ans = problem.getAnswer()
print("問題１：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))

# 問題２をニュートン法で解く
problem = NewtonMethod(func2, 5.0)
problem.solve()
# problem.printErrorRangeGraph("NewtonMethod2.png")
x, ans = problem.getAnswer()
print("問題２：" + "   最適解：" + str(x) + "   " + "最適値：" + str(ans))
