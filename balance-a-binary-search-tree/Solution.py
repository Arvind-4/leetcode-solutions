// https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, node: TreeNode) -> List[int]:
        if not node: return []
        return self.inOrderTraversal(node.left) + [node.val] + self.inOrderTraversal(node.right)

    def buildBalancedBST(self, elements: List[int]) -> TreeNode:
        if not elements: return None
        mid = len(elements) // 2
        node = TreeNode(elements[mid])
        node.left = self.buildBalancedBST(elements[:mid])
        node.right = self.buildBalancedBST(elements[mid + 1:])
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        elements = self.inOrderTraversal(root)
        return self.buildBalancedBST(elements)

        