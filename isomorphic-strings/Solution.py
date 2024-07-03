// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0

        ds, dt = {}, {}

        for i in range(len(s)):
            if s[i] in ds:
                if ds[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dt:
                    return False

                ds[s[i]] = t[i]
                dt[t[i]] = s[i]

        return True