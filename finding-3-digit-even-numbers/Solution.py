// https://leetcode.com/problems/finding-3-digit-even-numbers

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        d = Counter(digits)
        print(d)
        for n in range(100, 1000, 2):
            flag = 0
            for i, j in Counter(str(n)).items():
                if d[int(i)] < j:
                    flag = 1
            if flag == 0:
                res.append(n)

        return res