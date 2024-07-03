// https://leetcode.com/problems/beautiful-towers-ii

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        leftSum = 0

        stack = [-1]

        for i in range(n):
            while len(stack) > 1 and maxHeights[i] < maxHeights[stack[-1]]:
                j = stack.pop()
                leftSum -= (j - stack[-1]) * maxHeights[j]                
            leftSum += maxHeights[i] * (i - stack[-1])
            stack.append(i)
            left[i] = leftSum

        right = [0] * n
        rightSum = 0

        stack = [n]

        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                rightSum -= (j - stack[-1]) *  maxHeights[j]
            rightSum += maxHeights[i] * (i - stack[-1])
            stack.append(i)
            right[i] = -1 * rightSum

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i])

        return ans