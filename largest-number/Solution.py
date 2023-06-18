// https://leetcode.com/problems/largest-number

class LargerNumKey(str):
    def __lt__(x: int, y: int) -> bool:
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key = LargerNumKey)
        largestNumber = ''.join(nums)
        return "0" if largestNumber[0] == "0" else largestNumber

