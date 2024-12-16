import itertools

class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        center_idxs = itertools.product(range(1, n-1), range(1, n-1))

        answer = []
        for center_idx in center_idxs:
            x, y  = center_idx
            stack = []
            for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):
                stack.append(grid[x+dx][y+dy])
            answer.append(max(stack))
        return [answer[idx:idx+n-2] for idx in range(0, (n-2)*(n-2), n-2)]