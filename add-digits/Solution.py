// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:

        if num < 10: return num

        while num > 0:
            temp = 0
            while num > 0:
                digit = num % 10
                temp += digit
                num //= 10
            num = temp

            if num < 10: return num        
        return 0
