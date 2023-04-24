// https://leetcode.com/problems/get-maximum-in-generated-array

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l = [0 for i in range(n + 1)]
        for i in range(n + 1):
            if i == 0: l[i] = 0
            if i == 1: l[i] = 1
            if 2 <= 2 * i <= n: 
                l[2 * i] = l[i] 
            if 2 <= 2 * i + 1 <= n: 
                l[2 * i + 1] = l[i] + l[i + 1]
        return max(l)