class Solution:
    def isSubsequence(self, s, t):
        idx0, idx1 = 0, 0
        while (idx0 < len(s)) and (idx1 < len(t)):
            if s[idx0] == t[idx1]: idx0, idx1 = idx0+1, idx1+1
            else: idx1 += 1
        return idx0 == len(s)
