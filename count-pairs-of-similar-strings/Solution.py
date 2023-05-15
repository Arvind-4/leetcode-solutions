// https://leetcode.com/problems/count-pairs-of-similar-strings

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = [set(i) for i in words]
        count = []

        for i in range(len(sets)):
            for j in range(len(sets)):
                if sets[i] == sets[j] and i < j:
                    count.append((sets[i], sets[j]))

        print(count)
        return len(count)