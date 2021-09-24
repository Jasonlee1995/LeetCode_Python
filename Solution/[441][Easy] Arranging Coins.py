class Solution:
    def arrangeCoins(self, n):
        answer = int(((8*n + 1) ** 0.5 - 1) / 2)
        return answer
