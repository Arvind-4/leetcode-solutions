// https://leetcode.com/problems/number-of-common-factors

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        la, lb = [], []
        for i in range(1, a + 1):
            if a % i == 0:
                la.append(i)

        for i in range(1, b + 1):
            if b % i == 0:
                lb.append(i)

        count = 0

        if len(la) > len(lb):
            for i in la:
                if i in lb:
                    count += 1

        else:
            for i in lb:
                if i in la:
                    count += 1

        return count