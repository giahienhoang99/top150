class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - cannot rob adjacent houses
        - houses are in a circle (since 1st and last houses are adjacent)
        => max rob path either includes first house or last house

        => result = max(
                        max(f(i) for i from 0 to n - 2),
                        max(f(j) for j from 1 to n - 1)
                    )
        => 2 times house robber 1 then find the max between max amount of each
        
        recursive function:
        f(i) = max amount robbed at i-th house
    
        => at i, either choose prev house or prev2 + cur
        f(i) = max(f(i-1), f(i-2) + nums[i])
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        result = max(dp)

        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])

        for i in range(2, n - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i + 1])

        result = max(result, max(dp))
        return result