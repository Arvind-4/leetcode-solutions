// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        d = {}
        for num in nums:
            if num in d: d[num] += 1
            else: d[num] = 1
        
        nums[:] = d.get(0, 0) * [0] + d.get(1, 0) * [1] + d.get(2, 0) * [2]    