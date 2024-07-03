// https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i + j + 1 == len(mat[i]):
                    summ += mat[i][j]

        return summ
                
        