// https://leetcode.com/problems/simplified-fractions

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        d = {}
        l = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i <=j and j <= n and i != j:
                    if not (i / j) in d:
                        d[i / j] = f"{i}/{j}"
                        l.append(f"{i}/{j}")
        return l