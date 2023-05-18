// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new = {}
        def depthFirstSearch(node: 'Node') -> 'Node':
            if node in new:
                return new[node]
            
            copy = Node(node.val)
            new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(depthFirstSearch(neighbor))

            return copy

        return depthFirstSearch(node) if node else None


        