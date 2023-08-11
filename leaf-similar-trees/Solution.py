// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        def traverse(node, treearr):
            if node:
                traverse(node.left, treearr)
                if not node.left and not node.right:
                    treearr.append(node.val)
                traverse(node.right, treearr)
        traverse(root1, tree1)
        traverse(root2, tree2)
        if(tree1 == tree2):
            return True
        else:
            return False


