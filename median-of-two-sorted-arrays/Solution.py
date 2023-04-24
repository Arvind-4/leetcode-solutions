// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()


        if len(num) % 2 != 0:
            print(int(len(num) / 2))
            return num[(int(len(num) / 2))]
        else:
            return (num[(int(len(num) / 2))] + num[(int(len(num) / 2)) - 1]) / 2