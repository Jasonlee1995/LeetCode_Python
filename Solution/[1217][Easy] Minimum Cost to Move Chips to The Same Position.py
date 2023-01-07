class Solution:
    def minCostToMoveChips(self, position):
        dic = {0 : 0, 1 : 0}
        for p in position:
            dic[p%2] += 1
        return min(dic[0], dic[1])