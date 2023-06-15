// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n)[2:])
        count = 0
        for i in bin(n)[2:]:
            if i == "1":
                count += 1

        print("count", count)
        return count