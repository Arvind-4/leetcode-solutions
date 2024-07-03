// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num == 0:
                d[0] = d.get(0, 0) + 1
            elif num > 0:
                d[1] = d.get(1, 0) + 1
            elif num < 0:
                d[-1] = d.get(-1, 0) + 1
        
        if 0 in d:
            return 0
        
        for k, v in d.items():
            if k == -1:
                if v % 2 != 0:
                    return -1
        return 1
            