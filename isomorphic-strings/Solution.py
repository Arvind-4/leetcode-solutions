// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0

        st, ts = {}, {}

        for i in range(len(s)):
            if s[i] in st:
                if st[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ts:
                    return False

                st[s[i]] = t[i]
                ts[t[i]] = s[i]

        return True