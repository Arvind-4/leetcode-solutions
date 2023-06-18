// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate

import math

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mindist = math.inf
        answer = -1
        count = 0
        for i, j in points:
            if x == i or y == j:
                d = abs(x - i) + abs(y - j)
                if d < mindist:
                    answer = count
                    mindist = d
            count += 1
        return answer