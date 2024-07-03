// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        l = 0
        n = len(nums)
        for r in range(n):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if mp[nums[r]] > k:
                while nums[l] != nums[r]:
                    mp[nums[l]] -= 1
                    l += 1
                mp[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

        return count