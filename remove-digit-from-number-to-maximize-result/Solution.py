// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answer = 0
        for i, num in enumerate(list(number)):
            if num == digit:
                answer = max(answer, int(number[:i] + number[i + 1:]))

        return str(answer)
            