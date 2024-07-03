// https://leetcode.com/problems/crawler-log-folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log != "./":
                if log != "../":
                    stack.append(log)
                else:
                    if stack: stack.pop()
        return len(stack)