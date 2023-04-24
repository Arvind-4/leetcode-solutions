// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        nonAlphaNumberic = """`~!@#$%^&*()_-+=[]|\{}:;'",./?"""

        newS = ""
        for i in s:
            if i not in nonAlphaNumberic and i != " ":
                newS += i.lower()

        print(newS)
        if newS == newS[::-1]:
            return True
        return False
        
        