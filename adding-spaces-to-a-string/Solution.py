// https://leetcode.com/problems/adding-spaces-to-a-string

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        c = 0
        n = len(s)
        m = len(spaces)

        for i in range(n):
            if c < m and i == spaces[c]:
                string += " "
                c += 1
            string += s[i]
        return string