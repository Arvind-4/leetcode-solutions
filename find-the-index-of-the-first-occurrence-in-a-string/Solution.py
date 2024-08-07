// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)

        for i in range(lh - ln + 1):
            if haystack[i: i + ln] == needle:
                return i
        return -1
        