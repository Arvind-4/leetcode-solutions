// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, nums[n - 1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            j, i = 0, 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    j += 1
                    i += 1
                i += 1
            if j >= p: r = mid
            else: l = mid + 1
        return l