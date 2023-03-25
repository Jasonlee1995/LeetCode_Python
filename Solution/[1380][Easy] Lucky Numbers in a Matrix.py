class Solution:
    def luckyNumbers (self, matrix):
        m, n = len(matrix), len(matrix[0])
        row_min = set(min(matrix[r]) for r in range(m))
        col_max = set(max(col) for col in zip(*matrix))
        return list(row_min & col_max)