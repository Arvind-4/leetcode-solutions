// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)
        d = {}
        for i in range(n):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        l = list(d.values())
        n1 = len(l)
        n2 = len(set(l))

        return n1 == n2