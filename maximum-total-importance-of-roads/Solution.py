// https://leetcode.com/problems/maximum-total-importance-of-roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        res = 0
        label = 1

        for n1, n2 in roads:
            count[n1] += 1
            count[n2] += 1
        
        for i in sorted(count):
            res += label * i
            label += 1
        return res