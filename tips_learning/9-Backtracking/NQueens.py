from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    """
    backtracking and record every solution to a list

    problem: figure out how to check if a queen is attacking another
    - queen can attack horizontally, vertically, and diagonally
    - horizontal and vertical checking is ez
    - diagonal can be divided into 2 direction
        + top left -> bot right
        + top right -> bot left

    4x4 chess board
    00 01 02 03
    10 11 12 13
    20 21 22 23
    30 31 32 33

    first diag (top left -> bot right) or y = -x:
        - 10 -> 32: -1
        - 00 -> 33:  0
        - 01 -> 23:  1
        => j - i = diag #
        => mark diags (- n + 1) to (n - 1)

    2nd diag (top right -> bot left) or y = x:
        - i + j = diag #
        - 03 -> 30: all entries on this diag has i+j = 3
        => mark diags 0 to 2n - 1

    """
    # create chess board
    board = [["."] * n for _ in range(n)]
    print(board)

    # sets for keeping track of attacked status of each row, col, diag
    verti, hori = set(), set()
    first_diag, sec_diag = set(), set()

    solutions = []

    def record_solution():
        sol = []
        for row in board:
            sol.append("".join(row))
        solutions.append(sol)

    def backtrack(row):
        # stop condition:
        if row == n:
            record_solution()
            print(board)
            return

        for col in range(n):
            if col in verti or row in hori:
                continue
            if col - row in first_diag:
                continue
            if col + row in sec_diag:
                continue

            verti.add(col)
            hori.add(row)
            first_diag.add(col - row)
            sec_diag.add(col + row)
            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."
            sec_diag.remove(col + row)
            first_diag.remove(col - row)
            hori.remove(row)
            verti.remove(col)

    backtrack(0)
    return solutions
