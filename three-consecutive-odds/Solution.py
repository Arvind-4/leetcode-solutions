// https://leetcode.com/problems/three-consecutive-odds

class Solution:
    def returnOdd(self, num: int) -> bool:
        if num % 2 != 0: return True
        return False
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if all([
                self.returnOdd(arr[i]),
                self.returnOdd(arr[i + 1]),
                self.returnOdd(arr[i + 2]),
            ]): return 1
        return 0
        