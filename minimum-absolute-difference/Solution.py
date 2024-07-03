// https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = []
        minn = float('inf')
        for x, y in zip(arr, arr[1:]):
            diff = y - x
            if diff < minn:
                minn = diff
                l = [(x, y)]
            elif diff == minn:
                l.append((x, y))
            
        return l