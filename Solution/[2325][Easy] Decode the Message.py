class Solution:
    def checkXMatrix(self, grid):
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if (c == r) or (c == n-1-r):
                    if grid[r][c] == 0:
                        return False
                elif grid[r][c] != 0:
                    return False
        return True