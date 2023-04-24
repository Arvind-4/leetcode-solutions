// https://leetcode.com/problems/convert-to-base-2

class Solution:
    def baseNeg2(self, n: int) -> str:
        string = ""
        if n == 0: return string + "0"

        while n != 0:
            if n % 2 != 0:
                string += "1"
                n = int((n - 1) / -2)
            else:
                string += "0"
                n = int(n / -2)

        return string[::-1]


        