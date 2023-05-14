class Solution:
    def xorOperation(self, n, start):
        if start % 4 <= 1:
            if   n % 4 == 0: return 0
            elif n % 4 == 1: return start + 2 * (n-1)
            elif n % 4 == 2: return 2
            elif n % 4 == 3: return 2 + start + 2 * (n-1)

        else:
            if   n % 4 == 0: return start ^ 2 ^ (start + 2 * (n-1))
            elif n % 4 == 1: return start
            elif n % 4 == 2: return start ^ (start + 2 * (n-1))
            elif n % 4 == 3: return start ^ 2