class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            val = prices[i] - minimum
            ans = max(ans, val)
            minimum = min(prices[i], minimum)
        return ans