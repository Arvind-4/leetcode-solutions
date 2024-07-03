// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx = []
        l = []
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                idx.append(i)
        
        print(idx)

        for i in range(n):
            for j in idx:
                if (abs(i - j) <= k) :
                    l.append(i)
                    break
        return sorted(l)