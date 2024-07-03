// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:                
            if ch in "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif ch in "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif ch in "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif ch in "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            else:
                stack.append(int(ch))
        return stack[0]
        