// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int: 
        ans = 0
        n = len(seats)
        for i in range(n):
            _min1 = min(seats)
            _min2 = min(students)
            ans += abs(_min1 - _min2)
            seats.remove(_min1)
            students.remove(_min2)

        return ans
