class Solution:
    def minimumCost(self, cost):
        return sum(cost) - sum(sorted(cost, reverse=True)[2::3])