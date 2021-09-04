class Solution(object):
    def isPowerOfFour(self, n):
        return (n > 0) and (n&(n-1) == 0) and (len(bin(n))%2 == 1)
