// https://leetcode.com/problems/best-sightseeing-pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxVal = 0
        current = 0
        for i in range(1, len(values)):
            current = max(current, values[i - 1] + i - 1)
            maxVal = max(maxVal, current + values[i] - i)
        return maxVal

