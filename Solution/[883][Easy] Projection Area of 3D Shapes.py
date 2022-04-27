class Solution:
    def projectionArea(self, grid):
        R, C = len(grid), len(grid[0])
        answer = 0
        for r in range(R): answer += C - grid[r].count(0)
        for r in range(R): answer += max(grid[r])
        for c in range(C): answer += max(grid[r][c] for r in range(R))
        return answer
