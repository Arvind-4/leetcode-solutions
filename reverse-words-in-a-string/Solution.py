// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        print(s.split()[::-1])

        return " ".join(s.split()[::-1])