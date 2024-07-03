// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i

class Solution:
    def check(self, arr: List[int]) -> bool:
        if len(arr) != len(set(arr)):
            return False
        arr_sort = sorted(arr)
        if arr != arr_sort:
            return False
        return True

    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0

        for i in range(n):
            for j in range(i+1,n+1):
                if self.check(nums[:i] + nums[j:]):
                    count += 1
        print(count)
        return count
            