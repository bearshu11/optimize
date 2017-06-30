# import pandas as pd
import numpy as np


class TravellingSalesmanProblem:
    # decidedPathes,target,rowIndex,columnIndex:list型 matrix:np.array
    def __init__(self,matrix,decidedPathes,rowIndex,columnIndex,branchX=-1,target=[-1,-1]):
        if branchX == -1:
            pass
        else:
            convertdTarget = self.convertIndex(target,rowIndex,columnIndex)
            if branchX == 0:
                matrix[convertdTarget[0],convertdTarget[1]] = np.inf
            elif branchX == 1:
                del rowIndex[convertedTarget[0]]
                del columnIndex[convertedTarget[1]]
                matrix = self.removeRowColumn(convertdTarget,matrix)
                decidedPathes.append(target)

        self.matrix = matrix
        self.decidedPathes = decidedPathes
        self.rowIndex = rowIndex
        self.columnIndex = columnIndex
        self.lowerBound = np.inf

    def removeRowColumn(self,index,matrix):
        removedMatrix = np.delete(np.delete(matrix,index[0],0),index[1],1)
        return

    def convertIndex(self,target,rowIndex,columnIndex):
        r = rowIndex.index(target[0])
        c = columnIndex.index(target[1])
        return [r,c]

    def solveRelaxedProblem(self):
        matrix = self.matrix
        rowNum, colNum = matrix.shape

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
        self.lowerBound = Sr + Sc
        for decidedPath in self.decidedPathes:
            self.lowerBound += self.matrix[decidedPath[0],decidedPath[1]]

        # Scが０(一巡閉路)なら終端
        # terminal = True if Sc == 0 else False
        terminal = False

        return terminal


    def main(self):
        indexesOfMin = np.where(self.matrix == self.matrix.min())
        removedIndex = np.array([indexesOfMin[0][0],indexesOfMin[1][0]])
