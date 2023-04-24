// https://leetcode.com/problems/find-the-maximum-divisibility-score

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        c = 0
        ans = 0

        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    count += 1
            if count > c:
                ans = divisors[i]
                c = count
            if count == c:
                if ans == 0:
                    ans = divisors[i]
                ans = min(ans, divisors[i])

        return ans
