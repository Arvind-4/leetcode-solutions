// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minn = min(len(word1), len(word2))
        s = ""

        j = 0
        for i in range(minn):
            s += word1[i]
            s += word2[i]

        if len(word1) > len(word2):
            s += word1[minn:]
        else:
            s += word2[minn:]



        return s