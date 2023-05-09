class Solution:
    def finalPrices(self, prices):
        stack = []
        for idx, price in enumerate(prices):
            while stack and (prices[stack[-1]] >= price):
                prices[stack.pop()] -= price
            stack.append(idx)
        return prices