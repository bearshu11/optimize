from TravellingSalesmanProblem import TravellingSalesmanProblem
from Optimization import BranchAndBound
import numpy as np

matrix = np.array([[np.inf,21,7,13,15],
                   [11,np.inf,19,12,25],
                   [15,24,np.inf,13,5],
                   [6,17,9,np.inf,22],
                   [28,6,11,5,np.inf]])

problem = TravellingSalesmanProblem(matrix)

# 暫定値と暫定解の設定
result = {}
subjectValue = np.inf

method = BranchAndBound(problem,result,subjectValue)

# 分枝限定法で巡回セールスマン問題を解く
result, subjectValue = method.solve()

cityNum = list(result.keys())[0][0]
answer = ""
answer += str(list(result.keys())[0][0])
i = 0
while i<len(result):
    for key in result.keys():
        if key[0] == cityNum:
            answer += " -> "
            answer += str(key[1])
            cityNum = key[1]
            i += 1
print("Route: " + answer)
print("Distance: " + str(subjectValue))
