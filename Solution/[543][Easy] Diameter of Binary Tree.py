class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        for idx in range(0, len(s), 2*k):
            s[idx:idx+k] = reversed(s[idx:idx+k])
        return ''.join(s)
