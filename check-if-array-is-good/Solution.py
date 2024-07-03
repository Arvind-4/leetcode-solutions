// https://leetcode.com/problems/check-if-array-is-good

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        madeup = [i for i in range(1, len(nums))]
        madeup.append(len(nums) - 1)
        nums.sort()
        return nums == madeup