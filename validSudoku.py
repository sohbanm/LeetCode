class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anithing, modifi board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        """"These loops are just for us to find and record the preexisting numbers in the sudoku board"""
        for i in range(9):
            for j, val in enumerate(board[i]):
                if board[i][j] != '.':
                    rows[i].add(int(val))
                    cols[j].add(int(val))
                    box_idx = i // 3 * 3 + j // 3 #this will make it so the boxs are labeled 1-8
                    boxs[box_idx].add(int(val))

        def backTrack(i, j):
            nonlocal solved
            if i == 9:
                solved = True
                return

            # These 2 lines are a calculation trick to make sure that i is increased if j is at the 9th
            # position and j is increases until it reaches 9 and then becomes 0 again 
            new_i = i + (j+1) // 9 
            new_j = (j+1) % 9

            if board[i][j] != '.':
                backTrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    box_idx = i // 3 * 3 + j // 3
                    if num not in rows[i] and num not in cols[j] and num not in boxs[box_idx]:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxs[box_idx].add(num)
                        board[i][j] = str(num)

                        backTrack(new_i, new_j)
                        
                        if not solved:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxs[box_idx].remove(num)
                            board[i][j] = '.'


        solved = False
        backTrack(0, 0)