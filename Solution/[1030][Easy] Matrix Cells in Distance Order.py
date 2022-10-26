class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        answer, stack, check = [], [(rCenter, cCenter)], set()
        while stack:
            temp = set()
            for r, c in stack:
                if (0 <= r < rows) and (0 <= c < cols) and ((r, c) not in check):
                    check.add((r, c))
                    answer.append([r, c])
                    temp.update([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
            stack = temp
        return answer