// https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        result = 0
        while amount[1] and amount[2]:
            result += 1
            amount[1] -= 1
            amount[2] -= 1
            amount.sort()

        result += amount[2]

        return result
        