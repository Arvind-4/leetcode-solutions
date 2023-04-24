// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        result = 0

        end = start = len(nums) - 1

        for i in range(len(nums)):
            for j in range(i + 1):
                if abs(nums[i] - nums[j]) == k:
                    result += 1
        return result