// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for digit in digits:
            s += str(digit)
        num = int(s) + 1
        nums = list(str(num))
        return list(map(int, nums))
        