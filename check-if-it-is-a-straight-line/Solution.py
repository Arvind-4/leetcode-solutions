// https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        dx = x1 - x0
        dy = y1 - y0
        for x, y in coordinates:
            if dx * (y - y1) != dy * (x - x1):
                return 0
        return 1