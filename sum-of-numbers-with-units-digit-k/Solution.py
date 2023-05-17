// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if k % 2 == 0 and num % 2 != 0: return -1
        if num == 0: return 0
        elif k == 0 and num % 10 == 0: return 1
        elif k == 0: return -1

        i = 1

        while 1:
            if i * k > num:
                return -1
            if (i * k) % 10 == num % 10:
                return i

            i += 1

 