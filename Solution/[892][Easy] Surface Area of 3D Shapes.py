class Solution:
    def surfaceArea(self, grid):
        n, answer = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]: answer += 4*grid[i][j] + 2
                if i: answer -= 2 * min(grid[i-1][j], grid[i][j])
                if j: answer -= 2 * min(grid[i][j-1], grid[i][j])
        return answer