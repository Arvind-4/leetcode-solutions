// https://leetcode.com/problems/add-to-array-form-of-integer

import sys

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(20000)
        number = int("".join(map(str, num)))
        answer = list(str(number + k))
        return list(map(int, answer))