// https://leetcode.com/problems/maximum-odd-binary-number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        m = s.count('1') - 1
        answer = ['0'] * len(s)
        answer[-1] = '1'
        for i in range(m):
            answer[i] = '1'
        return ''.join(answer)