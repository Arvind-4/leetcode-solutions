// https://leetcode.com/problems/split-with-minimum-sum

class Solution:
    def splitNum(self, num: int) -> int:
        num1 = ""
        num2 = ""

        l = list(map(int, str(num)))
        l.sort()

        for i in range(len(l)):
            if i % 2 == 0:
                num1 += str(l[i])
            else:
                num2 += str(l[i])
        return int(num1) + int(num2)