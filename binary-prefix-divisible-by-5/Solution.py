// https://leetcode.com/problems/binary-prefix-divisible-by-5

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = ""
        l = []
        for i in nums: s+= str(i)

        for i in range(len(s)):
            if int(s[:i + 1], 2) % 5 == 0:
                l.append(True)
            else: l.append(False)
        return l