// https://leetcode.com/problems/maximum-sum-of-an-hourglass

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        summ = 0
        maxx = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                summ = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                maxx = max(summ, maxx)

        return maxx



        

        