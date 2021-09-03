class Solution:
    def isPowerOfThree(self, n):
        return (n > 0) and (3 ** 19 % n == 0)
