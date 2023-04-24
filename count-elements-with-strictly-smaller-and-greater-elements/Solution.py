// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

class Solution:
    def countElements(self, nums: List[int]) -> int:

        count = 0

        for i in range(len(nums)):
            if nums[i] < max(nums) and nums[i] > min(nums):
                count += 1

        return count