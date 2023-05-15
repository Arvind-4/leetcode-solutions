// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        l = [int(i) for i in str(num)]
        l.sort()
        return (l[1] * 10 + l[2]) + (l[0] * 10 + l[3])
        