// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            if nums[i] % 3 == 0 and nums[i] % 2 == 0:
                l.append(nums[i])

        if len(l) == 0: return 0
        return int(sum(l) / len(l))