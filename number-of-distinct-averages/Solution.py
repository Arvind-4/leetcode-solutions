// https://leetcode.com/problems/number-of-distinct-averages

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        s = set()
        while left <= right:
            s.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return len(s)
        