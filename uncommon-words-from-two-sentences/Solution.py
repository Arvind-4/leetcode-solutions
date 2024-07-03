// https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l = []
        d = {}
        for word in s1.split():
            if word in d: d[word] += 1
            else: d[word] = 1
        for word in s2.split():
            if word in d: d[word] += 1
            else: d[word] = 1
        for k, v in d.items():
            if v == 1:
                l.append(k)
        return l