class Solution:
    def minOperations(self, s):
        zero_first = sum(s[idx] != str(idx%2) for idx in range(len(s)))
        return min(zero_first, len(s)-zero_first)