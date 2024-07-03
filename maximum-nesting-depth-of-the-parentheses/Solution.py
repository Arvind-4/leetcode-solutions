// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        mx = 0
        for sy in s:
            if sy == "(":
                stack.append(sy)
            elif sy == ")":
                mx = max(mx, len(stack))
                stack.pop()
            
        return mx