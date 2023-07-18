// https://leetcode.com/problems/neither-minimum-nor-maximum

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)

        for i in nums:
            if i != mx and i != mn:
                return i


        return -1