// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}

        for i in text:
            if i in "balloon":
                if i in d: d[i] += 1
                else: d[i] = 1
        print(d)
        countb = d.get("b", 0)
        counta = d.get("a", 0)
        countl = d.get("l", 0) // 2
        counto = d.get("o", 0) // 2
        countn = d.get("n", 0)

        return min(countb, counta, countl, counto, countn)




        return 2