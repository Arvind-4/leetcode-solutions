// https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = []
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            self.sum.append(prefix_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.sum[right] - self.sum[left - 1]
        return self.sum[left or right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
