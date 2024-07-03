// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        n = len(nums)

        for i in range(n):
            if nums[(i - 1) % n] > nums[i]:
                count += 1
            if count > 1: return False
        return True