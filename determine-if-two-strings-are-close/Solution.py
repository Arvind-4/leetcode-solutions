// https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = {}, {}
        if len(word1) != len(word2): return False

        for ch in word1:
            d1[ch] = d1.get(ch, 0) + 1
        
        for ch in word2:
            d2[ch] = d2.get(ch, 0) + 1
            
        c1 = sorted(d1.keys()) == sorted(d2.keys())
        c2 = sorted(d1.values()) == sorted(d2.values())

        return c1 and c2