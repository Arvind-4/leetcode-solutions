// https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        track = 0
        ans = 0

        for num in nums:
            track = max(track, num)
            ans += track - num
            track += 1
        return ans