class Solution:
    def subtractProductAndSum(self, n):
        p, s = 1, 0
        while n:
            n, r = divmod(n, 10)
            p *= r
            s += r
        return p - s