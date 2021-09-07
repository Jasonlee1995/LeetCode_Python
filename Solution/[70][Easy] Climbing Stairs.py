class Solution:
    def climbStairs(self, n):
        s0, s1 = 1, 1
        for i in range(1, n):
            s0, s1 = s1, s0+s1
        return s1
