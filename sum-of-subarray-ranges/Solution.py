// https://leetcode.com/problems/sum-of-subarray-ranges

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        for i in range(n):
            maxx = -inf
            minn = inf
            for j in range(i, n):
                maxx = max(nums[j], maxx)
                minn = min(nums[j], minn)
                summ +=  maxx - minn
        return summ