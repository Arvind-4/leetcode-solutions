// https://leetcode.com/problems/sum-in-a-matrix

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        newNums = []
        for row in nums:
            newNums.append(sorted(row, reverse = True))
        tr = zip(*newNums)
        s = 0
        for i in tr:
            s += max(i)
        return s