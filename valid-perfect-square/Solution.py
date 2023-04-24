// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        val = False
        if num == 1: return True

        for i in range(int(num ** 0.5) + 1):
            if i * i == num:
                val = True
                break
        return val