class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        answer = 0
        for r in range(m):
            for c in range(n):
                if (mat[r][c] == 1) and (rows[r] == 1) and (cols[c] == 1):
                    answer += 1
        return answer