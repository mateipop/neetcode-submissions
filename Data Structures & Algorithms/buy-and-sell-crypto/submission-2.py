class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        i, j = 0, 1
        maxP = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                curP = prices[j] - prices[i]
                maxP = max(maxP, curP)
            else:
                i = j
            j += 1
        return maxP
