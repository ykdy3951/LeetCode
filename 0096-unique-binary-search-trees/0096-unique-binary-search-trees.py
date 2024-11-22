class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = dp[0] = 1
        
        for i in range(2, n + 1):
            tmp = 0
            for j in range(i):
                tmp += dp[j] * dp[i - 1 - j]
            dp[i] = tmp

        return dp[n]

"""
1 -> 1
2 -> 2
3 -> (2) + (1) + (2)
4 -> (3) + (2) * (1) + (1) * (2)
"""