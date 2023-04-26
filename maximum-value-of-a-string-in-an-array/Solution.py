// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array

import string

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        l = []
        for i in strs:
            if i.isnumeric(): l.append(int(i))
            else: l.append(len(i))
        return max(l)