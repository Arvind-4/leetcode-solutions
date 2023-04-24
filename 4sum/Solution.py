// https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_ == target:
                        res.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif sum_ > target: l -= 1
                    else: k += 1
        return list(res)