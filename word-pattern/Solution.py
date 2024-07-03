// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lp, ls = [], []

        slist = s.split()

        for i in pattern:
            lp.append(pattern.index(i))

        for j in slist:
            ls.append(slist.index(j))
        return lp == ls