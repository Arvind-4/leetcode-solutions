// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # l = []

        # for i in nums:
        #     if i not in l: 
        #         l.append(i)

        # print(l)
        # for i in range(len(l)):
        #     for j in range(i + 1, len(l)):
        #         for k in range(j + 1, len(l)):
        #             if i < j < k and l[i] < l[j] < l[k]:
        #                 return True 
        # return False

        first, second = float("inf"), float("inf")

        for third in nums:
            if third <= first:
                first = third
            elif third <= second:
                second = third
            else: return True

        return False