class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            if cost[i-1] < cost[i-2]: cost[i] += cost[i-1]
            else: cost[i] += cost[i-2]
        return min(cost[-2:])
