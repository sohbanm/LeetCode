# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

# my solution
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        left, middle, right = set(), set(), set()

        for r in range(1, 10):
            for c in range(1, 10):
                val = board[r-1][c-1]
                if val != ".":
                    if val in cols[c-1] or val in rows[r-1]:
                        return False

                    cols[c-1].add(val)
                    rows[r-1].add(val)
                
                    if 1 <= c <= 3:
                        if val in left:
                            return False
                        left.add(val)
                    elif 4 <= c <= 6:
                        if val in middle:
                            return False
                        middle.add(val)
                    elif 7 <= c:
                        if val in right:
                            return False
                        right.add(val)

                if r % 3 == 0:
                    if c == 3:
                        left = set()
                    elif c == 6:
                        middle = set()
                    elif c == 9:
                        right = set()

        return True

# better solution from neetcode 
# this one makes 9 boxes using (r // 3, c // 3) as the key
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True