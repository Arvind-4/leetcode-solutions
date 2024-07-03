// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n - 1
        res = 0
        leftmax, rightmax = height[l], height[r]

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
        return res