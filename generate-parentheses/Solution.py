// https://leetcode.com/problems/generate-parentheses

class Solution:
    def backtracking(self,n: int, opened: int, closed: int, result: List[int], current: List[int]) -> List[int]:
        if opened == closed == n:
            return result.append("".join(current))

        if opened < n:
            current.append("(")
            self.backtracking(n, opened + 1, closed, result, current)
            current.pop()

        if closed < opened:
            current.append(")")
            self.backtracking(n, opened, closed + 1, result, current)
            current.pop()

        return result

    def generateParenthesis(self, n: int) -> List[str]:
        closed, opened = 0, 0
        current = []
        result = []

        return self.backtracking(n, opened, closed, result, current)


    

        

        
