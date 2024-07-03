// https://leetcode.com/problems/rank-transform-of-an-array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        result = []
        d = {}
        l = arr.copy()
        l.sort()
        i = 1

        for el in l:
            if el not in d:
                d[el] = i
                i += 1
        
        for j in arr:
            result.append(d[j])
        return result


        