// https://leetcode.com/problems/find-the-pivot-integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i + 1

        return -1