// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index = 0
        maxel = float('-inf')
        for i in range(len(nums)):
            if nums[i] > maxel:
                maxel = nums[i]
                index = i
        return index