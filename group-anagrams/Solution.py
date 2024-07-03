// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            f = str(sorted(s))
            if f not in  d:
                d[f] = []
            d[f].append(s)
        return d.values()