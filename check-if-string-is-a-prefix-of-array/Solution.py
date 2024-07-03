// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        string = ""
        for word in words:
            string += word
            if string == s:
                return 1

        return 0
        