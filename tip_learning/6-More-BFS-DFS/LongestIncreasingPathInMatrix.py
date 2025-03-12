from typing import List


def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # for each cell, dfs for exploring path as deep as possible
        # time complexity: using a cache would take O(mn)
        DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
        m, n = len(matrix), len(matrix[0])
        cache = {}
        def explore(row, col):
            # check if calculated
            if (row, col) in cache:
                return cache[(row, col)]
            # path length minimum len = 1 cell
            longest_path = 1
            # explore each direction for each cell
            path = 0
            for dx, dy in DIRECTIONS:
                nx, ny = row + dx, col + dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] <= matrix[row][col]:
                    continue
                path = 1 + explore(nx, ny)
                longest_path = max(longest_path, path)
            
            # store longest path at (row, col) in cache
            cache[(row, col)] = longest_path
            return longest_path

        result = 1
        for i in range(m):     
            for j in range(n):
                result = max(result, explore(i, j))
        return result