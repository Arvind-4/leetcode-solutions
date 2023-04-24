// https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        val = False
        l = []

        for i in range(int(c ** 0.5) + 1):
            b = (c - i * i) ** 0.5
            if b == int(b):
                val = True
                break

        return val
