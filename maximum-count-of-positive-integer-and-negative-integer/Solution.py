// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCount, negCount = 0, 0

        for i in nums:
            if i < 0: negCount += 1
            if i > 0: posCount += 1

        return max(negCount, posCount)