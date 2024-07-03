// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        currentSum = sum(nums) 
        i = 0
        while i < n and nums[i] < 0 and k > 0:
            currentSum += 2 * abs(nums[i])
            i += 1
            k -= 1

        if i == n and k % 2 == 0:
            return currentSum
        
        elif i == n and k % 2 == 1:
            currentSum -= 2 * abs(nums[-1])
            return currentSum
        if nums[i] == 0 or k % 2 == 0:
            return currentSum
        
        if i > 0:
            currentSum -= 2 * min(
                abs(nums[i]), 
                abs(nums[i - 1])
            )
        else:
            currentSum -= 2 * nums[0]
        
        return currentSum