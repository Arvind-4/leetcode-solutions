// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        minn = min(len(word1), len(word2))
        maxx = max(len(word1), len(word2))

        for i in range(minn):
            result += word1[i]
            result += word2[i]
        if len(word1) > len(word2):
            result += word1[minn:]
        else:
            result += word2[minn:]
        return result