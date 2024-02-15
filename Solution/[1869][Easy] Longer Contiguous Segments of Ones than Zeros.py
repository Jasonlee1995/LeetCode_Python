class Solution:
    def checkZeroOnes(self, s):
        max_seq_0 = max(len(zeros) for zeros in s.split('1'))
        max_seq_1 = max(len(ones)  for ones  in s.split('0'))
        return max_seq_1 > max_seq_0