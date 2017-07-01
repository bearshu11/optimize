import numpy as np
import copy
class TravellingSalesmanProblem:
    # matrix:np.array
    def __init__(self,matrix,decidedPathes={},rowIndexes=[],columnIndexes=[]):
        self.matrix = matrix
        self.decidedPathes = decidedPathes
        self.rowIndexes = rowIndexes
        self.columnIndexes = columnIndexes
        if len(self.rowIndexes) == 0 and len(self.columnIndexes) == 0:
            rowNum, colNum = matrix.shape
            for i in range(1,rowNum+1):
                self.rowIndexes.append(i)
                self.columnIndexes.append(i)

    def branch(self):
        # 0から始まるインデックスの状態
        indexesOfMin = np.where(self.matrix == self.matrix.min())
        targetIndex = (indexesOfMin[0][0],indexesOfMin[1][0])
        # 都市1~nに対応したインデックスの状態
        convertdTargetIndex = self.convertToCityIndex(targetIndex,
                                                      self.rowIndexes,
                                                      self.columnIndexes)
        print(convertdTargetIndex)
        # x=0で分岐した先のTravellingSalesmanProblemのインスタンス作成
        matrix0 = copy.deepcopy(self.matrix)
        matrix0[targetIndex[0],targetIndex[1]] = np.inf
        rowIndexes0 = copy.deepcopy(self.rowIndexes)
        columnIndexes0 = copy.deepcopy(self.columnIndexes)
        decidedPathes0 = copy.deepcopy(self.decidedPathes)
        problem0 = TravellingSalesmanProblem(matrix0,decidedPathes0,
                                             rowIndexes0,columnIndexes0)

        # x=1で分岐した先のTravellingSalesmanProblemのインスタンス作成
        matrix1 = copy.deepcopy(self.matrix)
        rowIndexes1 = copy.deepcopy(self.rowIndexes)
        columnIndexes1 = copy.deepcopy(self.columnIndexes)
        del rowIndexes1[targetIndex[0]]
        del columnIndexes1[targetIndex[1]]
        matrix1 = self.removeRowColumn(targetIndex,matrix1)
        decidedPathes1 = copy.deepcopy(self.decidedPathes)
        decidedPathes1[convertdTargetIndex] = self.matrix[targetIndex[0],targetIndex[1]]
        problem1 = TravellingSalesmanProblem(matrix1,decidedPathes1,
                                             rowIndexes1,columnIndexes1)

        return problem0, problem1

    def removeRowColumn(self,index,matrix):
        removedMatrix = np.delete(np.delete(matrix,index[0],0),index[1],1)
        return removedMatrix

    def convertToCityIndex(self,target,rowIndexes,columnIndexes):
        r = rowIndexes[target[0]]
        c = columnIndexes[target[1]]
        return (r,c)

    def convertToNormalIndex(self,target,rowIndexes,columnIndexes):
        r = rowIndexes.index(target[0])
        c = columnIndexes.index(target[1])
        return (r,c)

    def solve(self):
        matrix = copy.deepcopy(self.matrix)
        rowNum, colNum = matrix.shape

        if rowNum > 1:
            # 各行の最小値を求めて各行から引く
            Sr = 0
            for i in range(0,rowNum):
                row = matrix[i,:]
                Sr += row.min()
                row = row - row.min()
                matrix[i,:] = row

            # 各列の最小値を求めて各列から引く
            Sc = 0
            for i in range(0,colNum):
                column = matrix[:,i]
                Sc += column.min()
                column = column - column.min()
                matrix[:,i] = column

            # 下界値
            lowerBound = Sr + Sc
            for value in self.decidedPathes.values():
                lowerBound += value

            # Scが０(一巡閉路)なら終端
            # TODO:議論が間違っているので正しく変更
            terminal = True if Sc == 0 else False
            # TODO:返却する解を決める
            result = self.decidedPathes if terminal == True else None
        else:
            lowerBound = matrix[0][0]
            for value in self.decidedPathes.values():
                lowerBound += value
            terminal = True
            result = self.decidedPathes
        return terminal, result, lowerBound
