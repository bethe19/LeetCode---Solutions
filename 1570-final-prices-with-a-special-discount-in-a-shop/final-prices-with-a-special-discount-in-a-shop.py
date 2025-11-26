class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        result = prices[:]
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                result[idx] = prices[idx] - price
            stack.append(i)
        return result