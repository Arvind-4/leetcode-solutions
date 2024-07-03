// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d: d[num] += 1
            else: d[num] = 1

        sort = sorted(d.items(), key= lambda x: x[1], reverse=True)
        l = []
        count = 1
        for k, v in sort[:k]:
            l.append(k)
        return l
        