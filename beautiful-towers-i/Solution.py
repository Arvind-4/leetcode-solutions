// https://leetcode.com/problems/beautiful-towers-i

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            heights = [0] * n
            l = i - 1
            h = i + 1
            heights[i] = maxHeights[i]
            while l >= 0:
                if maxHeights[l] <= heights[l + 1]:
                    heights[l] = maxHeights[l]
                else:
                    heights[l] = heights[l + 1]
                l -= 1
            while h < n:
                if maxHeights[h] <= heights[h - 1]:
                    heights[h] = maxHeights[h]
                else:
                    heights[h] = heights[h - 1]
                h += 1
            summ = 0
            for su in heights:
                summ += su
            ans = max(ans, summ)

        return ans


 


