// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def bubbleSort(self, array: List[int]) -> List[int]:
        n = len(array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        self.bubbleSort(arr) 
        el = set()       
        for i in range(len(arr) - 1):
            el.add(abs(arr[i] - arr[i + 1]))
        if len(el) == 1: return 1
        return 0
