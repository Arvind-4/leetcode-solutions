// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = []
        s = set()
        for i in range(len(skill) // 2):
            l.append((skill[i], skill[-i - 1]))
            s.add(skill[i] + skill[-i - 1])
        if len(s) != 1:
            return -1
        prod = 0
        for i, j in l:
            prod += (i * j)
        return prod