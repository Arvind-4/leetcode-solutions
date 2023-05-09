// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        truth = [True] * n 
        truth[0], truth[1] = False, False 
        
        i = 2
        
        
        while i * i < n: 
            if truth[i] == True:
                for j in range(i*i,n,i): 
                    truth[j] = False
            i += 1
        return sum(truth)