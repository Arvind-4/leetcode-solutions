// https://leetcode.com/problems/count-integers-with-even-digit-sum

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            summ = sum(list(map(int, str(i))))
            if summ % 2 == 0: count += 1

    
        return count