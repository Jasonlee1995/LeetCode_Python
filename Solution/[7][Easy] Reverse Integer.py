class Solution:
    def reverse(self, x):
        overflow = [-2147483648, 2147483647]
        sign = -1 if x < 0 else 1
        x *= sign
        result = 0
        while x:
            pop = x % 10
            x = x // 10
            if (result > overflow[1]//10) or ((result == overflow[1]//10) and (pop > 7)): return 0
            if (result < overflow[0]//10) or ((result == overflow[0]//10) and (pop < -8)): return 0
            result = 10 * result + pop
        return sign * result
