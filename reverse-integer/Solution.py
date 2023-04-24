// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0: num = str(x)[::-1]
        else: 
            sign = str(x)[0]
            number = str(x)[1:]
            num = sign + number[::-1]

        if int(num) in range((-2) ** 31, 2 ** 31):
            return int(num)
        return 0