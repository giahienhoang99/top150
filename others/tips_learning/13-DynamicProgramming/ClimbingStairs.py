class Solution:
    def climbStairs(self, n: int) -> int:
        """
        f(i) = number of ways to reach i-th stair
        f(i) = f(i-1) + f(i-2)
        """
        if n == 1:
            return 1
        dp = [1] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
