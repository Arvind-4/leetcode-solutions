// https://leetcode.com/problems/sum-of-digits-of-string-after-convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        string = ""
        for i in range(len(s)):
            string += str(ord(s[i]) - ord("a") + 1)

        for j in range(k):
            string = sum(list(map(int, str(string))))
        return int(string)