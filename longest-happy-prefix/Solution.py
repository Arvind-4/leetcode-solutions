// https://leetcode.com/problems/longest-happy-prefix

class Solution:
    def longestPrefix(self, s: str) -> str:
        ptr1, ptr2 = 0, len(s) - 1
        str1, str2 = "", ""
        string = 0
        while ptr2 != 0:
            str1 += s[ptr1]
            str2 = s[ptr2] + str2

            ptr2 -= 1
            ptr1 += 1
            if str2 == str1:
                string = str1
    
        if string != 0: return string
        return ""
        

    