// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None: 
            return []

        l = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node.children:
                for child in node.children:
                    stack.append(child)

            l.append(node.val)
        return l[::-1]