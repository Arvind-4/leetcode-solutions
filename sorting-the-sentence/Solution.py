// https://leetcode.com/problems/sorting-the-sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        l = ""
        for i in s.split():
            d[i[-1]] = i[:-1]
        for k, v in dict(sorted(d.items())).items():
            l += v + " "
        return l.strip()