// https://leetcode.com/problems/ugly-number-ii

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [0] * n
        l[0] = 1
        x = y = z = 0
        for i in range(1, n):
            l[i] = min(
                l[x] * 2, 
                l[y] * 3, 
                l[z] * 5
            )
            if l[x] * 2 == l[i]:
                x += 1
            if l[y] * 3 == l[i]: 
                y += 1
            if l[z] * 5 == l[i]:
                z += 1
        return l[n-1]
            