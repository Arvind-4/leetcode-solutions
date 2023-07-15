// https://leetcode.com/problems/edit-distance

class Solution:
    @lru_cache(None)
    def dp(self, i: int, j: int, w1: int, w2: int, word1: str, word2: str):
        if i >= w1: return w2 - j
        if j >= w2: return w1 - i
        if word1[i] == word2[j]:
            return self.dp(i + 1, j + 1, w1, w2, word1, word2)

        return min(
            self.dp(i, j + 1, w1, w2, word1, word2),
            self.dp(i + 1, j, w1, w2, word1, word2),
            self.dp(i + 1, j + 1, w1, w2, word1, word2)
        ) + 1
        
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)
        return self.dp(0, 0, w1, w2, word1, word2)
