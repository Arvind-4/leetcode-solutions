// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            for row in matrix:
                if row:
                    result.append(row.pop(-1))
            if matrix:
                result.extend(reversed(matrix.pop(-1)))
            result.extend(reversed([row.pop(0) for row in matrix if row]))
        return result