class Solution:
    def numDecodings(self, s: str) -> int:
        """
        - need to remove leading zeroes
        
        recursive function? 

        f(i) = num ways to decode string up to ith num
        
        at i: 
            - if s[i] valid standalone: f(i) = f(i - 1)     (non zero)
            - if s[i] matchable w s[i-1]: f(i) = f(i - 2)   (10 - 26)
            - both: f(i) = f(i - 1) + f(i - 2)
        """
        n = len(s)
        dp = [0] * n
        dp[0] = int(s[0] != '0')

        for i in range(1, n):
            # check if cur char is non-zero (1-9)
            if int(s[i] != '0'):
                dp[i] = dp[i - 1]
            # check if matchable with prev char
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += 1 if i < 2 else dp[i - 2]

        return dp[n - 1]
            

