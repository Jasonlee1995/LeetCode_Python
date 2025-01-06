class Solution:
    def smallestEvenMultiple(self, n):
        return n << (n & 1)