from TravellingSalesmanProblem import TravellingSalesmanProblem
from Optimization import BranchAndBound
import numpy as np

matrix = np.array([[np.inf,21,7,13,15],
                   [11,np.inf,19,12,25],
                   [15,24,np.inf,13,5],
                   [6,17,9,np.inf,22],
                   [28,6,11,5,np.inf]])
# matrix = np.array([[np.inf,21,5,15,9],
#                    [17,np.inf,12,6,24],
#                    [13,5,np.inf,20,8],
#                    [9,12,7,np.inf,23],
#                    [26,7,13,8,np.inf]])

problem = TravellingSalesmanProblem(matrix)
result = {}
subjectValue = np.inf
method = BranchAndBound(problem,result,subjectValue)
result, subjectValue = method.solve()
print(result, subjectValue)
