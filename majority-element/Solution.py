// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in nums:
            if i in d: d[i] += 1
            else: d[i] = 1
        for k, v in d.items():
            if v > n // 2:
                return k
        