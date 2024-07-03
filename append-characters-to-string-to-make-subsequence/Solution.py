// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        count = 0
        for i in s:
            if j == len(t):
                return 0
            if i == t[j]:
                j += 1
                count += 1
        
        return len(t) - count