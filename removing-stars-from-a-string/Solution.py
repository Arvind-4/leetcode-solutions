// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)