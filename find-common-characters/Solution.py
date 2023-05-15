// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        d, answer = {}, []

        for idx, word in enumerate(words):
            for letter in word:
                if letter not in d:
                    d[letter] = [0] * len(words)
                    d[letter][idx] = 1
                else:
                    d[letter][idx] += 1

        for letter in d:
            for i in range(0, min(d[letter])):
                answer.append(letter)

        return answer