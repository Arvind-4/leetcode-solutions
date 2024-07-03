// https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)

        x = tickets[k]

        time = 0

        for i, ticket in enumerate(tickets):
            buy = x
            if i > k: buy = x - 1
            time += min(buy, ticket)

        return time