// https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in set(allowed):
                    count += 1
                    break
        return len(words) - count