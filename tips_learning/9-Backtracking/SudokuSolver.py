from collections import defaultdict
from typing import List


def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        

        012 // 3 = 0 -> 0
        345 // 3 = 1 -> 1
        678 // 3 = 2 -> 2

        2d to 1d:  (row // 3) * 3 + (col // 3)

        4,3 -> 4
        3 + 1
        8,8 -> 8
        6 + 2 
        8,3 -> 7
        6 + 1
        6, 8 -> 8
        6 + 2
        """
        def get_square_index(x, y):
            return (x // 3) * 3 + y // 3

        # 27 sets
        col = defaultdict(set)
        row = defaultdict(set)
        squares = defaultdict(set)

        # list of empty cells
        empty = []

        # fill in sets with numbers
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                if cell != ".":
                    row[i].add(cell)
                    col[j].add(cell)
                    squares[get_square_index(i, j)].add(cell)
                else:
                    empty.append((i, j))

        # backtrack from empty cells
        def backtrack(i):
            # end condition: i == len(empty)
            if i == len(empty):
                return True
            
            # N empty cells
            # choices for each cell: 1->9
            # can fill if not in row, col, squares

            x, y = empty[i]
            sqr_idx = get_square_index(x, y)

            for num in range(1, 10):
                s = str(num)
                if s in row[x]:
                    continue
                if s in col[y]:
                    continue
                if s in squares[sqr_idx]:
                    continue
                
                # make decision
                board[x][y] = s
                row[x].add(s)
                col[y].add(s)
                squares[sqr_idx].add(s)
                
                if backtrack(i + 1):
                    return True
                
                squares[sqr_idx].remove(s)
                col[y].remove(s)
                row[x].remove(s)
                board[x][y] = "."
            
            return False

        backtrack(0)