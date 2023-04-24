// https://leetcode.com/problems/greatest-common-divisor-of-strings

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            x = str1[:math.gcd(len(str1), len(str2))]
        else:
            x = ""
        
        return x
        
            