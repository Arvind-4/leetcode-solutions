// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        n = len(temps)
        res = [0] * n

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
            