// https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, equal, larger = [], [], []

        for i in range(len(nums)):
            if nums[i] < pivot: smaller.append(nums[i])
            if nums[i] == pivot: equal.append(nums[i])
            if nums[i] > pivot: larger.append(nums[i])

        return smaller + equal + larger