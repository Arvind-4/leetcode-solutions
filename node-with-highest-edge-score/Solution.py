// https://leetcode.com/problems/node-with-highest-edge-score

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = {}
        maxx = 0
        for i in range(len(edges)):
            if edges[i] in graph:
                graph[edges[i]].append(i)
            else:
                graph[edges[i]] = [i] 
        
        s, count = 0, 0

        for key, value in graph.items():
            if sum(value) > s:
                s = sum(value)
                count = key
            if sum(value) == s and key < count:
                count = key
        return count