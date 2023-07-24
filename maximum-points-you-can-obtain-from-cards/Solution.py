// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum = [0], [0]
        n = len(cardPoints)

        for i in range(k):
            lsum.append(cardPoints[i] + lsum[-1])
            rsum.append(cardPoints[n - i - 1] + rsum[-1])

        maxScore = 0
        for i in range(k + 1):
            score = lsum[i] + rsum[k - i]
            maxScore = max(maxScore, score)

        return maxScore