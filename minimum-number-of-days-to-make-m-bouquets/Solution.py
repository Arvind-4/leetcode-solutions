// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            consecutive_length, bouquets = 0, 0
            for bloom in bloomDay:
                if bloom <= mid:
                    consecutive_length += 1
                    if consecutive_length >= k:
                        consecutive_length = 0
                        bouquets += 1
                else:
                    consecutive_length = 0
            if bouquets >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans