// https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative, j = [], [], 0
        for i in range(len(nums)):
            if nums[i] >= 0: positive.append(nums[i])
            else: negative.append(nums[i])

        for i in range(0, len(nums), 2):
            nums[i] = positive[j]
            nums[i + 1] = negative[j]
            j += 1

        print(nums)

        return nums

        