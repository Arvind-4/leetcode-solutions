// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left, right, valid, windowProd = 0, 0, 0, 1

        while right < len(nums):
            windowProd *= nums[right]
            right += 1

            while left < right and windowProd >= k:
                windowProd /= nums[left]
                left += 1

            valid += right - left

        return valid
