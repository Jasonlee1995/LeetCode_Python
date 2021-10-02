class Solution:
    def findComplement(self, num):
        return num ^ (2 ** num.bit_length() - 1)
