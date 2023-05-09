// https://leetcode.com/problems/alternating-digit-sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sumOdd, sumEven, j = 0, 0, 0
        for i in str(n):         
            if j % 2 == 0:
                sumEven += int(i)
            else:
                sumOdd += int(i)
            j += 1


        return sumEven - sumOdd