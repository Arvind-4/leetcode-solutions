// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        visited = []
        for k, v in d.items():
            if v in visited:
                return 0
            visited.append(v)
        return 1