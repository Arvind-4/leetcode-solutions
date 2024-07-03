// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l, prod = 0, 1

        for r, num in enumerate(nums):
            prod *= num

            while prod >= k and l <= r:
                prod //= nums[l]
                l += 1
            count += r - l + 1
        return count