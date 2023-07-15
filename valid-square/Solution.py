// https://leetcode.com/problems/valid-square

class Solution:
    def dist(self, a: List[int], b: List[int]):
        return ((a[0]- b[0])**2 + (a[1] - b[1])**2) ** 0.5

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d1 = self.dist(p1, p2)
        d2 = self.dist(p1, p3)
        d3 = self.dist(p1, p4)
        d4 = self.dist(p2, p3)
        d5 = self.dist(p2, p4)
        d6 = self.dist(p3, p4)

        l = [d1, d2, d3, d4, d5, d6]

        maxVal = max(l)
        minVal = min(l)
        maxCount, minCount= 0, 0

        for i in l:
            if i == maxVal:
                maxCount += 1
            elif i == minVal:
                minCount += 1
        print(minCount, maxCount)
        if minCount == 4 and maxCount == 2:
            return True
        return False