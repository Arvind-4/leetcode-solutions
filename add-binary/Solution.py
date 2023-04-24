// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        s = []

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(carry % 2)
            carry //= 2
        string = ''
        for i in s[::-1]:
            string += str(i)


        return string
