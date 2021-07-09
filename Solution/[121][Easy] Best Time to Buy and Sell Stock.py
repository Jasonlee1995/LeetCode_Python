class Solution:
    def maxProfit(self, prices):
        answer, buy = 0, prices[0]
        for sell in prices:
            answer = max(answer, sell-buy)
            buy = min(buy, sell)
        return answer
