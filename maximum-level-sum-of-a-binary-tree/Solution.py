// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [root]
        maxLevel = root.val
        maxSum = root.val
        level = 1

        while queue:
            levelSum = 0
            nextLevel = []

            for node in queue:
                levelSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            queue = nextLevel
            level += 1

        return maxLevel


