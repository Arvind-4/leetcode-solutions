// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        for i in nums:
            if i in d:
                d[i] += 1
            else: d[i] = 1

        obj = sorted(d.items(), key= lambda x: x[1], reverse=True)

        for k, v in obj[:k]:
            result.append(k)

        


        return result