// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:

        ans = x ** n
        num = "{:.5f}".format(ans)
        return float(num)