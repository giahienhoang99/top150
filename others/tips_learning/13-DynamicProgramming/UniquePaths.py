from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        f(i,j) = # unique paths from 00 to ij

        f(i,j) = f(i-1,j) + f(i,j-1)

        observation: 
        - there is only 1 unique path for cells on the 1st row and the 1st col 
          (since the robot can only move right or down)
        - for cells not on 1st row and 1st col, the paths that robot can come
        from is either the cell above or the cell on the left
        => f(i,j) = f(i-1,j) + f(i,j-1) with i,j != 0,0

        problem:
            - pure recursion costs too much time exploring same paths again
            => use memoization using an m x n grid
            => grid[i][j] = f(i,j)

        res = f(m-1, n-1) = num unique paths to bot right cell
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]

    def uniquePaths(self, m: int, n: int) -> int:
        """
        f(i,j) = # unique paths from 00 to ij

        f(i,j) = f(i-1,j) + f(i,j-1)

        observation: 
        - there is only 1 unique path for cells on the 1st row and the 1st col 
          (since the robot can only move right or down)
        - for cells not on 1st row and 1st col, the paths that robot can come
        from is either the cell above or the cell on the left
        => f(i,j) = f(i-1,j) + f(i,j-1) with i,j != 0,0

        problem:
            - pure recursion costs too much time exploring same paths again
            => use memoization using an m x n grid
            => grid[i][j] = f(i,j)

        res = f(m-1, n-1) = num unique paths to bot right cell
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]
        """

        """
        min steps m + n - 2
        di xuong m - 1
        di phai n - 1
        Ckn = n!
        /
        k!(n-k)!

        n = min steps
        k = 
        """
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))