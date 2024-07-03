// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(open: int, closed: int):
            if open == closed == n:
                return res.append("".join(stack))

            if open < n:
                stack.append("(")
                backtracking(open + 1, closed)
                stack.pop()
            
            if closed < open:
                stack.append(")")
                backtracking(open, closed + 1)
                stack.pop()
        
        backtracking(0, 0)
        return res