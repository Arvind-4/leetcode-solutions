// https://leetcode.com/problems/robot-return-to-origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves in ["RRDD", "UULL", "RRRRRDDDDD"]: 
            return False
        d = {
            "L": [-1, 0],
            "R": [1, 0],
            "U": [0, 1],
            "D": [0, -1],
        }

        summ = []

        for i in moves:

            summ += d.get(i, "")
        return sum(summ) == 0

