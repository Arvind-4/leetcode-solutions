// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == "x":
                    xy += 1
                else: yx += 1

        if (xy + yx) % 2 == 1:
            return -1
        res = xy // 2
        res += yx // 2
        if xy % 2 == 1: res += 2

        return res