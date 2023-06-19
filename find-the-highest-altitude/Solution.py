// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight, currentHeight = 0, 0
        for g in gain:
            currentHeight += g
            maxHeight = max(currentHeight, maxHeight)
        return maxHeight