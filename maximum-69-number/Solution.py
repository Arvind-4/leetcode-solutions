// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        l = []

        for i in range(len(nums)):
            if nums[i] == "6":
                val = nums[:i] + "9" + nums[i + 1:]
                return int(val)
        return num
        