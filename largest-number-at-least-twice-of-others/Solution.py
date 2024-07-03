// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxx = max(nums)
        maxidx = nums.index(maxx)

        for num in nums:
            if maxx < 2 * num and num != maxx:
                return -1

        return maxidx
    