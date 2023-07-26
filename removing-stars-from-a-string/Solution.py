// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        string = ""
        for i in range(len(s)):
            if s[i] != "*":
                string += s[i]
            else: 
                string = string[:len(string) - 1]

        return string