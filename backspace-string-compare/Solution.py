// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def generate(self, string: str) -> str:
        newString = ""
        for i in range(len(string)):
            if string[i] != "#":
                newString += string[i]
            else:
                newString = newString[:len(newString) - 1]
        return newString

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.generate(s) == self.generate(t)