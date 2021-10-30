class Solution:
    def checkPerfectNumber(self, num):
        Pnums = [(2 ** (p-1)) * (2 ** p - 1) for p in [2, 3, 5, 7, 13]]
        return num in Pnums
