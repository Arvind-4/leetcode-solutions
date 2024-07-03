// https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return 1

        left = 0
        right = int(c ** 0.5) + 1

        print(left, right)

        while left <= right:
            _sum = (left ** 2) + (right ** 2)
            if _sum == c:
                return 1
            elif _sum > c:
                right -= 1
            else:
                left += 1
        return 0
            
        