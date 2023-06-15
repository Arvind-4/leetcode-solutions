// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftNode(self, root: Optional[TreeNode], isLeft):
        if not root: return 0
        if not root.left and not root.right and isLeft:  return root.val
        
        leftSum = self.leftNode(root.left, True)
        rightSum = self.leftNode(root.right, False)
        return leftSum + rightSum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftNode(root, False)
