// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ans(self, root: Optional[TreeNode], stack: List[int]) -> None:
        if root == None:
            return stack
        else:
            stack.append(root.val)
            self.ans(root.left, stack)
            self.ans(root.right, stack)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.ans(root, stack)
        return stack      