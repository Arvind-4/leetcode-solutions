// https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = 0
        curr = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                pre = curr
                curr = 1

            if pre >= curr:
                count += 1
        return count        