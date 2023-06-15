// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        string = []
        for i in s.split():
            string.append(i[::-1])
        print(string)
        return " ".join(string)