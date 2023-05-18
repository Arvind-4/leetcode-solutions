// https://leetcode.com/problems/number-of-provinces

class Solution:

    def dfs(self, isConnected: List[List[int]], n: int, src: int, visited: List[bool]) -> None:
        visited[src] = True
        for i in range(n):
            if isConnected[src][i] and visited[i] is False:
                self.dfs(isConnected, n, i, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = [False] * n

        for i in range(n):
            if visited[i] is False:
                count += 1
                self.dfs(isConnected, n, i, visited)
        return count


        

    