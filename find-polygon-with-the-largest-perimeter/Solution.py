// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        _sum = nums[0] + nums[1]
        for num in nums[2:]:
            if _sum > num:
                res = _sum + num
            _sum += num
        if res == 0: return -1
        return res
