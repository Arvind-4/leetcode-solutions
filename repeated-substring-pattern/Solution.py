// https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                ss = s[:i]
                if ss * (n // i) == s:
                    return 1
        return 0