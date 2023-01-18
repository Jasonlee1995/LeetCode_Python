class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        arr = sum(grid, [])
        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]
        return [arr[r:r+n] for r in range(0, len(arr), n)]