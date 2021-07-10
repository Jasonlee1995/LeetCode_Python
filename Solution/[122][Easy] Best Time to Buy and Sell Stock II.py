class Solution:
    def maxProfit(self, prices):
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: answer += (prices[i] - prices[i-1])
        return answer
