// https://leetcode.com/problems/count-good-meals

import math
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        answer = 0
        MOD = pow(10, 9) + 7

        for i in deliciousness:
            for j in range(22):
                sqr = pow(2, j)
                if (sqr - i) in count:
                    answer += count[(sqr - i)]
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        return answer % MOD
                