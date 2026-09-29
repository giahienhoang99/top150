class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        f(i) = max(f(j) + 1) with nums[i] > nums[j] and j < i
        res = max(f(i))
        """
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)