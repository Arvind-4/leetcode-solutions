// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0

        for num in nums:
            for digit in str(num):
                digitSum += int(digit)

        return abs(sum(nums) - digitSum)