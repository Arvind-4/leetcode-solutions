// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = []
        for i in s:
            if i not in l and s.count(i) == 1: 
                return s.find(i)
        return -1
        