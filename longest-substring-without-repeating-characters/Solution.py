// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        maxx = 0
        for i in range(length, len(s) - length):
            p = s[length: i + 1]
            if(len(p) == len(set(p))):
                maxx = max(len(p), maxx)
            else:
                length += 1
        return maxx