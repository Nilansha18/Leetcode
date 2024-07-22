class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minm=prices[0]
        for i in range(len(prices)):
            minm= min (minm,prices[i])
            maxprofit=max(maxprofit,prices[i]-minm)   
        return maxprofit
        