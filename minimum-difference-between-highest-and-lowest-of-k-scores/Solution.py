// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            r += 1
            l += 1
        return res