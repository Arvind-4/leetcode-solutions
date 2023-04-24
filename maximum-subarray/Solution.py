// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]  
        temp = 0
        for i in range(len(nums)):
            if temp < 0: temp = 0
            temp += nums[i]
            if temp > max_: max_ = temp    
        return max_