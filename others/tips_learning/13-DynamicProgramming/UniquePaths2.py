class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # check starting point if blocked
        if obstacleGrid[0][0]:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] else dp[i - 1][0]
        
        for i in range(1, n):
            dp[0][i] = 0 if obstacleGrid[0][i] else dp[0][i - 1]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m-1][n-1]

