// https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        i, j = edges[0][0], edges[0][1]
        if  i in edges[1]:
            return i
        return j