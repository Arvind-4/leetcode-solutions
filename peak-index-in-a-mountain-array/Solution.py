// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        index = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                index = i + 1

        return index