// https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        remaining = []
        result = []

        for num in arr2:
            d[num] = 0
        
        for num in arr1:
            if num in d: d[num] = d.get(num, 0) + 1
            else: remaining.append(num)
        
        print("d", d)
        print("remaining", remaining)

        for num in arr2:
            result += [num] * d.get(num)
        print("result", result)
        return result + sorted(remaining)