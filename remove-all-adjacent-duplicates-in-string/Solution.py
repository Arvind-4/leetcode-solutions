// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = [s[0]]
        n = len(s)
        for i in range(1, n):
            if len(l) == 0 or l[len(l) - 1] != s[i]:
                l.append(s[i])
            else:
                l = l[:len(l) - 1]
        return "".join(l)
        