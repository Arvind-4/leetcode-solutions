// https://leetcode.com/problems/closest-prime-numbers-in-range

import math

class Solution:

    def isPrime(self, num: int) -> bool:
        if num < 2: return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:

        minn = float("inf")
        queue = []
        answer = [-1, -1]

        for i in range(left, right + 1):
            if self.isPrime(i): queue.append(i)

            while len(queue) >= 2:
                if abs(queue[0] - queue[1]) < minn:
                    answer = [queue[0], queue[1]]

                    diff = abs(queue[0] - queue[1])

                    if diff <= 2: return answer     
                queue.pop(0)
        return answer