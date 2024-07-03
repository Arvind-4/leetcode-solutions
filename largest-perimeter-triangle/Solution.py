// https://leetcode.com/problems/largest-perimeter-triangle

class Solution:
    def valid(self, a: int, b: int, c: int):
        if (a + b) > c and (b + c) > a and (c + a) > b:
            return True, a + b +c
        return False, 0
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        for i in range(n - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0
        

