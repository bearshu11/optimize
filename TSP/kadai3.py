from TravellingSalesmanProblem import TravellingSalesmanProblem
from BranchAndBound import BranchAndBound
import numpy as np

matrix = np.array([[np.inf,21,7,13,15],
                   [11,np.inf,19,12,25],
                   [15,24,np.inf,13,5],
                   [6,17,9,np.inf,22],
                   [28,6,11,5,np.inf]])

problem = TravellingSalesmanProblem(matrix)
result = {}
subjectValue = 50
method = BranchAndBound(problem,result,subjectValue)
method.solve()
print(method.result)
