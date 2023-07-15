// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0: return 0
        if n <= 2: return 1
        for i in range(n - 2 + 1):
            c = a + b
            a = b
            b = c
        return b           