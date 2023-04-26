// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ''
        for indexi, i in enumerate(s):
            for indexj, j in enumerate(s[indexi:], start=indexi):
                if i == j and s[indexi: indexj + 1] == s[indexi: indexj + 1][::-1] and len(s[indexi: indexj + 1]) > len(substring):
                    substring = s[indexi: indexj + 1]

        return substring
                    