class Solution:
    def generate(self, numRows):
        import math
        answer = [[math.comb(i, j) for j in range(i+1)] for i in range(numRows)]
        return answer
