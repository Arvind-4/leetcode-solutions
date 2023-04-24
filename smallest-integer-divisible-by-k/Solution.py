// https://leetcode.com/problems/smallest-integer-divisible-by-k

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5: return -1

        n, length = 1, 1

        while 1:
            if not n % k: return length
            length += 1
            n = (n * 10) + 1