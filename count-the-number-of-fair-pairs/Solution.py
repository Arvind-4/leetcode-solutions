// https://leetcode.com/problems/count-the-number-of-fair-pairs

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer = 0
        result = 0

        start = end = len(nums) - 1

        for i in range(len(nums)):
            while end >= 0 and nums[i]+nums[end] > upper:
                end -= 1
                print("end", end)
            while start>=0 and nums[i]+nums[start]>=lower:
                start -= 1
                print("start", start)
            if(start < i and end >= i):
                result += end - start - 1 
            else:
                result += end - start

        print(result)
        return int(result / 2)