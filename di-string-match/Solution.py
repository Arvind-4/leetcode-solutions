// https://leetcode.com/problems/di-string-match

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l, r = 0, len(s)

        for i in s:
            if i == "I":
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1

        if s[-1] == "D":
            res.append(l)
        else:
            res.append(r)

        return res

        