class Solution:
    def mySqrt(self, x):
        left, right = 0, x+1
        while right - left > 1:
            mid = (left + right) // 2
            if x < mid * mid: right = mid
            else: left = mid
        return left
