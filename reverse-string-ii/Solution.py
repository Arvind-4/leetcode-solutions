// https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count, string = 0, ""
        for i in range(0, len(s), k):
            if count % 2 == 0:
                string += s[i: i + k][::-1]
            else: string += s[i: i + k]
            count += 1
        return string