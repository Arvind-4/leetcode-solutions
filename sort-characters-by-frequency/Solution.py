// https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        string = ""
        for i in s:
            if i not in d: d[i] = 1
            else: d[i] += 1

        for i in sorted(d.items(), key=lambda x:x[1]):
            string += i[0] * i[1]
        return string[::-1]
