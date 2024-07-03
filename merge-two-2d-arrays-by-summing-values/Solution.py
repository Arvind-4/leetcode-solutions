// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

class Solution:
    import itertools
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        maxx = max(len(nums1), len(nums2))
        minn = min(len(nums1), len(nums2))
        l = [0] * 1001
        for idx, val in nums1:
            l[idx] += val
        for idx, val in nums2:
            l[idx] += val
        return [[a,b] for a,b in enumerate(l) if b != 0]  