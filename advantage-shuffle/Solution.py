// https://leetcode.com/problems/advantage-shuffle

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []
        n = len(nums1)
        for idx in range(n):
            heapq.heappush(li, (-nums2[idx], idx))
        nums1.sort()
        l, r = 0, len(nums1)-1
        res = [0 for _ in range(n)]
        for i in range(n):
            target, idx = heapq.heappop(li)
            target = -target
            if target >= nums1[r]:
                res[idx] = nums1[l]
                l += 1
            else:
                res[idx] = nums1[r]
                r -=1
        return res 


        