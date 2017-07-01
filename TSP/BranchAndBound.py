
class BranchAndBound:

    def __init__(self,problem,result,subjectValue):
        self.problem = problem
        self.process = [self.problem]
        self.result = result
        self.subjectValue = subjectValue

    def solve(self):
        if len(self.process) == 0:
            pass
        else:
            prob = self.process.pop()
            terminal, tempResult, tempSubjectValue = prob.solve()
            # 終端であるかどうか
            if terminal == True:
                if tempSubjectValue < self.subjectValue:
                    self.subjectValue = tempSubjectValue
                    self.result = tempResult
            else:
                if tempSubjectValue < self.subjectValue:
                    self.branch(prob)
            self.solve()

    def branch(self,prob):
        problem0, problem1 = prob.branch()
        self.process.append(problem0)
        self.process.append(problem1)
