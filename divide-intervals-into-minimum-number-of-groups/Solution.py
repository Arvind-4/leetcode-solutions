// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        maxx = max([v for _, v in intervals])
        dp = [0] * (maxx + 2)

        for x, y in intervals:
            dp[x] += 1
            dp[y + 1] -= 1
        
        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]

        return max(dp)