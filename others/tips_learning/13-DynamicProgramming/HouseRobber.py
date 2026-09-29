class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        rule:
        - cannot rob 2 adj houses

        recursive function:
        f(i) = max amount robbed at i-th house
    
        => at i, either choose prev house or prev2 + cur
        f(i) = max(f(i-1), f(i-2) + nums[i])


        dry run:
        nums = [1,2,3,1]
        dp = [1,2,x,x]
        
        i = 2:
        2 or 1 + 3
        => 1+3 = 4
        => dp = [1,2,4,x]

        i = 3:
        3 or 2 + 1
        => either 
        => dp = [1,2,4,3]

        result = max(dp) = 4
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) # rob bigger

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)
        