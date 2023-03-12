class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        r, c, answer = 0, n-1, 0
        while (r < m) and (0 <= c):
            if grid[r][c] >= 0:
                r += 1
            else:
                answer += m-r
                c -= 1
        return answer