// https://leetcode.com/problems/find-the-divisibility-array-of-a-string

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        l = []
        num = 0
        for i in word:
            num = num * 10 + int(i)
            if num % m == 0: l.append(1)
            else: l.append(0)

            num = num % m
        return l