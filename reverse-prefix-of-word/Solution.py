// https://leetcode.com/problems/reverse-prefix-of-word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        string = ""
        if ch not in word:
            return word

        for i in word:
            if ch != i:
                string += i
                idx += 1
            if ch == i:
                string += i
                idx += 1
                break

        return string[::-1] + word[idx:]