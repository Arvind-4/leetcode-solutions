// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        if len(l) > 0: return [l[0], l[-1]]
        return [-1, -1]

        