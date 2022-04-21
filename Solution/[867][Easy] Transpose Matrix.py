class Solution:
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        answer = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                answer[j].append(matrix[i][j])
        return answer
