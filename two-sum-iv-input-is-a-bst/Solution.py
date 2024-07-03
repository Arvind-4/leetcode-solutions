// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node: Optional[TreeNode], nums: List[int]) -> None:
        if not node:
            return 
        self.inOrder(node.left, nums)
        nums.append(node.val)
        self.inOrder(node.right, nums)
        return nums

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = self.inOrder(root, [])

        l, r = 0, len(nums) - 1

        while l < r:
            summ = nums[l] + nums[r]
            if summ == k:
                return 1
            elif summ < k:
                l += 1
            else:
                r -= 1
        return 0