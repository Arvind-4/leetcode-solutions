// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0
        for i in str(n):
            prod *= int(i)
            summ += int(i)

        
            

        return prod - summ