class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        for row, col in zip(matrix, zip(*matrix)):
            if (len(set(row)) != n) or (len(set(col)) != n):
                return False
        return True