// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxx = 0
        
    def dfs(self, node: Optional[TreeNode], left: int, right: int):
        self.maxx = max(self.maxx, left, right)
        if node.left:
            self.dfs(node.left, right + 1, 0)
        if node.right:
            self.dfs(node.right, 0, left + 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, 0)
        return self.maxx
