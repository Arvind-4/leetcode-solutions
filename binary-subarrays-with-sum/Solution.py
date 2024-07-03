// https://leetcode.com/problems/binary-subarrays-with-sum

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        summ = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in summ:
                count += summ[prefix_sum - goal]
            summ[prefix_sum] = summ.get(prefix_sum, 0) + 1
        return count