// https://leetcode.com/problems/sum-of-all-odd-length-subarrays

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                if len(arr[i: j]) % 2 != 0: ans += sum(arr[i:j])
        return ans