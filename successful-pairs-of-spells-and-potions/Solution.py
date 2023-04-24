// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        sortedPotions = sorted(potions)
        output = []
        for spell in spells:
            count = len(sortedPotions) - bisect_left(sortedPotions, (success + spell - 1) // spell)
            output.append(count)

        return output
