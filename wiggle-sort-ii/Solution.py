// https://leetcode.com/problems/wiggle-sort-ii

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        i = 1
        j = n - 1
        res = [0] * n

        while i < n:
            res[i] = nums[j]
            i += 2
            j -= 1
        
        i = 0
        while i < n:
            res[i] = nums[j]
            i += 2
            j -= 1

        for i in range(n):
            nums[i] = res[i]

