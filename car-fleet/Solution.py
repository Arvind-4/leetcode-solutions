// https://leetcode.com/problems/car-fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - pos) / s for pos, s in sorted(zip(position, speed))]
        count = 0
        current = 0
        time.reverse()
        for t in time:
            if t > current:
                count += 1
                current = t
        return count