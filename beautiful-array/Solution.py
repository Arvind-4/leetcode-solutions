// https://leetcode.com/problems/beautiful-array

class Solution:
    def recurseFunction(self, arr: List[int]):
        if len(arr) <= 2:
            return arr
        return self.recurseFunction(arr[::2]) + self.recurseFunction(arr[1::2])

    def beautifulArray(self, n: int) -> List[int]:
        return self.recurseFunction([i for i in range(1, n + 1)])


        