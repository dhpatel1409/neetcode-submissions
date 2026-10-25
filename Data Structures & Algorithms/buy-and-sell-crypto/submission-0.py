class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        buy=prices[0]
        
        for i in range(1,len(prices)):
            sell=prices[i]
            prof=sell-buy
            maxprof=max(prof,maxprof)
            if prices[i]<buy:
                buy=prices[i]
        return maxprof
        # while i<len(prices)

        
        