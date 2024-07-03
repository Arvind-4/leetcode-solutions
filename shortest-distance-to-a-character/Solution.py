// https://leetcode.com/problems/shortest-distance-to-a-character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = []
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                l.append(i)
        
        for i in range(len(s)):
            tmp = []
            for j in l:
                tmp.append(abs(i - j))
            ans.append(min(tmp))
        return ans