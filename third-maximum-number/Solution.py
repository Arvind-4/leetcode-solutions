// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse = True)
        if len(nums) >= 3:
            return nums[2]
        else: return max(nums)