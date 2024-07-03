// https://leetcode.com/problems/maximum-matching-of-players-with-trainers

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i, j, ans = 0, 0, 0
        players.sort()
        trainers.sort()

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1
        return ans