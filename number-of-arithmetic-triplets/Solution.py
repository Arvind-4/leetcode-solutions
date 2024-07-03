// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)

        count = 0

        for num in nums:
            if (num + diff) in s and (num + diff + diff) in s:
                count += 1

        return count
