// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles

class Solution:
    def interchangeableRectangles(self, arr: List[List[int]]) -> int:
        d = {}
        answer = 0
        for w, h in arr:
            ratio = w / h
            if ratio in d and d[ratio] == 1:
                answer += 1
            elif ratio in d:
                answer += (d[ratio])
            d[ratio] = d.get(ratio, 0) + 1

        return answer