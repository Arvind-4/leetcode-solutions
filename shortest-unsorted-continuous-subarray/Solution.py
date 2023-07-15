// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sortedNums = sorted(nums)
        lower, upper = n - 1, 0

        for i in range(n):
            if nums[i] != sortedNums[i]:
                lower = min(i, lower)
                upper = max(i, upper)
        if lower >= upper: return 0
        return upper - lower + 1
        

