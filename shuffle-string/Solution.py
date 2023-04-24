// https://leetcode.com/problems/shuffle-string

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(zip(indices,s))
        arr.sort()
        letters = [ second for _,second in arr ]
        return ''.join(letters)

