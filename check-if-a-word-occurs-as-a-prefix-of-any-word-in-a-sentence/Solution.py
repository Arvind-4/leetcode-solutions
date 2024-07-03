// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        count = 0

        for word in words:
            count += 1
            if word.startswith(searchWord):
                return count

        return -1

        