// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = {}

        for edge in edges:
            [u, v] = edge
            if not u in graph: graph[u] = []
            if not v in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        for k, v in graph.items():
            if len(v) == max(graph) - 1:
                return k
            