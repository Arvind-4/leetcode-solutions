// https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        prod = 1
        while prod < n:
            prod *= 4

        return prod == n