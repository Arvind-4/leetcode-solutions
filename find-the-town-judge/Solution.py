// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = [0] * n

        for i in trust:
            cnt[i[0] - 1] -= 1
            cnt[i[1] - 1] += 1

        for i in range(n):
            if cnt[i] == n - 1:
                return i + 1
                
        return -1