class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices)<2:
            return 0
        l,r=0,1
        while r<=len(prices)-1:
            if prices[r]<prices[l]:
                l=r 
            max_profit=max(prices[r]-prices[l],max_profit)
            r+=1
            print(l,r)
        return max_profit
        
