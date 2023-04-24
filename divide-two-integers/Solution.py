// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = int(dividend / divisor)
        if not (-2**31 <= answer <= 2**31-1):
            return 2**31 - 1
        return answer