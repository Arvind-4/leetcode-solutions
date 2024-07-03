// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = set()
        for i in range(len(nums)):
            if nums[i] == 0: continue
            if nums[i] in l: continue

            l.add(nums[i])
        return len(l)

        