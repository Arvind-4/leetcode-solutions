// https://leetcode.com/problems/number-of-unequal-triplets-in-array

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        ans = 0

        for i, counter in Counter(nums).items():
            right -= counter
            ans += left * counter * right
            left += counter
        return ans
        