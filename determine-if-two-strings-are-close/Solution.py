// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = {}, {}

        if len(word1) != len(word2):
            return 0
        count1 = Counter(word1)
        count2 = Counter(word2)

        c1 = sorted(count1.keys()) == sorted(count2.keys())
        c2 = sorted(count1.values()) == sorted(count2.values())
        
        return c1 and c2