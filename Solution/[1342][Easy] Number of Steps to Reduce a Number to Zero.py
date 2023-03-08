class Solution:
    def numberOfSteps(self, num):
        bin_num = bin(num)[2:]
        return len(bin_num) + bin_num.count('1') - 1