// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}

        for i in range(len(nums)):
            for j in nums[i]:
                if j not in d: d[j] = 1
                else: d[j] += 1

        answer = []

        for key, value in d.items():
            if value == len(nums):
                answer.append(key)

        return sorted(answer)