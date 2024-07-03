// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in s:
            if stack and i == stack[-1][0]:
                stack[-1][1] += 1

                if stack[-1][1] >= k:
                    stack.pop()
            else: stack.append([i, 1])
        
        ans = ""
        for ch, n in stack:
            ans += ch * n
        return ans
