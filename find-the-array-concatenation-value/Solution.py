// https://leetcode.com/problems/find-the-array-concatenation-value

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = []
        limit = 0
        if len(nums) % 2 == 0: limit = len(nums) // 2
        else: limit = (len(nums) // 2) + 1

        for i in range(len(nums)):
            if i < limit:
                if i == limit - 1 and len(nums) % 2 != 0:
                    num = str(nums[i])
                else:
                    num = str(nums[i]) + str(nums[-(i + 1)])
                l.append(num)

        print(l)
        l = [int(i) for i in l]

        return sum(l)




