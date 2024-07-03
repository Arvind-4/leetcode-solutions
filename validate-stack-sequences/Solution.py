// https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        n = len(pushed)

        for i in range(n):
            stack.append(pushed[i])

            while stack != [] and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return stack == []
