// https://leetcode.com/problems/total-cost-to-hire-k-workers

push = heapq.heappush
pop = heapq.heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, q: int) -> int:
        n = len(costs)
        H = []
        for i in range(q):
            H.append((costs[i], i, 'L'))
        i += 1
        j = n-1
        while j >= i and (n-j) <= q:
            H.append((costs[j], j, 'R'))
            j -= 1           
        
        heapq.heapify(H)
        
        res = 0
        
        for _ in range(k):
            v, ind ,d = pop(H)
            res += v
            if i <= j:
                if d == 'R':
                    push(H, (costs[j], j, 'R'))
                    j -= 1
                else:
                    push(H, (costs[i], i, 'L'))
                    i += 1
        
        return res
 