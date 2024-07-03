// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        _bool = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= _max:
                _bool.append(True)
            else:
                _bool.append(False)
        return _bool