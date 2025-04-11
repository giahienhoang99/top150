from typing import List


def exist(self, board: List[List[str]], word: str) -> bool:
    """
    - find list of starting positions
    - backtracking to explore all paths from valid starting points
        - stop condition: len(cur_list) == len(word)
        - values to pass in backtrack():
            + row, col
            + cur_list: list of chars explored
            + idx: index to check next valid char in word
            + visited: set to track visited cells
        - check 4 directions if match word[i]
    """
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    M, N, L = len(board), len(board[0]), len(word)

    def backtrack(row, col, idx, visited) -> bool:
        if idx == L:
            return True
        # check board constraints, visited cell, diff char
        if not (0 <= row < M and 0 <= col < N):
            return False
        if (row, col) in visited:
            return False
        if board[row][col] != word[idx]:
            return False

        visited.add((row, col))

        for dx, dy in DIRECTIONS:
            nx, ny, nidx = row + dx, col + dy, idx + 1
            if backtrack(nx, ny, nidx, visited):
                return True

        visited.remove((row, col))

        return False

    # start exploring from the valid start points
    for i in range(M):
        for j in range(N):
            if board[i][j] == str(word[0]):
                if backtrack(i, j, 0, set()):
                    return True

    return False
