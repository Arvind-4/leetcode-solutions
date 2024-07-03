// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqs = collections.defaultdict(set)

        n = len(board)

        for r in range(n):
            for c in range(n):
                el = board[r][c]
                if el == ".":
                    continue
                if el in rows[r] or el in cols[c] or el in sqs[(r // 3, c // 3)]: return 0
                cols[c].add(el)
                rows[r].add(el)
                sqs[(r // 3, c // 3)].add(el)
        return 1