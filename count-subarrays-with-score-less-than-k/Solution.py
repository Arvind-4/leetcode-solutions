// https://leetcode.com/problems/count-subarrays-with-score-less-than-k

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # l = [[]]
        # count = 0
        # l = [nums[j:i] for i in range(len(nums)+1) for j in range(i)]
        # for i in range(len(l)):
        #         if len(l[i]) > 0 and sum(l[i]) * len(l[i]) < k: count += 1


        # return count

        left, right, valid, windowSum = 0, 0, 0, 0

        while right < len(nums):
            windowSum += nums[right]
            right += 1

            while left < right and windowSum * (right - left) >= k:
                windowSum -= nums[left]
                left += 1

            valid += right - left

        return valid
