import numpy as np
import copy

# 巡回セールスマン問題:分枝限定法対応
class TravellingSalesmanProblem:
    # @param np.array matrix, {(int,int):int} decidedPathes, int[] rowIndexes int[] columnIndexes
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

    # 分岐先の二つの部分問題を生成する
    # @return problem0, problem1
    def branch(self):
        # 分岐先として経路が短いものから選択する
        indexesOfMin = np.where(self.matrix == self.matrix.min())
        # 0から始まる(単なる配列として考えるときの)インデックスでの値
        targetIndex = (indexesOfMin[0][0],indexesOfMin[1][0])
        # 都市1~nに対応したインデックスでの値
        convertdTargetIndex = self.convertToCityIndex(targetIndex,
                                                      self.rowIndexes,
                                                      self.columnIndexes)

        # このTravellingSalesmanProblemインスタンスのメンバーをコピー
        matrix0, rowIndexes0, columnIndexes0, decidedPathes0 = self.copySelfMember()
        matrix1, rowIndexes1, columnIndexes1, decidedPathes1 = self.copySelfMember()

        # 選択した経路を通らないとしたとき(xij=0)の分岐処理(dij = inf)
        matrix0[targetIndex[0],targetIndex[1]] = np.inf

        # x=0で分岐した先のTravellingSalesmanProblemのインスタンス作成
        problem0 = TravellingSalesmanProblem(matrix0,decidedPathes0,
                                             rowIndexes0,columnIndexes0)

        # 選択した経路を通るとしたとき(xij=1)の分岐処理(i行とj列を取り除く処理等)
        del rowIndexes1[targetIndex[0]]
        del columnIndexes1[targetIndex[1]]
        matrix1 = self.removeRowColumn(targetIndex,matrix1)
        decidedPathes1[convertdTargetIndex] = self.matrix[targetIndex[0],targetIndex[1]]

        # x=1で分岐した先のTravellingSalesmanProblemのインスタンス作成
        problem1 = TravellingSalesmanProblem(matrix1,decidedPathes1,
                                             rowIndexes1,columnIndexes1)

        return problem0, problem1

    def copySelfMember(self):
        matrix = copy.deepcopy(self.matrix)
        rowIndexes = copy.deepcopy(self.rowIndexes)
        columnIndexes = copy.deepcopy(self.columnIndexes)
        decidedPathes = copy.deepcopy(self.decidedPathes)
        return matrix, rowIndexes, columnIndexes, decidedPathes

    # xij=1としたときの行列からi行とj列を取り除く処理
    def removeRowColumn(self,index,matrix):
        removedMatrix = np.delete(np.delete(matrix,index[0],0),index[1],1)
        return removedMatrix

    # 配列のインデックス(0,1,...)から都市のインデックスに変更
    def convertToCityIndex(self,target,rowIndexes,columnIndexes):
        r = rowIndexes[target[0]]
        c = columnIndexes[target[1]]
        return (r,c)

    # 都市のインデックスから配列のインデックスに変更
    def convertToNormalIndex(self,target,rowIndexes,columnIndexes):
        r = rowIndexes.index(target[0])
        c = columnIndexes.index(target[1])
        return (r,c)

    # TravellingSalesmanProblemを解く
    # @return bool terminal, {(int,int):int} result, int lowerBound
    def solve(self):
        matrix = copy.deepcopy(self.matrix)
        rowNum, colNum = matrix.shape

        if rowNum > 1:
            # 各行の最小値を求めて各行から引く
            Sr = 0
            for i in range(0,rowNum):
                row = matrix[i,:]
                Sr += row.min()
                if row.min() != np.inf:
                    row = row - row.min()
                matrix[i,:] = row

            # 各列の最小値を求めて各列から引く
            Sc = 0
            for i in range(0,colNum):
                column = matrix[:,i]
                Sc += column.min()
                if column.min() != np.inf:
                    column = column - column.min()
                matrix[:,i] = column

            # 下界値を求める
            lowerBound = Sr + Sc
            for value in self.decidedPathes.values():
                lowerBound += value

            # 将来的に変更すべきTODO
            # TODO:一巡閉路なら終端になるようにする処理
            # terminal = True if Sc == 0 else False >>不可
            terminal = False

            # 将来的に変更すべきTODO
            # TODO:返却する解の変更
            result = self.decidedPathes if terminal == True else None
        else:
            # 下界値を求める
            lowerBound = matrix[0][0]
            for value in self.decidedPathes.values():
                lowerBound += value

            # これ以上分枝できないので終端
            terminal = True

            result = self.decidedPathes
            result[(self.rowIndexes[0], self.columnIndexes[0])] = matrix[0][0]

        return terminal, result, lowerBound
