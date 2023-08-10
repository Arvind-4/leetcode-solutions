// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l = []
        for i in range(1, n + 1):
            if n % i == 0:
                l.append(i)

        print(l)
        if len(l) < k or n < k:
            return -1

    
        return l[k - 1]
