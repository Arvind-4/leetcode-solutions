// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution:
    def partition(self, arr: List[int], low:int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr: List[int], low:int, high: int) -> List[int]:
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
        return arr


    def maximumProduct(self, nums: List[int]) -> int:
        arr = self.quickSort(nums, 0, len(nums) - 1)
        maxx = arr[-1] * arr[-2] * arr[-3]
        minn = arr[-1] * arr[0] * arr[1]
        return max(minn, maxx)