// https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) > len(t):
            for i in s:
                if s.count(i) > t.count(i): return i
        else:
            for i in t:
                if t.count(i) > s.count(i): return i