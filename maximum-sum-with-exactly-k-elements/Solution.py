// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)
        maxx = max(nums)
        for _ in range(k):
            for i in range(n):
                if nums[i] == maxx:
                    total += nums[i]
                    nums[i] = nums[i] + 1
                    maxx = nums[i]
        return total