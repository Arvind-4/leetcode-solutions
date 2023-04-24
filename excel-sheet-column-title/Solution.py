// https://leetcode.com/problems/excel-sheet-column-title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber != 0:
            answer += chr(ord('A') + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
        return answer[::-1]