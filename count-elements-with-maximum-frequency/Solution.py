// https://leetcode.com/problems/count-elements-with-maximum-frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101
        maxf = 0
        for num in nums:
            freq[num] += 1
            maxf = max(maxf, freq[num])

        ans = 0
        for i in freq:
            if i == maxf:
                ans += i
        return ans      