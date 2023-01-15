class Solution:
    def oddCells(self, m, n, indices):
        row, col = [False] * m, [False] * n
        for r, c in indices:
            row[r] ^= True
            col[c] ^= True
        
        row_odd, row_even = sum(row), m - sum(row)
        col_odd, col_even = sum(col), n - sum(col)

        return row_odd * col_even + row_even * col_odd