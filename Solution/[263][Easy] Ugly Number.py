class Solution:
    def isUgly(self, n):
        for num in [2, 3, 5]:
            while n and (n%num == 0):
                n = n//num
        return n == 1
