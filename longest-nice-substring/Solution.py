// https://leetcode.com/problems/longest-nice-substring

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ""
        stack = [s]
        while stack:
            word = stack.pop()
            if not word:
                continue
            set_ = set(list(word))
            for i, j in enumerate(word):
                if j.swapcase() not in set_:
                    stack.append(word[i + 1:])
                    stack.append(word[:i])
                    break
            else:
                res = max(res, word, key=len)

        return res