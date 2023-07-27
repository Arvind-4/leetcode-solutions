// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros, res, left = 0, 0, 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            res = max(res, right - left + 1 - zeros)

        return res - 1 if res == n else res