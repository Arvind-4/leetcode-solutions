// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        l = []
        for k, v in d.items():
            if v > 1:
                l.append(k)
        return l