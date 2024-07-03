// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        for num in nums:
            if num in nums and (-1 * num) in nums:
                ans = max(ans, abs(num))
        return ans
        