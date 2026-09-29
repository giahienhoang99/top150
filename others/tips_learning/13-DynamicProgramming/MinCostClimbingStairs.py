class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        - can start from dp[0] or dp[1]
        f(0) and f(1) = 0
        f(i) = min(f(i-1) + cost[i-1], f(i-2) + cost[i-2])
        
        - can reach the end from either dp[-1] or dp[-2]
        - return min(dp[-1], dp[-2]) ?
        - or can create dp with len = len cost + 1 and return dp[-1]?
        """
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        print(dp)
        return dp[-1]