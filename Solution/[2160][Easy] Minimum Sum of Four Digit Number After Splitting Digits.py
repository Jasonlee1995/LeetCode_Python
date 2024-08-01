class Solution:
    def minimumSum(self, num):
        a, b, c, d = [int(n) for n in sorted(str(num))]
        return 10 * (a + b) + c + d