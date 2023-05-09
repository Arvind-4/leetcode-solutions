// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while n > 0:
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit ** 2
                n //= 10

            if temp in used: return False
            else: used.append(temp)


            if temp == 1: return True

            n = temp

        return False
