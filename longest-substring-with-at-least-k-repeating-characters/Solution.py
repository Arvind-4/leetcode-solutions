// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
            
        f = self.longestSubstring
        d = collections.Counter(s)
        for character, occurrence in d.items():
            if occurrence < k:
                return max(f(sub_string, k) for sub_string in s.split(character))
        return len(s)