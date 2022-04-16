class Solution:
    def backspaceCompare(self, s, t):
        idx1, idx2, skip1, skip2 = len(s)-1, len(t)-1, 0, 0
        while (idx1 > -1) or (idx2 > -1):
            if (idx1 > -1) and (s[idx1] == '#'): idx1, skip1 = idx1-1, skip1+1
            elif (idx2 > -1) and (t[idx2] == '#'): idx2, skip2 = idx2-1, skip2+1
            elif skip1: idx1, skip1 = idx1-1, skip1-1
            elif skip2: idx2, skip2 = idx2-1, skip2-1
            elif ((idx1 > -1) and (idx2 > -1)) and (s[idx1] == t[idx2]): idx1, idx2 = idx1-1, idx2-1
            else: break
        return (idx1 < 0) and (idx2 < 0)
