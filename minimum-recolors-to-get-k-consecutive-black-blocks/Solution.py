// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n, minn = len(blocks), math.inf
        for i in range(n - k + 1):
            whites = blocks.count("W", i, i + k)
            minn = min(whites, minn)
        return minn