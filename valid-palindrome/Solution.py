// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        string = ""
        for i in range(n):
            if s[i].isalnum():
                string += s[i].lower()
        m = len(string)
        for j in range(m):
            print("string[j]", string[j])
            print("string[m - j - 1]", string[m - j - 1])
            if string[j] != string[m - j - 1]:
                return False
        return True