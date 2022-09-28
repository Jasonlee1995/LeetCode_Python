class Solution:
    def findJudge(self, n, trust):
        infos = [0] * n
        for a, b in trust:
            infos[a-1] -= 1
            infos[b-1] += 1
        
        for i in range(n):
            if infos[i] == n-1:
                return i+1
        return -1