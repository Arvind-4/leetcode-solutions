// https://leetcode.com/problems/left-and-right-sum-differences

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i]) - sum(nums[i + 1:])) for i in range(len(nums))]
