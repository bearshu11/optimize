
class BranchAndBound:
    def __init__(self,problem,result,subjectValue):
        # process 処理を保存するスタック
        self.process = [problem]
        # result 暫定解
        self.result = result
        # subjectValue 暫定値
        self.subjectValue = subjectValue

    # self.problemを分枝限定法で解く
    def solve(self):
        if len(self.process) == 0:
            pass
        else:
            problem = self.process.pop()
            terminal, tempResult, tempSubjectValue = problem.solve()
            # 終端であるかどうか
            if terminal == True:
                # 求めた目的関数の値が暫定値より小さければ、暫定値・解を変更する
                if tempSubjectValue < self.subjectValue:
                    self.subjectValue = tempSubjectValue
                    self.result = tempResult
            else:
                # 求めた下界値が暫定値よりも小さければ分枝して処理を続ける
                if tempSubjectValue < self.subjectValue:
                    self.branch(problem)
            self.solve()

        return self.result, self.subjectValue

    # 分枝処理
    def branch(self,problem):
        problem0, problem1 = problem.branch()
        self.process.append(problem0)
        self.process.append(problem1)
