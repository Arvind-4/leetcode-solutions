// https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return 1
        l = 0
        r = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                if l == len(s):
                    return 1
            r += 1
        return 0
        