// https://leetcode.com/problems/find-unique-binary-string

import random


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)


        for i in range(2 ** n):
            t = str(bin(i)).replace('0b', "")
            if len(t) < len(nums[0]):
                t += "0" * abs(len(t) - len(nums[0]))
            
            if t not in nums:
                return str(t)
        else:
            return ""