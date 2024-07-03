// https://leetcode.com/problems/richest-customer-wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        maxx = 0
        for i in range(n):
            maxx = max(maxx, sum(accounts[i]))

        return maxx
        