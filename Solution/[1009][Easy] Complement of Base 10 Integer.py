import math


class Solution:
    def bitwiseComplement(self, n):
        ones = (2 << int(math.log(max(n, 1), 2))) - 1
        return ones - n