class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        return (numBottles * numExchange - 1) // (numExchange - 1)