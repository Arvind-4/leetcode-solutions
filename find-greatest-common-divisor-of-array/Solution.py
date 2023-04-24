// https://leetcode.com/problems/find-greatest-common-divisor-of-array

import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minEl = min(nums)
        maxEl = max(nums)
        return math.gcd(minEl, maxEl)

