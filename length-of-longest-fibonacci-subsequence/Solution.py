// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        longest = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                length = 2

                while a + b in nums:
                    a, b = b, a + b
                    length += 1
                if length > 2 and length > longest: longest = length
        return longest