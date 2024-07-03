// https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                if d[5] > 0:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return 0
            else:
                if d[5] > 0 and d[10] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return 0
        return 1
        