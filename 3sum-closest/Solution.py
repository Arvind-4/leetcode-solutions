// https://leetcode.com/problems/3sum-closest

import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0
        diff = math.inf

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                summ = nums[i] + nums[j] + nums[k]

                if abs(target - summ) < diff:
                    diff = abs(target - summ)
                    answer = summ
                elif summ < target: j +=1 
                else: k -= 1
        return answer