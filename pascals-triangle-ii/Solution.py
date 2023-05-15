// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = []
        for i in range(1, rowIndex + 2):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = answer[i - 2][j] + answer[i - 2][j - 1]
            if i - 1 == rowIndex:
                return row
            answer.append(row)
        return []