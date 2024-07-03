// https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        j = 0
        _max = 0
        for i in range(len(worker)):
            while j < len(jobs) and jobs[j][0] <= worker[i]:
                _max = max(_max, jobs[j][1])
                j += 1
            ans += _max
        return ans