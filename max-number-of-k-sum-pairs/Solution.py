// https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer, l, r = 0, 0, len(nums) - 1
        while l < r:
            val = nums[l] + nums[r]
            if val <= k: l += 1
            if val >= k: r -= 1
            if val == k: answer += 1
        return answer
