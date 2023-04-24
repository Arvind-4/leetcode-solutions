// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for i in s:
            if i in brackets.keys():
                res.append(brackets[i])

            elif not res or res[-1] != i:
                return False
            else:
                res.pop()
        return len(res) == 0
            