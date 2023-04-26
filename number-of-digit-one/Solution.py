// https://leetcode.com/problems/number-of-digit-one

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        if n < 10: return 1

        count = 0
        power = 1

        while power <= n:
            divisor = power * 10
            quotient = n // divisor
            remainder = n % divisor

            if quotient > 0:
                count += quotient * power
            if remainder >= power:
                count += min(remainder - power + 1, power)

            power *= 10

        return count