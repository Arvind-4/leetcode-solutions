// https://leetcode.com/problems/divisor-game

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0: return 1
        return 0