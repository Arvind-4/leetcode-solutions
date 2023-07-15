// https://leetcode.com/problems/rotate-function

import math
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        summ = 0
        maxx = -math.inf 
        total = sum(nums)
        n = len(nums)
        for i in range(n):
            if i == 0:
                for j, value in enumerate(nums):
                    summ += value * j
            else:
                summ += -total + n * nums[i - 1]
            maxx = max(summ, maxx)
        return maxx