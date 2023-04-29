// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0: return False
        if n == 0: return False
        if n == 1: return True

        prod = 1
        while prod < n:
            prod *= 3

        if prod == n: return True

        return False
