// https://leetcode.com/problems/dota2-senate

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        ridx = deque([i for i in range(n) if senate[i]=='R'])
        didx = deque([j for j in range(n) if senate[j]=='D'])

        while ridx and didx:
            r = ridx.popleft()
            d = didx.popleft()

            if r < d:
                ridx.append(n + r)
            else:
                didx.append(n + d)

        
        return "Radiant" if ridx else "Dire"
