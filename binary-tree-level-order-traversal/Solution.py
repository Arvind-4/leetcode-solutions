// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        levels = []
        queue = [root]
        while queue:
            n = len(queue)
            curr_level = []
            for _ in range(n):
                first = queue.pop(0)
                curr_level.append(first.val)
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)
            levels.append(curr_level)
        return levels

        