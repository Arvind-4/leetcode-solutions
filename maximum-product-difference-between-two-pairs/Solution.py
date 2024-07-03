// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1, min2, *args, max2, max1 = sorted(nums)
        return (max1 * max2) - (min2 * min1)