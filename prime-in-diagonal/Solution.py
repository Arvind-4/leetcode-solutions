// https://leetcode.com/problems/prime-in-diagonal

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def isPrime(number: int) -> bool:
            if number == 1: return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0: return False
            return True

        l = []
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if (i == j or i + j == len(nums[i]) - 1):
                    if isPrime(nums[i][j]):
                        answer = max(answer, nums[i][j])
        return answer