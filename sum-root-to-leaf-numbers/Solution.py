// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalSum = 0 
    def sumNumbersHelper(self, root: TreeNode, currentSum: int):
        if not root.left and not root.right:
            self.totalSum += currentSum * 10 + root.val
            return
        currentSum *= 10
        currentSum += root.val
        if root.left:
            self.sumNumbersHelper(root.left, currentSum)
        if root.right:
            self.sumNumbersHelper(root.right, currentSum)

    def sumNumbers(self, root: TreeNode) -> int:
        self.sumNumbersHelper(root, 0)
        return self.totalSum
        