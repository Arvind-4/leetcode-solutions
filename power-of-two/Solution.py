// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        prod = 1
        while prod < n:
            prod *= 2

        return prod == n