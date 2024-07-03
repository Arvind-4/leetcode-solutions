// https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = 0
        n0 = 0
        maxlen = 0
        d = {}

        d[0] = -1
        
        for i in range(n):
            n1 += nums[i]
            n0 = (i + 1) - n1
            if n1 - n0 in d:
                maxlen = max(maxlen, i - d[n1 - n0])
            else: d[n1 - n0] = i
        return maxlen
        