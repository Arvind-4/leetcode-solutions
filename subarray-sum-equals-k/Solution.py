// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, n, preSum, dic = 0, len(nums), 0, {}

        dic[0] = 1

        for num in nums:
            preSum += num
            if preSum - k in dic:
                ans += dic[preSum - k]

            dic[preSum] = dic.get(preSum, 0) + 1

        print(ans) 

        

        return ans
