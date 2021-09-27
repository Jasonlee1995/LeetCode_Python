class Solution:
    def findContentChildren(self, g, s):
        g.sort(); s.sort()
        answer = 0
        idx0, idx1 = 0, 0
        while (idx0 < len(g)) and (idx1 < len(s)):
            if g[idx0] <= s[idx1]:
                answer += 1
                idx0, idx1 = idx0+1, idx1+1
            else:
                idx1 += 1
        return answer
