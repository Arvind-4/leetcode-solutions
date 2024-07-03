// https://leetcode.com/problems/magical-string

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [3 - s[-1]] * s[i]
            i += 1

        c = s[:n].count(1)
        return c
