// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = answer[i - 2][j] + answer[i - 2][j - 1]
            answer.append(row)
        return answer