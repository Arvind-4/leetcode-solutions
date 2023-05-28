// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphabets = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        l, result = [], []
        if len(digits) == 0: return l

        for digit in digits:
            l.append(alphabets[digit])
        code = product(*l)
        for k in code:
            result.append("".join(k))

        return result