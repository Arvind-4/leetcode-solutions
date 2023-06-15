// https://leetcode.com/problems/plus-one

import sys
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sys.set_int_max_str_digits(20000)
        number = int("".join(map(str, digits)))
        answer = list(str(number + 1))
        return list(map(int, answer))