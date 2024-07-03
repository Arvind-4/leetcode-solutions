// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        total = 0
        flag = 0
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            # print(i)
        # print(d)
        for i in d:
            if d[i] % 2 == 0:
                total += d[i]
            else:
                flag = 1
                total += d[i] - 1
        if flag == 1:
            return total + 1
        return total



        return 0
        