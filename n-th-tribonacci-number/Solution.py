// https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1

        a = 0
        b = 1
        c = 1

        for i in range(n - 2):
            summ = a + b + c
            a = b
            b = c
            c = summ

        return c
