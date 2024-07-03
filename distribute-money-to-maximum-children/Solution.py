// https://leetcode.com/problems/distribute-money-to-maximum-children

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        money = money - children

        no8 = money // 7
        no1 = children - no8
        money %= 7

        if no1 < 0:
            return children - 1
        if (no1 == 1 and money == 3) or (no1 == 0 and money):
            no8 -= 1
        return no8

        