// https://leetcode.com/problems/super-pow

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        maxel = ''.join(map(str, b))
        return pow(a, int(maxel), 1337)