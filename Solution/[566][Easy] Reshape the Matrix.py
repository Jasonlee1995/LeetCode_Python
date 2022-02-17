class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if (m*n % r != 0) or (m == r): return mat
        r, c = r, m*n // r
        answer = [[] for _ in range(r)]
        idx_c = -1
        for x in range(m):
            for y in range(n):
                if (n*x + y) % c == 0:  idx_c += 1
                answer[idx_c].append(mat[x][y])
        return answer
