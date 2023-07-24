// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count1, flag1 = 0, 0
        count0, flag0 = 0, 0
        for i in range(len(s)):
            if s[i] == "1":
                count1 += 1
                if count1 > flag1:
                    flag1 = count1
            else:
                count1 = 0

        for i in range(len(s)):
            if s[i] == "0":
                count0 += 1
                if count0 > flag0:
                    flag0 = count0
            else:
                count0 = 0
        return flag1 > flag0