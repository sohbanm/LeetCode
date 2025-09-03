#my solution, marks cells to not flip in a hashset
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) - 1
        n = len(board[0]) - 1
        notFlip = set()

        def sameRegion(x, y):
            if x == -1 or y == -1 or x == (m + 1) or y == (n + 1) or board[x][y] == "X" or (x, y) in notFlip:
                return

            notFlip.add((x,y))
            sameRegion(x + 1, y)
            sameRegion(x, y + 1)
            sameRegion(x - 1, y)
            sameRegion(x, y - 1)
            

        for r in range(m + 1):
            for c in range(n + 1):
                if board[r][c] == "O" and (r in [0, m] or c in [0, n]):
                    sameRegion(r, c)

        for m in range(1, m + 1):
            for n in range(1, n + 1):
                if board[m][n] == "O" and (m, n) not in notFlip:
                    board[m][n] = "X"

# neetcode solution, uses T placeholder to mark cells to not flip
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            capture(r - 1, c)

        # (DFS) capture unsurrounded regions (O -> T)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        #capture surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        #uncapture the unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"