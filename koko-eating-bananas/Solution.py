// https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (right + left) // 2
            hours = 0
            
            for ba in piles:
                hours += math.ceil(ba / mid)
            
            if hours <= h:
                ans = min(ans, mid)

                right = mid - 1
            else:
                left = mid + 1
        return ans
        