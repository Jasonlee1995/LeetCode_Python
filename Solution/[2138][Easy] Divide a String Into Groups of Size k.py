class Solution:
    def divideString(self, s, k, fill):
        if len(s) % k > 0: s += fill * (k - len(s)%k)
        return [s[idx:idx+k] for idx in range(0, len(s), k)]