// https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1l, nums2l = [], []

        for i in nums1:
            if i not in nums2:
                nums1l.append(i)

        for i in nums2:
            if i not in nums1:
                nums2l.append(i)

        nums1l = list(set(nums1l))
        nums2l = list(set(nums2l))
        return [nums1l, nums2l]

                