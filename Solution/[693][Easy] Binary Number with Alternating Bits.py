class Solution:
    def hasAlternatingBits(self, n):
        return ('00' not in bin(n)) and ('11' not in bin(n))
