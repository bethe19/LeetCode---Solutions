class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[i] < prices[j] and (prices[j] - prices[i]) > maxProfit:
        #             maxProfit = prices[j] - prices[i]
        # return maxProfit
        bestBuy = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] < bestBuy:
                bestBuy = prices[i]
                continue
            # bestBuy = min(bestBuy, prices[i])
            if maxProfit < (prices[i]-bestBuy):
                maxProfit = prices[i]-bestBuy
            # maxProfit = max(maxProfit, prices[i]-bestBuy)
        return maxProfit