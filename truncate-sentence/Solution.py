// https://leetcode.com/problems/truncate-sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        new = s.split()[:k]
        return " ".join(new)
        