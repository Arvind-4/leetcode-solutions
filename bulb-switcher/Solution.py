// https://leetcode.com/problems/bulb-switcher

class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        return int(n ** 0.5)
        


