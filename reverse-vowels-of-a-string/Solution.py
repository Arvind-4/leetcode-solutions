// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU" :
                l.append(i)
        for i in range(len(l) // 2):
            s[l[i]], s[l[-i - 1]] = s[l[-i - 1]], s[l[i]]
        return "".join(s)
                
            