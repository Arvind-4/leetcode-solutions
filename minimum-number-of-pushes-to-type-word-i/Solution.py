// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        shift = 1
        n = len(word)

        while n > 0:
            if n >= 8:
                count += 8 * shift
                n -= 8
            else:
                count += n * shift
                break
            shift += 1

        return count