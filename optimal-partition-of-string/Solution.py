// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        temp = ""
        count = 1
        for i in s:
            if i not in temp:
                temp += i
            else:
                temp = i
                count += 1
        
        return count