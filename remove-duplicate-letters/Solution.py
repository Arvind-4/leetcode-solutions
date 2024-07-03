// https://leetcode.com/problems/remove-duplicate-letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        n = len(s)
        d = {}

        for i in range(n):
            d[s[i]] = i
        
        stack = []
        for i in range(n):
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and d[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
        