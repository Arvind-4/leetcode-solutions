// https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            elif nums[i] < nums[i - 1]:
                inc = False
        return dec or inc