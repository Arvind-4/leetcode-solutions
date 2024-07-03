// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        base = heights.copy()
        base.sort()
        ans = 0

        for i, j in zip(base, heights):
            if (i != j):
                ans += 1
        return ans
        