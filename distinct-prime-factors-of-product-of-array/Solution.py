// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array

import math

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        answer = []

        for i in range(len(nums)):
            root = int(math.sqrt(nums[i]))

            for primeNum in range(2, root + 1):
                if nums[i] % primeNum == 0:
                    answer.append(primeNum)
                
                    while nums[i] % primeNum == 0:
                        nums[i] = nums[i] // primeNum

            if nums[i] >= 2: 
                answer.append(nums[i])
        return len(set(answer))