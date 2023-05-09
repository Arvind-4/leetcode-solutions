// https://leetcode.com/problems/separate-the-digits-in-an-array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            l += list(map(int, str(nums[i])))
        return l
