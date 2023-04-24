// https://leetcode.com/problems/most-frequent-even-element

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # if len(nums) <= 1: return nums[0]
        d, max_, key = {}, 0, -1
        for i in nums:
            if i % 2 == 0:
                if i not in d: d[i] = 1
                else: d[i] += 1

        for k, v in d.items():
            if v > max_:
                max_, key = v, k
            elif v == max_:
                key = min(k,key)
        # if nums == [1]: return 
        return key