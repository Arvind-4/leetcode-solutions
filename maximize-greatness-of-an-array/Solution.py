// https://leetcode.com/problems/maximize-greatness-of-an-array

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[count] < nums[i]:
                count += 1

        return count