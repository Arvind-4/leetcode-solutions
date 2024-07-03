// https://leetcode.com/problems/longest-absolute-file-path

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        stack = []

        res = 0

        for line in lines:
            level = line.count("\t")
            if not stack:
                stack.append([level, len(line) - level])
            else:
                while stack and stack[-1][0] >= level:
                    stack.pop()
                offset = stack[-1][1] + 1 if stack else 0
                stack.append([level, offset + len(line) - level])
            if "." in line:
                res = max(res, stack[-1][1])

        return res
                


        return 1
        