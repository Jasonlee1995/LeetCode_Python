class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        answer = 0
        for i in range(n):
            answer += mat[i][i] + mat[i][-i-1]
        if n % 2 == 1:
            answer -= mat[n//2][n//2]
        return answer