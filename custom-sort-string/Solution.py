// https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in order:
            if i in d:
                result += i * d[i]
                del d[i]
        for k, v in d.items():
            result += k * v
        return result