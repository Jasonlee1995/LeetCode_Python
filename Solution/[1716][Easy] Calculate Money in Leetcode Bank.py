class Solution:
    def totalMoney(self, n):
        s, r = n//7, n%7
        return 28 * s + 7 * ((s * (s-1)) // 2) + (r * (2*s+r+1)) // 2