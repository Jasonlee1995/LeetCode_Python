class Solution:
    def getRow(self, rowIndex):
        import math
        return [math.comb(rowIndex, i) for i in range(rowIndex+1)]
